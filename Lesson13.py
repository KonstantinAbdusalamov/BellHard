from threading import Barrier, Thread
from time import sleep

bar = Barrier(3)
store = []

def f1(x):
    print('Part1')
    store.append(x**3)
    sleep(0.5)
    bar.wait()

def f2(x):
    print('Part2')
    store.append(x*3)
    sleep(1)
    bar.wait()


Thread(target=f1, args=(4,)).start()
Thread(target=f2, args=(12,)).start()

bar.wait()

print('Result:', sum(store))

#2

# import multiprocessing
# import os
#
#
# def do_this(what):
#     who_am_i(what)
#
# def who_am_i(what):
#     print(f"Process {os.getpid()} says: {what}")
#
#
# if __name__ == '__main__':
#     who_am_i("I'm the main program")
#     for n in range(4):
#         process = multiprocessing.Process(
#             target=do_this,
#             args=(f"I'm function {n}",)
#         )
#         process.start()
#3
import asyncio


async def main():
    await  asyncio.sleep(1.4)
    print('Hello ...')
    await  asyncio.sleep(1.4)
    print('...Peter')


asyncio.run(main())
