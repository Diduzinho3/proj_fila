from colorama import Fore
import os
from time import sleep

queue = []
treated = []
finish = False

def split():
    print("--------------------------")
    sleep(0.3)

def new_person():
    os.system("cls")
    new = input("New person to join on queue:\n")
    split()
    queue.append(new)

def queue_list():
    sleep(0.3)
    print("Actual queue:")
    for i in range(len(queue)):
        print(Fore.GREEN + f"{i+1}°: {queue[i]}" + Fore.WHITE)
    split()

def run_again():
    while True:
        run = input("Do you wanna add more? (Y/N)\n").upper()
        if run == "N":
            os.system("cls")
            print(Fore.RED + "Finishing Program!" + Fore.WHITE)
            split()
            return False
        elif run == "Y":
            return True
        else:
            print("Write 'Y' or 'N'")
            sleep(0.3)

def finished():
    global finish
    print("State of queue:")
    if not finish:
        print(Fore.YELLOW + f"{queue[0]} is next in line" + Fore.WHITE)
        split()
        queue_list()
        finish = True
    elif finish:
        print(Fore.RED + f"{queue[0]} left the queue." + Fore.WHITE)
        split()
        treated.append(queue.pop(0))
        queue_list()
        finish = False

def clearing_queue():
    sleep(0.3)
    print(Fore.RED + f"{queue[0]} left the queue." + Fore.WHITE)
    treated.append(queue.pop(0))
    split()
    sleep(0.3)

def end_program():
    while len(queue) > 0:
        clearing_queue()

def treated_patients():
    print("Treated patients:")
    for i in range(len(treated)):
        print(Fore.GREEN + f"{i+1}°: {treated[i]}" + Fore.WHITE)
    split()
    print(Fore.BLUE + "Queue has finished!")

def program():
    while True:
        new_person()
        finished()
        if not run_again():
            break
    os.system("cls")
