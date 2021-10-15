def tripler(func):
    ''' this function calls the function within three times'''
    func()
    func()
    func()
def three_times():
    '''this function prints a statement'''
    print("print this statement three times")
'''call three_times function 3 times using tripler function'''
three_times = tripler(three_times)
