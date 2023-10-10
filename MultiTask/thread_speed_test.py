import time
import threading


class CountDownClock(threading.Thread):
    def __init__(self, time_left):
        super().__init__()
        self.time_left = time_left

    def count_down(self):
        while self.time_left:
            time.sleep(1)
            self.time_left -= 1
            print("还剩%s秒" % self.time_left)
        print("时间到")

    def run(self):
        self.count_down()


class ThreadAdd(threading.Thread):
    thread_add_number = 0

    def __init__(self):
        super().__init__()
        self.result = 0
        ThreadAdd.thread_add_number += 1

    def add(self):
        while count_down_clock.time_left:
            self.result += 1
        print("%s:%s" % (self.name, self.result))

    def run(self):
        self.add()

    @classmethod
    def add_all(cls):
        # todo
        print(cls.thread_add_number)


if __name__ == "__main__":
    result_main_process = 0

    count_down_clock = CountDownClock(5)
    count_down_clock.start()

    thread_add_1 = ThreadAdd()
    thread_add_2 = ThreadAdd()
    thread_add_3 = ThreadAdd()

    thread_add_1.start()
    thread_add_2.start()
    thread_add_3.start()

    ThreadAdd.add_all()

    while count_down_clock.time_left:
        result_main_process += 1

    print("result_main_process:", result_main_process)
