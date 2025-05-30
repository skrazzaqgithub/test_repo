# from calci import add, sub
#
# def main():
#     eng1 = 250
#     ind1 = 220
#     eng2 = 180
#     engtotal = add(eng1, eng2)
#     ind2 = sub(engtotal, ind1)
#     target = add(ind2, 1)
#     print("2nd innings for india target is:", target)
#
#
# if __name__ == "__main__":
#     main()
from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(8):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(8):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Bye")
# t1.start()
# t2.start()