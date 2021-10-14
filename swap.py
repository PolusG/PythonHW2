def swap_last_item(list):
	size = len(list)
	temp = list[0]
	list[0] = list[size-1]
	list[size-1] = temp

	return list
