startp:int = int(input("please enter the start point: "))
endp:int = int(input("please enter the end point: "))
gap:int = int(input("please enter the gap: "))
for num in range(startp, endp + 1, gap):
    print(num)