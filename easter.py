# prompts user for a year and then provides the month and day easter is that year
#
# Written by: Victoria Knight
# Last Modified: 9/2/2025
##################################################################################

year = input("Please enter a year: ")

y = int(year)

a = y % 19

b = y // 100

c = y % 100

d = b // 4

e = b % 4

g = (8 * b + 13) // 25

h = (19 * a + b - d - g + 15) % 30

j = c // 4

k = c % 4

m = (a + 11 * h) // 319

r = (2 * e + 2 * j - k - h + m + 32) % 7

n = (h - m + r + 90) // 25

p = (h - m + r + n + 19) % 32

if n == 3:
    print(f"In the year {y}, Easter Sunday falls of March {p}")
else:
    print(f"In the year {y}, Easter Sunday falls of April {p}")
