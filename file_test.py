"""
@author:Administrator
@file: argv.py
@time: 2019/01/{DAY}
"""


#!usr/bin/env python
#-*- coding:utf-8 _*-
import random
from time import *

num = 50000


remote_long = r"C:\Users\Administrator\Desktop\remote_long.txt"
remote_str = r"C:\Users\Administrator\Desktop\remote_str.txt"
def func():
    n = num
    counter = 1
    target = open(remote_long, 'w')
    print("Opening the file...")
    while counter <= n:
        counter += 1
        date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
        time1 = mktime(date1)
        date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
        time2 = mktime(date2)
        temp = random.randint(time1, time2)
        random_time = str(temp)
        target.write(random_time)
        target.write("\n")
    target.close()
pass


def func2():
    abc = random.sample('zyxwvutsrqponmlkjihgfedcba', 10)
    ff = "".join(abc)
    print(ff)
    pass


def func1():
    n = num
    counter = 1
    target = open(remote_str, 'w')
    print("Opening the file...")
    while counter <= n:
        counter += 1
        abc = random.sample('zyxwvutsrqponmlkjihgfedcba', 10)
        ff = "".join(abc)
        target.write(ff)
        target.write("\n")
    target.close()
    pass

class Main():
    def __init__(self):
       func1();
       func();


if __name__ == "__main__":
    Main();




