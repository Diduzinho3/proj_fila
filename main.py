# Create code that simulate a queue, using the concept of FIFO.

from colorama import Fore
import os
from time import sleep

queue = []
finish = False

def queue_list():
    sleep(0.3)
    print("Actual queue:")
    for i in range(len(queue)):
        sleep(0.3)
        print(Fore.GREEN + f"{i+1}°: {queue[i]}" + Fore.WHITE)

def split():
    print("--------------------------")
    sleep(0.3)

def run_again():
    while True:
        run = input("Do you wanna add more? (Y/N)\n").upper()
        if run == "N":
            sleep(0.3)
            print(Fore.RED + "Finishing Program!" + Fore.WHITE)
            os.system("cls")
            print(Fore.RED + "Finishing Program!" + Fore.WHITE)
            sleep(0.3)
            split()
            return False
        elif run == "Y":
            return True
        else:
            print("Write 'Y' or 'N'")

def new_person():
    new = input("New person to join on queue:\n")
    queue.append(new)

def finished():
    global finish
    print("State of queue:")
    sleep(0.3)
    if not finish:
        print(Fore.YELLOW + f"{queue[0]} is next in line" + Fore.WHITE)
        sleep(0.3)
        finish = True
    elif finish:
        print(Fore.RED + f"{queue[0]} left the queue." + Fore.WHITE)
        sleep(0.3)
        del queue[0]
        finish = False

def clearing_queue():
    sleep(0.3)
    print(Fore.RED + f"{queue[0]} left the queue." + Fore.WHITE)
    del queue[0]
    sleep(0.3)

while True:
    new_person()
    split()
    queue_list()
    split()
    finished()
    split()
    if not run_again():
        break
    split()
    os.system("cls")

while len(queue) > 0:
    queue_list()
    clearing_queue()
    split()

print("Queue has finished!")