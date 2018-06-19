import time


class RunTime:

    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        end = time.time()

        m, s = divmod(end - self.start_time, 60)
        h, m = divmod(m, 60)
        print('用时： %dh, %dm, %ds' % (h, m, s))


runtime = RunTime()
