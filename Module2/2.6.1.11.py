hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
print(f"{(hour+round(dura/60))%24}:{(mins+dura%60)%60}")