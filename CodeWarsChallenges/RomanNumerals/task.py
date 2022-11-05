ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}
    
class RomanNumerals:
    
    def to_roman(val):
        s = ''
        for key, value in ROMANS.items():
            while val % value != val:
                val -= value
                s += key
        return s
    
    def from_roman(roman_num):
        s = 0
        for key, value in ROMANS.items():
            while roman_num.startswith(key):
                roman_num = roman_num[len(key):]
                s += value
        return s

def test(fun, x):
    return fun == x


print(test(RomanNumerals.to_roman(1000), 'M'))
print(test(RomanNumerals.to_roman(4), 'IV'))
print(test(RomanNumerals.to_roman(1), 'I'))
print(test(RomanNumerals.to_roman(1990), 'MCMXC'))
print(test(RomanNumerals.to_roman(2008), 'MMVIII'))

print(test(RomanNumerals.from_roman('XXI'), 21))
print(test(RomanNumerals.from_roman('I'), 1))
print(test(RomanNumerals.from_roman('IV'), 4))
print(test(RomanNumerals.from_roman('MMVIII'), 2008))
print(test(RomanNumerals.from_roman('MDCLXVI'), 1666))