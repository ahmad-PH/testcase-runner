import os

class TemporaryFile:
	n_temp_files = 0

	def __init__(self, content):
		self.content = content
		self.filename = 'temp' + str(TemporaryFile.n_temp_files) + '.txt'
		TemporaryFile.n_temp_files += 1

	def __enter__(self):
		self.file = open(self.filename, 'w')
		self.file.write(self.content)
		self.file.close()
		return self.filename

	def __exit__(self, exc_type, exc_value, exc_traceback): 
		os.remove(self.filename)

def green_text(text):
	return "\u001b[32m" + text + "\033[0m" 

def red_text(text):
	return "\u001b[31m" + text + "\033[0m" 


def quote_path(path):
	already_quoted = (path[0] == '\"' and path[-1] == '\"')
	if not already_quoted:
		return '\"' + path + '\"'
	else:
		return path