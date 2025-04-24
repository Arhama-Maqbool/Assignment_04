def print_ones_digit(num :int):
    print(f"\nThe ones digit is {num % 10}")
    
def main():
    num = int(input("\n\033[1;34mEnter a number: \033[0m"))
    print_ones_digit(num)
    
if __name__ == "__main__":
    main()