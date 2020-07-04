# Two Variables
Int_score = f'25_000_000.0'
Int = f'25000000'

print(Int_score)
print(Int)
print("Int_score: 25_000_000")
print("Int: 25000000")

#Value to e
number = 175000.0
formattednumber = format(number, "e")
print(formattednumber)

# Prompt User for base and exponent
number = int(input(" Please enter a base: "))
exponent = int(input(" Please enter an exponent: "))
power = 1
i = 1
while(i <= exponent):
    power = power * number
    i = i + 1
    
print("{0} to the power of {1} = {2}".format(number, exponent, power))