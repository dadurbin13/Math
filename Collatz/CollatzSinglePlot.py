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

def plot_collatz(n):
    sequence = collatz_sequence(n)
    sequence_length = len(sequence)
    sequence_max = max(sequence)
    
    plt.figure(figsize=(10,6))
    plt.plot(sequence, label=f'Collatz Sequence (n={n})', marker='o')
    plt.title(f'Collatz Sequence for n = {n}\nMax Value: {sequence_max}, Length: {sequence_length}')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example number
n = 319804831
plot_collatz(n)
