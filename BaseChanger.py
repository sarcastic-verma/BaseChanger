num = input("Enter the number ")
from_base = int(input("Enter the base "))
to_base = int(input("Enter the new base "))
hex_codes = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
             10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
splitter = num.split(".")
before_dec = 0
power = 0
num_int = splitter[0][::-1]
for i in num_int:
    if i in hex_codes:
        before_dec = before_dec + hex_codes[i] * (from_base ** power)
    else:
        i = int(i)
        before_dec = before_dec + i * (from_base ** power)
    power += 1
inter = before_dec
if len(splitter) != 1:
    point = 0
    power = -1
    num_before_dec = splitter[1]
    for i in num_before_dec:
        if i in hex_codes:
            point = point + hex_codes[i] * (from_base ** power)
        else:
            i = int(i)
            point = point + i * (from_base ** power)
        power = power - 1
    inter = inter + point
ans = 0
before_dec = []
after_dec = []
if to_base == 10:
    print(inter)
else:
    inter = str(inter)
    split_inter = inter.split(".")
    inter = int(split_inter[0])
    while inter >= to_base:
        rem = inter % to_base
        inter = inter // to_base
        if rem in hex_codes:
            before_dec.append(hex_codes[rem])
        else:
            before_dec.append(rem)
    if inter in hex_codes:
        before_dec.append(hex_codes[inter])
    else:
        before_dec.append(inter)
    before_dec = before_dec[::-1]
    ans = "".join([str(i) for i in before_dec])
    if len(splitter) != 1:  # debug for binary,hex base
        len_dec = len(split_inter[1])
        inter_dec = int(split_inter[1])
        for i in range(5):
            multiply_inter_dec = str(inter_dec * to_base)
            len_inter_dec = len(multiply_inter_dec)
            if len_inter_dec > len_dec:
                appender = multiply_inter_dec[:len_inter_dec - len_dec] + "." + multiply_inter_dec[
                                                                                len_inter_dec - len_dec:]
            else:
                appender = "0." + multiply_inter_dec
            append_splitter = appender.split(".")
            hex_check = int(append_splitter[0])
            if hex_check in hex_codes:
                after_dec.append(hex_codes[hex_check])
            else:
                after_dec.append(append_splitter[0])
            inter_dec = int(append_splitter[1])
        after_dec = "".join([str(i) for i in after_dec])
        ans = ans + "." + after_dec
    print(ans)
