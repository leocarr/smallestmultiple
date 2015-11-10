# smallest multiple

found = False
smallest = 0 
current = 20
while found == False:
    div = 0
    for i in range(1,21):
        if current%i == 0:
            div += 1
    if div == 20:
        found = True
        smallest = current
    else:
      current += 20

print(smallest)
