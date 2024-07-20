def main():
    while True:
        num1, num2 = get_numbers()
        operation = get_operation()
        
        if operation == '1':
            result = add(num1, num2)
            print(f"The result of adding {num1} and {num2} is {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of subtracting {num2} from {num1} is {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of multiplying {num1} and {num2} is {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of dividing {num1} by {num2} is {result}")
        
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
