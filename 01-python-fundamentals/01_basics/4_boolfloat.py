import sys 
from fractions import Fraction
from decimal import Decimal     # for complex decimal calculation we use decimal

boy = True # first letter should be uppercase
are = False
a =1
b=3
c =0 
d = a + boy # upcasting
e = -4

iszero = a and b and c
print(f"is boy : {bool(boy)}")
print(f"{bool(iszero)}")
print(f"{d}")
print(f"{bool(e)}")

fl1 = 95.5
fl2 = 95.04334434542393029293943949095939032939409390293
print(f"{fl1 - fl2}")