inp = int(input("Enter a number: "));
dividor = 2;
factors = [];
while dividor <= inp//2:
    while inp % dividor == 0:
        factors.append(dividor);
        inp /= dividor;
    dividor += 1;
print(factors);
