inp = int(input("How many prime numbers do you want listed: "));
primes = [2];
number = 3;
while len(primes) < inp:
    for p in primes:
        if number % p == 0:
            break;
    else:
        primes.append(number);
    number += 1;
    continue;
print(primes);
