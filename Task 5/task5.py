sum1:int = 0
count1:int = 1
iq:int = int(input("please enter the iq: "))
while iq >= 30 and iq <= 300:
    sum1 = sum1 + iq
    count1 = count1 + 1
    iq: int = int(input("please enter the iq: "))
avg1:float = (sum1+iq)/count1
print(f"the average is {avg1:.2f}")
print("one year of python training has been completed...")
sum2:int = 0
count2:int = 1
iq:int = int(input("please enter the iq: "))
while iq >= 30 and iq <= 300:
    sum2 = sum2 + iq
    count2 = count2 + 1
    iq: int = int(input("please enter the iq: "))
avg2:float = (sum2+iq)/count2
print(f"the average is {avg2:.2f}")
print(f"the average has grown by {avg2 - avg1:.2f}!" if avg2 > avg1 else f"the average has been decreased by {avg1 - avg2:.2f}!" if avg1 > avg2 else f"it remains the same average : {avg2:.2f}")