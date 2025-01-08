startingVal = int(input(""))
step_it = 0
while startingVal != 1:
    if startingVal%2==0:
        startingVal = startingVal / 2
        step_it+=1
        print(int(startingVal))
    else:
        startingVal = 3*startingVal+1
        step_it+=1
        print(int(startingVal))
print(f"steps:{step_it}")