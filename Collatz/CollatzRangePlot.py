import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_special_collatz_sequences(start, end):
    longest_sequence = None
    highest_max_sequence = None
    longest_length = 0
    highest_max = 0

    for n in range(start, end + 1):
        sequence = collatz_sequence(n)
        sequence_length = len(sequence)
        sequence_max = max(sequence)

        # Print the current integer and its Collatz sequence
        print(f"{', '.join(map(str, sequence))}")

        if sequence_length > longest_length:
            longest_length = sequence_length
            longest_sequence = (n, sequence)

        if sequence_max > highest_max:
            highest_max = sequence_max
            highest_max_sequence = (n, sequence)

    plt.figure(figsize=(10,6))
    
    if longest_sequence:
        plt.plot(longest_sequence[1], label=f'Longest (n={longest_sequence[0]}) - Length: {longest_length}', marker='o')
    
    if highest_max_sequence and highest_max_sequence[0] != longest_sequence[0]:
        plt.plot(highest_max_sequence[1], label=f'Highest Max (n={highest_max_sequence[0]}) - Max Value: {highest_max}', marker='o')

    plt.title(f'Special Collatz Sequences in Range {start} to {end}')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    plt.legend()
    plt.show()

# Parameters
start = 2
end = 10000
plot_special_collatz_sequences(start, end)
