class Variable():
    ONE     = "เอ็ด"
    UNIT    = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    TEN     = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ",]
    MILL    = ["ร้อย", "พัน", "หมื่น", "แสน", "ล้าน",]
    ERROR   = "ข้อมูลไม่ถูกต้อง"

def convertNumToTh(num):
    if type(num) != int or num < 0 or num > 10_000_000:
        return Variable.ERROR

    value = ""
    millions            = (num % 10_000_000) // 1_000_000
    hundred_thousands   = (num % 1_000_000) // 100_000
    ten_thousands       = (num % 100_000) // 10_000
    thousands           = (num % 10_000) // 1_000
    hundreds            = (num % 1_000) // 100
    tens                = (num % 100) // 10
    units               = (num % 10)

    if millions > 0:
        value += "{}{}".format(Variable.UNIT[millions], Variable.MILL[4])
    if hundred_thousands > 0:
        value += "{}{}".format(Variable.UNIT[hundred_thousands], Variable.MILL[3])
    if ten_thousands > 0:
        value += "{}{}".format(Variable.UNIT[ten_thousands], Variable.MILL[2])
    if thousands > 0:
        value += "{}{}".format(Variable.UNIT[thousands], Variable.MILL[1])
    if hundreds > 0:
        value += "{}{}".format(Variable.UNIT[hundreds], Variable.MILL[0])
    if tens > 0:
        value += "{}".format(Variable.TEN[tens])
    if units > 0:
        value += checkUnitOne(unit=units, ten=tens)
    return value

def checkUnitOne(unit, ten):
        if unit == 1 and ten > 0:
            return Variable.ONE
        else:
            return Variable.UNIT[unit]

print(convertNumToTh(3234678))