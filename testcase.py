import signal
import subprocess
import os

from utility import TemporaryFile, green_text, red_text

def alarm_handler(signum, frame):
	raise TimeoutError()

class TestCase:
	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
		self.timeout_seconds = 1
		self.containing_folder_name = os.path.basename(os.path.dirname(self.input_path))

	def __repr__(self):
		return 'in: ' + self.input_path + ' out: ' + self.output_path

	def run(self, executable, cmd_args):
		signal.signal(signal.SIGALRM, alarm_handler)
		signal.alarm(self.timeout_seconds)
		try:
			actual_output = subprocess.check_output(
				"{} {} < {}".format(executable, cmd_args, self.input_path),
				shell=True
			).decode("utf-8")
		except TimeoutError:
			return TimedoutTestCaseResult()
		except subprocess.CalledProcessError:
			return BadExitCodeTestCaseResult()


		# temporary thing, cuz of saeed's mistake
		actual_output = actual_output.replace('value for money', 'value_for_money') \
			.replace('overal rating', 'overal_rating')

		with TemporaryFile(actual_output) as actual_output_filename:
			completed_process = subprocess.run(
				"diff -b {} {}".format(self.output_path, actual_output_filename),
				check = False,
				shell = True,
				stdout= subprocess.PIPE
			)
		if completed_process.returncode == 0:
			return CorrectTestCaseResult()
		else:
			diff_output = completed_process.stdout.decode("utf-8")
			return IncorrectTestCaseResult(diff_output)


class CorrectTestCaseResult:
	def __init__(self):
		self.type_string = "correct"

	def to_string(self):
		return green_text(self.type_string)

class IncorrectTestCaseResult:
	def __init__(self, diff_output):
		self.type_string = "incorrect"
		self.diff_output = diff_output

	def to_string(self):
		result = "incorrect (left:expected, right: actual):\n"
		result += self.diff_output
		return red_text(result)

class TimedoutTestCaseResult:
	def __init__(self):
		self.type_string = "timed_out"

	def to_string(self):
		return red_text(self.type_string)

class BadExitCodeTestCaseResult:
	def __init__(self):
		self.type_string = "bad_exit_code"

	def to_string(self):
		return red_text(self.type_string)
