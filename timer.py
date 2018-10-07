import time
class Timer:
    def __init__(self, loops_timed):
        self.start_time = time.time()
        self.loop_counter = 0
        self.loops_timed = loops_timed
    def run(self):
        self.loop_counter += 1
        if self.loop_counter == self.loops_timed:
            seconds = time.time() - self.start_time
            print("{} loops takes {} seconds".format(self.loops_timed, seconds))
            self.loop_counter = 0
            self.start_time = time.time()

timer = Timer(100)
for i in range(1000):
    [1 for j in range(100000)]
    timer.run()
