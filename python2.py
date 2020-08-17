def is_divisible_by_3(number):
	my_bool = True
	if sum(map(int, str(number))) % 3 != 0:
		my_bool = False
	return my_bool