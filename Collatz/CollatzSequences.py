import signal
stop_requested = False

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def update_log_file(log_file, sequence):
    with open(log_file, 'a') as file:
        file.write(','.join(map(str, sequence)) + '\n')

def signal_handler(signum, frame, log_file):
    print("\nInterrupt received, stopping...")
    update_log_file(log_file, sequence)
    global stop_requested
    stop_requested = True

def find_special_collatz_numbers(log_file="CollatzSequences.log"):
    global stop_requested
    stop_requested = False

    signal.signal(signal.SIGINT, lambda s, f: signal_handler(s, f, log_file))

    with open(log_file, 'r') as file:
        lines = file.readlines()
        if lines:
            n_str = ','.join(lines[-1].strip().split(',')[:-1])
            n = int(n_str)
        else:
            n = 1
        print(f"Continuing from {n}")

    sequence = collatz_sequence(n)

    while not stop_requested:
        update_log_file(log_file, sequence)
        print(','.join(map(str, sequence)))
        sequence = collatz_sequence(sequence[-1])

    update_log_file(log_file, sequence)
    print(f"Finished at {sequence[0],}")

find_special_collatz_numbers()