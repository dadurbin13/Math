def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def save_collatz_sequences(sequence, filename):
    with open(filename, 'a') as file:
        file.write(f"{', '.join(str(num) for num in sequence)}\n")

sequences = []
num = 1
while num < 11:
    sequence = collatz_sequence(num)
    save_collatz_sequences(sequence, 'CollatzSequences.log')
    print(f"{sequence}")
    num += 1