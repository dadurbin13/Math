import signal
from datetime import datetime

filename = "PrimeProgress.log"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def load_last_number():
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip().split('- ')[-1]
            return int(last_line)
        return 0

def signal_handler(sig, frame):
    global max_prime
    with open(filename, "w") as file:
        file.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {max_prime}")
        print(f"\n{datetime.now():%Y-%m-%d %H:%M:%S} - {max_prime:,}")
    print("Exiting...")
    exit(0)

def main():
    global max_prime

    num = load_last_number()
    max_prime = num

    while True:
        num += 1
        if is_prime(num):
            max_prime = num
        
        if num % 1000000 == 0:
            print(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {max_prime:,}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()