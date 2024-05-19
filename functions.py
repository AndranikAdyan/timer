def checker(user_input: str) -> bool:
	for char in user_input:
		if not char.isdigit() and char != ":":
			return False

	times = {}
	if ':' in user_input:
		times["hour"], times["minute"], times["second"] = user_input.split(":")
	else:
		print("Invalid time format. Please enter the time in h:m:s format.")
		return False

	if int(times["second"]) > 60 or int(times["minute"]) > 60:
		print("Invalid time entry: 'seconds' or 'minutes' should not exceed 60.")
		return False

	if len(times["second"]) > 2 or len(times["minute"] > 2):
		print("The number of digits in 'seconds' or 'minutes' should not exceed 2.")
		return False

	return True

def print_time(times):
    print(f"{times['hour'].zfill(2)}:{times['minute'].zfill(2)}:{times['second'].zfill(2)}")