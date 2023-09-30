# TASK 1 "stay alive"
numbers = [4, 8, 15, 16, 23, 42]
# here we use massive and create peremennaya
for number in numbers:
    print(number, end=" ")

# 2

for number in numbers:
    print(number)
# 3

    # num = int(input("Enter a number: "))
    # print(num, num + 1, num + 2)


#4
    # num1 = int(input("Enter the first integer: "))
    # num2 = int(input("Enter the second integer: "))
    # num3 = int(input("Enter the third integer: "))
    # sum = num1 + num2 + num3
    # print(sum)

    # 5



    abc = int(input("Enter the edge length of the cube: "))

    # volume of the cube
    volume = abc ** 3
    tsa = 6 * (abc ** 2)
    print("Volume =", int(volume))
    print("Total surface area =", int(tsa))

    # TASK 2
    #1
    qwe = int(input("Enter the number of schoolchildren: "))
    tangerines = int(input("Enter the number of tangerines: "))
    tang = tangerines // qwe
    remaind = tangerines % qwe
    print(tang)
    print(remaind)

    #2
    NUM = int(input("Enter a four-digit number: "))
    thousand = (NUM // 1000) % 10
    hundred = (NUM // 100) % 10
    ten = (NUM // 10) % 10
    unit = NUM % 10
    print("The digit in the thousands position is", thousand)
    print("The digit in the hundreds position is", hundred)
    print("The digit in the tens position is", ten)
    print("The digit in the units position is", unit)
    #3


    population = int(input("Enter the population of the universe: "))
    if population % 2 == 0:
        alive = population // 2
    else:
        alive = (population + 1) // 2
    print("Number of survivors:", alive)

    # 4
    NUM1 = int(input("Enter a number: "))
    Result = NUM1 << 1
    if Result == 0:
        print("The result of << is zero. Please enter a different number.")
    else:
        print("The result of << is", Result)

        # 5
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            operation = input("Please choose the operation (+, -, *, /): ")
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ZeroDivisionError("Division by zero is not allowed.")
            else:
                raise ValueError("Invalid operation entered.")

            print(f"{num1} {operation} {num2} = {result:.3f}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")