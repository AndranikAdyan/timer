def checker(user_input: str) -> bool:
	for char in user_input:
		if not char.isdigit() and char != ":":
			return False

	times = {}
	if ':' in user_input:
		times["hour"], times["minute"], times["second"] = user_input.split(":")
	else:
		return False

	if int(times["second"]) > 60 or int(times["minute"]) > 60:
		return False

	return True

def print_time(times):
    print(f"{times['hour'].zfill(2)}:{times['minute'].zfill(2)}:{times['second'].zfill(2)}")