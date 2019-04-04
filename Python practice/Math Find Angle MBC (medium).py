import math
AB = float(input()) 
BC = float(input())
AC = math.sqrt(AB**2 + BC**2)
MC = AC / 2
BM = math.sqrt(BC**2 + MC**2 - 2 * MC * (BC**2)/AC)
numerator = BC**2 + BM**2 - MC**2
denominator = 2 * BC * BM
teta = round(math.acos(numerator/denominator) * 180 / math.pi)
print ("%s" % teta, chr(176), sep='')
