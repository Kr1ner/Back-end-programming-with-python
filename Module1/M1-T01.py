print("using for loop")
for i in range(1,11):
    print(f"Hello World! {i}")

print("--------------------------")

print("using while loop")

iterator = 1
while iterator<=10:
    print(f"Hello World! {iterator}")
    iterator+=1;

print("--------------------------")
print("using recursion")

def count(a):
    if a<=10:
        print(f"Hello World! {a}")
        a+=1
        count(a)
count(1)