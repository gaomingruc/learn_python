import time
import threading



class Dog(object):
    def __init__(self, name):
        self.name = name

    def run(self, n):
        print("小狗-%s-在跑，跑了%s圈" % (self.name, n))
        time.sleep(1)

    def bark(self, n, content):
        print("小狗-%s-在狂吠，叫了%s下，内容是%s" % (self.name, n, content))
        time.sleep(1)


if __name__ == "__main__":
    dog = Dog("小黄")

    # for i in range(5):
    #     dog.run()
    #     dog.bark()
    #     time.sleep(1)
    #     print("-" * 10)

    for i in range(5):
        thread_run = threading.Thread(target=dog.run, args=(5,))
        thread_bark = threading.Thread(target=dog.bark, args=(3, ), kwargs={"content":"hello"})
        thread_run.start()
        thread_bark.start()
        time.sleep(1)
        print("-" * 10)