import argparse
import os
import re

from testcase import TestCase
from utility import red_text, green_text

def gather_all_testcases_in_folder(foldername):
	filenames = sorted(os.listdir(foldername))
	result = []

	for filename in filenames:
		path = os.path.join(foldername, filename)

		if os.path.isdir(path):
			result += gather_all_testcases_in_folder(path)
		else: 
			match = re.match('(.+)\.in$', filename) 
			if match:
				input_filename = match.group(1)
				if (input_filename + '.out') in filenames:
					new_test_case = TestCase(
						os.path.abspath(path),
						os.path.abspath(os.path.join(foldername, input_filename + '.out'))
					)
					result.append(new_test_case)
				else:
					raise Exception("found *.in file with no corresponding *.out file: " + path)

	return result


def print_summary(summary):
	print(
		'correct:', green_text(str(summary['correct'])),
		'incorrect:', red_text(str(summary['incorrect'])),
		'timed_out:', red_text(str(summary['timed_out'])),
		'bad_exit_code:', red_text(str(summary['bad_exit_code']))
	)

def print_summary_by_folder(summary_by_folder):
	for foldername in summary_by_folder:
		print(foldername, ': ', end='')
		print_summary(summary_by_folder[foldername])

def print_summary_overall(summary):
	print('overall: ', end='')
	print_summary(summary)

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--exe', '-e', required=True, help='path to the executable to be tested.', dest="executable")
	parser.add_argument('--tests', '-t', required=True, help='path to the folder containing the tests', dest="test_folder")
	parser.add_argument('--args', '-a', required=False,
		help='command line arguments to be passed to the executable', dest='commandline_args')
	args = parser.parse_args()

	testcases = gather_all_testcases_in_folder(args.test_folder)

	# ensure no address breaks because of the upcoming os.chdir:
	args.executable = os.path.abspath(args.executable)
	args.test_folder = os.path.abspath(args.test_folder)
	
	os.chdir(os.path.dirname(args.executable))

	summary_by_folder = {}
	summary_overall = {'correct': 0, 'incorrect': 0, 'timed_out': 0, 'bad_exit_code': 0}
	for testcase in testcases:
		print('testing {}:'.format(testcase.input_path), end=' ')
		result = testcase.run(args.executable, args.commandline_args)
		print(result.to_string())
		summary_overall[result.type_string] += 1

		if testcase.containing_folder_name not in summary_by_folder:
			summary_by_folder[testcase.containing_folder_name] = {'correct': 0, 'incorrect': 0, 'timed_out': 0, 'bad_exit_code': 0}
			
		summary_by_folder[testcase.containing_folder_name][result.type_string] += 1

	print_summary_overall(summary_overall)
	print_summary_by_folder(summary_by_folder)
