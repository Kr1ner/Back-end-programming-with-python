for i in range(1,11):
    for j in range(1,11):
        print(repr(i*j).rjust(3),end=" ",sep="")
    print("\n")