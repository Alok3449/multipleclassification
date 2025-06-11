def zeroToNine(n):
    digits = ["Zero", "One", "Two", "Three", "Four",
              "Five", "Six", "Seven", "Eight", "Nine"]
    return digits[n]


def elevenToNineteen(n):
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return teens[n - 11]


def tens(n):
    tens_power = ["Ten", "Twenty", "Thirty", "Forty",
                  "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    return tens_power[(n // 10) - 1]


def zeroToHundred(n):
    if n < 10:
        return zeroToNine(n)
    elif 10 < n < 20:
        return elevenToNineteen(n)
    elif n == 10:
        return "Ten"
    elif n % 10 == 0:
        return tens(n)
    else:
        return f"{tens(n)} {zeroToNine(n % 10)}"


def hundredTo999(n):
    if n <= 99:
        return zeroToHundred(n)

    hundreds_place = n // 100
    rest = n % 100

    if rest == 0:
        return f"{zeroToNine(hundreds_place)} Hundred"
    else:
        return f"{zeroToNine(hundreds_place)} Hundred and {zeroToHundred(rest)}"


def thousandTo99999(n):
    if n <= 999:
        return hundredTo999(n)

    thousands_place = n // 1000
    rest = n % 1000

    prefix = zeroToHundred(thousands_place)
    if rest == 0:
        return f"{prefix} Thousand"
    else:
        return f"{prefix} Thousand {hundredTo999(rest)}"


def lakhTo10Lakh(n):
    if n < 100000:
        return thousandTo99999(n)

    lakhs_place = n // 100000
    rest = n % 100000

    prefix = zeroToHundred(lakhs_place)
    if rest == 0:
        return f"{prefix} Lakh"
    else:
        return f"{prefix} Lakh {thousandTo99999(rest)}"

for i in range(0, 1000001):
    print(lakhTo10Lakh(i),end=",")
