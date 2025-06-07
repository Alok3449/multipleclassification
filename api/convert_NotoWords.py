
def zeroToNine(n):
    digits = ["Zero", "One", "Two", "Three", "Four",
              "Five", "Six", "Seven", "Eight", "Nine"]
    return digits[n]


def elevenToNineteen(n):
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return teens[n-11]


def tens(n):
    tens_Power = ["Ten", "Twenty", "Thirty", "Forty",
                  "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    return tens_Power[(n//10)-1]


def zeroToHundred(n):
    if n < 10:
        return zeroToNine(n)
    if n >= 11 and n <= 19:
        return elevenToNineteen(n)
    if n % 10 == 0:
        return tens(n)
    digit = n % 10
    t = n-digit
    return f"{tens(t)} {zeroToNine(digit)}"


for i in range(0, 100):
    print(zeroToHundred(i), end=",")


def HundredTo999(n):
    if n<=99:
        return zeroToHundred(n)
    
    hundreds_place = n // 100
    rest = n % 100

    if rest == 0:
        return f"{zeroToNine(hundreds_place)} Hundred"
    else:
        return f"{zeroToNine(hundreds_place)} Hundred and {zeroToHundred(rest)}"





for i in range(0, 1000):
    print(HundredTo999(i), end=", ")
    