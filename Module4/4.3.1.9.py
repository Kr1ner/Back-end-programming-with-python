def is_prime(num):
    it = 2
    bool = True
    while it < num:
        if num%it==0:
            return False
        it+=1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
