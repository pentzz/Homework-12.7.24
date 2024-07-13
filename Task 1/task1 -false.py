
#סעיף 1 ערך שקר a=1 b=0

a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")


#סעיף 2 ערך שקר: a=0 b=0 c=0 d=0
a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



#סעיף 3 ערך שקר: a=1 b=2 c=3 d=4
a = 1
b = 2
c = 3
d = 4
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



#סעיף 4 ערך שקר: a=1 b=2 c=4 d=3
a = 1
b = 2
c = 4
d = 3
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



#סעיף 5 ערך שקר: a=1 b=2 c=3 d=4
a = 1
b = 2
c = 3
d = 4
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



#סעיף 6 ערך שקר: a=0 b=0 c=0 d=0
a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



#סעיף 7 ערך שקר: a=1 b=1
a = 1
b = 1
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")



#סעיף 8 ערך שקר: אין ערכים לביטוי כיוון שיש or true מה שמביא לאמת בכל הזנה
a = 3
b = 1
c = 4
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c} -allways true because of or true statment!")
else:
    print(f"was False for {a} {b} {c}")



#סעיף 9 ערך שקר:a=2 b=1 c=0
a = 2
b = 1
c = 0
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")



#סעיף 10 ערך שקר: a=4 b=3 c=4 d=4
a = 4
b = 3
c = 4
d = 4
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")