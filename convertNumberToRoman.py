def convertNumberToRoman(num):
    if not 0 < num < 1001:
        return "Number Invalid."
    arabicNumber = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    romanNumber = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    indexNumber = 0
    while num > 0:
        for _ in range(num // arabicNumber[indexNumber]):
            result += romanNumber[indexNumber]
            num -= arabicNumber[indexNumber]
        indexNumber += 1

    return result

print(convertNumberToRoman(234))