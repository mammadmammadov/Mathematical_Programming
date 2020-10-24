#This program finds the product of two binary numbers
def convertToDecimal(number):
    numberInString=str(number)
    reversedNumberInString=numberInString[::-1]
    valueInDecimal=0
    lengthOfNumberInString=len(numberInString)
    for digit in range(lengthOfNumberInString):
        valueInDecimal =valueInDecimal+int(reversedNumberInString[digit])*2**digit
    return valueInDecimal
def convertToBinary(number):
    valueInBinary=""
    while number>=1:
        valueInBinary=valueInBinary+str(number%2)
        number=number//2
        if number==1:
            valueInBinary=valueInBinary+"1"
            break
    return valueInBinary[::-1]
number1=int(input("Input the first number: "))
number2=int(input("Input the second number: "))
print(f"Multiply of these numbers")


