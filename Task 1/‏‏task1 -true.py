# סעיף 1 ערך אמת: a=1 b=1
a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

# סעיף 2 ערך אמת: a=1 b=1 c=1 d=1
a = 1
b = 1
c = 1
d = 1
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")


#סעיף 3 ערך אמת: a=2 b=1 c=1 d=1
a = 2
b = 1
c = 1
d = 1
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")


#סעיף 4 ערך אמת: a=2 b=1 c=1 d=1
a = 2
b = 1
c = 1
d = 1
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")


#סעיף 5 ערך אמת: a=1 b=1 c=2 d=3
a = 1
b = 1
c = 2
d = 3
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")


#סעיף 6 ערך אמת: a=1 b=1 c=1 d=1
a = 1
b = 1
c = 1
d = 1
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")


#סעיף 7 ערך אמת: a=1 b=2
a = 1
b = 2
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")


#סעיף 8 ערך אמת: a=1 b=2 c=3
a = 1
b = 2
c = 3
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")


#סעיף 9 ערך אמת: a=1 b=2 c=3
a = 1
b = 2
c = 3
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")


#סעיף 10 ערך אמת: a=2 b=2 c=3 d=2
a = 2
b = 2
c = 3
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")