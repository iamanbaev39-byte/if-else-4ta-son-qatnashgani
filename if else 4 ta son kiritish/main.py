a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
d = int(input("4-sonni kiriting: "))

if a >= b:
    if c >= d:
        if a >= c:
            eng_katta = a
        else:
            eng_katta = c
    else:
        if a >= d:
            eng_katta = a
        else:
            eng_katta = d
else:
    if c >= d:
        if b >= c:
            eng_katta = b
        else:
            eng_katta = c
    else:
        if b >= d:
            eng_katta = b
        else:
            eng_katta = d

print("Eng katta son:", eng_katta)