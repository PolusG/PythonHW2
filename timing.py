from time import *
#function to gerate execution time
def calculate_time(func):
    def time_rn():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time-start_time
        print(f"EXACTLY  {execution_time} second")
    return time_rn
