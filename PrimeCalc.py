import itertools as it

def erat2a():
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D:
                x += 2*p
            D[x] = p

def log_primes():
    with open("Primes.log", "w") as f:
        f.write("Prime numbers:\n")
        start_time = time.time()
        prime_generator = erat2a()
        for i, prime in enumerate(prime_generator):
            print(f"Prime {i + 1}: {prime}")
            f.write(f"{i + 1}: {prime}\n")
            if i % 1000 == 0:
                print(f"Found {i + 1} primes in {time.time() - start_time:.2f} seconds")

log_primes()