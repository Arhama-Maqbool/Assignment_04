def print_divisors (num:int):

    print(f"\nHere are the divisors of {num}")

    for i in range (num):
        curr_divisors = i + 1

    if num % curr_divisors == 0:
        print(curr_divisors)
        
def main():
    num = int(input("\n\033[1;3;34mEnter a number:\033[0m"))

    print_divisors(num)

if __name__ == "__main__":
    main()                