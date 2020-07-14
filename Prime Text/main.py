maxNum = 1000000
f = open("primes.txt","a")
open('primes.txt', 'w').close();
primes = [];
for n in range(2,maxNum+1):
    for p in primes:
        if n % p == 0:
            break;
    else:
        primes.append(n);
        f.write(str(n)+'\n');
f.close();
print("Done!");
