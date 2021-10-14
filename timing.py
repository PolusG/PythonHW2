import time
#function to gerate execution time
def calculate_time(func):
    def time_rn():
        start_time = time.time()
        time.sleep(2)
        end_time = time.time()
        execution_time = end_time-start_time
        print(f'Total time {execution_time}')
    return time_rn
