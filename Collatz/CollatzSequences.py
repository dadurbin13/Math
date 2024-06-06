from datetime import datetime

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def load_last_number(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip().split(', ')[0]
            return int(last_line)
        return 0

def main():
    filename = "CollatzSequences.log"

    num = load_last_number(filename)

    while True:
        with open(filename, 'a') as file:
            for i in range(10000):
                num += 1
                sequence = collatz_sequence(num)
                file.write(f"{', '.join(str(number) for number in sequence)}\n")

        print(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {sequence}")

if __name__ == "__main__":
    main()