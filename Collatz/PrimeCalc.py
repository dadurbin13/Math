# TODO: Refactor for prime numbers

import time
import signal

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def update_log_file(number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max, log_file):
    with open(log_file, 'w') as file:
        file.write(f"{number_with_longest_sequence},{longest_sequence_length}\n")
        file.write(f"{number_with_highest_max},{highest_max}\n")
        file.write(f"{n},{sequence_length},{sequence_max}\n")

def signal_handler(signum, frame, log_file, number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max):
    print("\nInterrupt received, stopping...")
    update_log_file(number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max, log_file)
    global stop_requested
    stop_requested = True

def find_special_collatz_numbers(minutes=None, log_file="CollatzProgress.log"):
    global stop_requested
    stop_requested = False
    start_time = time.time()

    signal.signal(signal.SIGINT, lambda s, f: signal_handler(s, f, log_file, number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max))

    # Read the current state from the log file
    with open(log_file, 'r') as file:
        lines = file.readlines()
        number_with_longest_sequence = int(lines[0].split(',')[0])
        longest_sequence_length = int(lines[0].split(',')[1])
        number_with_highest_max = int(lines[1].split(',')[0])
        highest_max = int(lines[1].split(',')[1])
        n = int(lines[2].split(',')[0])

    # Main calculation loop
    while (minutes is None or time.time() - start_time < minutes * 60) and not stop_requested:
        sequence = collatz_sequence(n)
        sequence_length = len(sequence)
        sequence_max = max(sequence)

        update_required = sequence_length > longest_sequence_length or sequence_max > highest_max or n % 100000 == 0

        if sequence_length > longest_sequence_length:
            longest_sequence_length = sequence_length
            number_with_longest_sequence = n

        if sequence_max > highest_max:
            highest_max = sequence_max
            number_with_highest_max = n

        if update_required:
            update_log_file(number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max, log_file)
            print(f"Processing Number: {n:,}; Sequence Max: {sequence_max:,}; Sequence Length: {sequence_length:,}")

        n += 1

    # Update the log file before exiting normally
    update_log_file(number_with_longest_sequence, longest_sequence_length, number_with_highest_max, highest_max, n, sequence_length, sequence_max, log_file)

    print(f"Finished at {n:,}")
    print(f"Number with the longest sequence: {number_with_longest_sequence:,} (Length: {longest_sequence_length:,})")
    print(f"Number with the highest max value: {number_with_highest_max:,} (Max Value: {highest_max:,})")

find_special_collatz_numbers()
