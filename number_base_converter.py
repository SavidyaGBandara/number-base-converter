# A simple number base converter that supports bases 2 to 10.

def converterA(numberA,baseA):
    #Converts a number string from the given base to decimal (base 10).
    decimal=0
    digits=[int(i) for i in numberA]
    power=len(digits)-1
    for x in digits:
        decimal=decimal + x*baseA**power
        power-=1
    return decimal

def converterB(numberB,baseB):
    #Converts a decimal (base 10) integer to a number string in the given base.
    remainder=""
    while numberB>0:    
        remainder = str(numberB%baseB) + remainder
        numberB = numberB//baseB
    return remainder

def validate(numberC,baseC):
    #Returns True if all digits in the number are valid for the given base, False otherwise.
    for k in numberC:
        if int(k) >= baseC:
            return False
    return True


inA=input("Enter the number to convert: ")
try:
    inB=int(input("Enter the base of the given number (e.g., 2, 8, 10): "))
    inC=int(input("Enter the base you want to convert to: "))
    if validate(inA,inB):
        print(converterB(converterA(inA,inB),inC))
    else:
        print("Error: Invalid number for the given base")
except ValueError:
    print("Please Enter a valid integer")

