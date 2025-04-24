def main():
    
    num1 = input("\033[1;3;34mEnter your first number: \033[0m")
    num1 = int(num1)

    num2 = input("Enter your second number:")
    num2 = int(num2)

    total_sum = num1 + num2

    print(f"The sum of the two numbers is: {total_sum}")

if __name__ == "__main__":
    main()    