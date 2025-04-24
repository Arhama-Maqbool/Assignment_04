def subtract_seven(num):
    num = num - 7
    return num

def main():
    user_num: int = int(input("\nEnter a num: "))
    num = subtract_seven(user_num)
    print(f"this should be {num} after substracting from {user_num}")

if __name__ == '__main__':
    main()
