def swap_last_item(list):
	'''sets first element = to temp and sets first element = to last
	element and sets last item = to temp'''
	size = len(list)
	temp = list[0]
	list[0] = list[size-1]
	list[size-1] = temp
	#return the new list
	return list
