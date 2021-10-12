from art import *
from datetime import datetime
import cmd, sys
import config

class gameitShell(cmd.Cmd):
	prompt = "$ "
	log = {"practice": [], "battle": [], "satisfaction": []}
	tasks = ["gameit 5m",
		"Leetcode: tag1 * 4 2h", 
		"Leetcode: tag2 * 4 1h40m", 
		"Leetcode: graph * 5 2h30m", 
		"Python: Class 30m",
		"BQ: 3 30m",
		"Simulation: ms 30m"] 
	
	durations = [''] * len(tasks)
	crossed = set()
	
	time = None

	def do_tasks(self, arg):
		self.print_tasks()
		self.time = datetime.now()

	def print_tasks(self):
		for i in range(len(self.tasks)):
                        if i in self.crossed:
                                print( u"\u25A0"+ " " +self.tasks[i])
                        else:
                                print( u"\u25A1"+ " " +self.tasks[i])
	
	def do_fin(self, arg):
		print("\n****Hooray!!!!****\n")
		
		now = datetime.now()
		duration = now - self.time
		duration_in_s = duration.total_seconds()
		hours = divmod(duration_in_s, 3600) 
		minutes = divmod(hours[1], 60)
		self.time = now		
		
		taskid = int(arg)
		formatted_duration = ""
		if int(hours[0]) > 0:
			formatted_duration += str(int(hours[0])) + "h "
		if int(minutes[0]) > 0:
			formatted_duration += str(int(minutes[0])) + "m "
		if int(minutes[1]) > 0 :
			formatted_duration += str(int(minutes[1])) + "s" 
		self.durations[taskid] = formatted_duration

		print("【" + self.tasks[taskid] + "】" + " Mission completed in 【" + formatted_duration + "】\n") 
		self.tasks[taskid] += config.bcolors.OKYELLOW + " - finished in " + self.durations[taskid] + config.bcolors.OKGREEN
		self.crossed.add(taskid)
		self.print_tasks()
		print("\n")
		
		if len(self.crossed) == len(self.tasks):
			print("You're killing it!!! Now have a rest soldier :)")
			config.save(self.tasks)
			return True
 
	def do_bye(self, arg):
		print('See you next round:)')
		# save data
		#for i in range(len(self.tasks)):
		#	self.tasks[i] += " " + self.durations[i]
		config.save(self.tasks)
		return True

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
	# generate artsy title
	title = text2art("GAMEIT", "rnd-large")

	# print colored title
	CEND = '\033[0m'
	title += CEND
	print(config.bcolors.OKGREEN + "======================================================\n\n")
	print(config.bcolors.OKGREEN + title)

	# read info from file
	username = "sigkilll"

	# print current info
	print(config.bcolors.OKGREEN + "============== WELCOME, PLAYER " + username + " ==============")

	
	gameitShell().cmdloop()

