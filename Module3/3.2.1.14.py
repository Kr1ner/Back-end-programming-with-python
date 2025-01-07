blocks = int(input("Enter the number of blocks: "))

iterator = 1
height = 1
while iterator+1<blocks:
    height+=1
    iterator+=1
    blocks-=iterator

print("The height of the pyramid:", height)
