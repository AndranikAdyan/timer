from functions import *
import time

user_input = input("Insert time to count down (h:m:s) ")

if checker(user_input):
	times = {}
	times["hour"], times["minute"], times["second"] = user_input.split(":")

	while True:
		print_time(times)
		if int(times["minute"]) == 0 and int(times["second"]) == 0:
			times["hour"] = str(int(times["hour"]) - 1)
			times["minute"] = "60"

		if int(times["second"]) == 0 and int(times["minute"]) != 0:
			times["minute"] = str(int(times["minute"]) - 1)
			times["second"] = "60"

		times["second"] = str(int(times["second"]) - 1)
		time.sleep(1)

		if all(int(times[i]) == 0 for i in times):	
			print_time(times)
			break
	print("Time is up!!!")
else:
    print("Bad Input!")