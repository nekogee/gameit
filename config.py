import json
from datetime import datetime

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	OKYELLOW = '\033[93m'
	OKRED = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	CEND = '\033[0m'

filename = "log.txt"
def loadinfo():
	myfile = open(filename,"a+")
	myfile.close()

def save(log):
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S") + "\n\n"
	myfile = open(filename,"a+")
	myfile.write(date_time)
	myfile.write(json.dumps(log)+"\n\n\n")
	myfile.close()

