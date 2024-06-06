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

def save_collatz_sequences(sequence, filename):
    with open(filename, 'a') as file:
        file.write(f"{', '.join(str(num) for num in sequence)}\n")

def remove_duplicates(filename):
    with open(filename, "r") as file:
        log_content = file.read()

    lines = log_content.split("\n")

    unique_lines = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            unique_lines.append(lines[i-1].strip())
            continue
        for j in range(i + 1, len(lines)):
            line2 = lines[j].strip()
            if not line2:
                continue
            if not set(line).issubset(line2):
                unique_lines.append(line)
                break

    with open(filename, "w") as file:
        file.write("\n".join(unique_lines))

def main():
    filename = "CollatzSequences.log"

    num = load_last_number(filename)

    while num < 50:
        num += 1
        sequence = collatz_sequence(num)
        save_collatz_sequences(sequence, filename)

    remove_duplicates(filename)

if __name__ == "__main__":
    main()