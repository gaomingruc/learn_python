import time

def print_hello(hello_times):
    def print_hello_inner(func):
        def plus_hello(n):
            result = func(n)
            for i in range(hello_times):
                print("hello world")
            return result
        return plus_hello
    return print_hello_inner


def report_time(func):
    def sum_square_plus_report_time(n):
        time_start = time.time()
        result = func(n)
        time_end = time.time()
        print("耗时%.2f秒" % (time_end - time_start))
        return result
    return sum_square_plus_report_time


@print_hello(10)
@report_time
def sum_square(n):
    generator_n = (i for i in range(n))
    result = 0
    for i in generator_n:
        print(i)
        result += i
    return result


if __name__ == "__main__":
    print("result:", sum_square(1000000))
