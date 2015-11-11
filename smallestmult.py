# smallest multiple

maxmult = 20
found = False
smallest = 0 
current = maxmult
while found == False:
    div = 0
    for i in range(1,maxmult+1):
        if current%i == 0:
            div += 1
    if div == maxmult:
        found = True
        smallest = current
    else:
        current += maxmult

print(smallest)

