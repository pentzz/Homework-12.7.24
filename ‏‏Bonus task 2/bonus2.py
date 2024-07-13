sum1:int = 0
count1:int = 1
iq:int = int(input("please enter the iq: "))
max1:int = iq
min1:int = iq
while iq >= 30 and iq <= 300:
    sum1 = sum1 + iq
    count1 = count1 + 1
    iq: int = int(input("please enter the iq: "))
    if iq > max1:
        max1 = iq
    if iq < min1:
        min1 = iq
avg1:float = (sum1+iq)/count1
print(f"the average is {avg1:.2f}\nthe highest iq of group 1 is: {max1}\nthe lowest iq of group 1 is: {min1}")
print("one year of python training has been completed...")
sum2:int = 0
count2:int = 1
iq:int = int(input("please enter the iq: "))
max2:int = iq
min2:int = iq
while iq >= 30 and iq <= 300:
    sum2 = sum2 + iq
    count2 = count2 + 1
    iq: int = int(input("please enter the iq: "))
    if iq > max2:
        max2 = iq
    if iq < min2:
        min2 = iq
avg2:float = (sum2+iq)/count2
print(f"the average is {avg2:.2f}\nthe highest iq of group 2 is: {max2}\nthe lowest iq of group 2 is: {min2}")
print(f"the average has grown by {avg2 - avg1:.2f}!" if avg2 > avg1 else f"the average has been decreased by {avg1 - avg2:.2f}!" if avg1 > avg2 else f"it remains the same average : {avg2:.2f}")
print(f"\n{max1} of group 1 is the highest between the two groups." if max1 > max2 else f"\n{max2} of group 2 is the highest between the two groups." if max2 > max1 else f"\nthere is a tie for the highest iq for the 2 groups :{max1}.")
print(f"{min1} of group 1 is the lowest between the two groups." if min1 < min2 else f"{min2} of group 2 is the lowest between the two groups." if min2 < min1 else f"there is a tie for the lowest iq for the 2 groups :{min1}.")