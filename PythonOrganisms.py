


## Increase in organisms by day and percentage



amount = int(input("Starting organisms: "))
percentage = int(input("Average daily percent increase: "))
time_to_repeat= int(input("Number of days: "))
print()
print()
print('Day Approximate', '      Population')
for time_to_repeat in range(1,time_to_repeat + 1,1):
    print(time_to_repeat - 1, '                   ',amount)
    amount = amount * (1 + percentage/100)
    

print()
print("this program was written by a confused evan gohary")
