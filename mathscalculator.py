# noinspection PyUnreachableCode
def get_number(number):
while True:
    # noinspection PyUnreachableCode
operand1 = input("Number" + str(number) + ":")
    try:
        return float(operand1)
    except:
        print("Invalid input")
operand1 = get_number(1)
operand2 = get_number(2)
sign = input("Type any mathematical operation sign: ")

result = 0
if sign == "+":
    result = operand1 + operand2
elif sign == "-":
    result = operand1 - operand2
elif sign == "/":
    result = operand1 / operand2
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Division by zero")
elif sign == (*):
    result = operand1 * operand2
else:
    print("Invalid sign")

print(result)





