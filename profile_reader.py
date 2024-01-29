import re
import os

def read_lprun(name):
	data = []

	for file in os.scandir('./profiles/lp'):
		if name not in file.path:
			continue

		with open(file, 'r') as file:
			while not file.readline().startswith('='):
				pass

			file.readline()
			line = file.readline()

			temp = []
			while line:
				tokens = re.split(r'\s+', line)
				temp.append(float(tokens[3]))
				line = file.readline()

			data.append(temp)

	return data

def read_mprun(name):
	data = []

	for file in os.scandir('./profiles/mp'):
		if name not in file.path:
			continue

		with open(file, 'r') as file:
			while not file.readline().startswith('='):
				pass

			file.readline()
			file.readline()
			file.readline()
			line = file.readline()

			temp = []
			while line:
				tokens = re.split(r'\s+', line)

				if len(tokens) < 3:
					break

				temp.append(float(tokens[4]))
				line = file.readline()

			print('')
			data.append(temp)

	return data
