
# Queue and threads in Python 
# https://www.youtube.com/watch?v=NwH0HvMI4EA

# Import Queue module
from queue import Queue
# Import threading modules
import threading

# Import time module for using stop watch
import time



# Setup Threading queue 
print_lock = threading.Lock()
# Assign queue funtion to q
q = Queue()


# This function is where the actual task is done
# Function definition
def exampleJob(worker):
    # This is a dummy task that could be a useful item
    print("Exampe Job function")
    time.sleep(0.5)
    # this shows the threads in action for learning 
    with print_lock:
        # Prints the actual threds
        print(threading.current_thread().name, worker)

# This is where we put jobs into the queu
def threader():
    # Loops while there is something in the queue
    while True:
        # This "pops" a jon off the queue.
        # This could be the job board.
        worker = q.get()
        # Call the worker function with the job to be done
        exampleJob(worker)
        # When the work is done the thread is closed
        q.task_done()


# This is the factory manager dishing out the work.
# We'll have 10 workers
for x in range(10):
    # Adds the threads 
    t = threading.Thread(target = threader)
 
    # Sets the thread to run in the background 
    t.daemon = True
    # This starts the work day
    t.start()
# Starts the stop workday
start = time.time()

# This is the numner of tasks to perform
for worker in range(20):
    # Add a job to the work queue
    q.put(worker)

q.join()

print(f"Entire job took", time.time() - start )

