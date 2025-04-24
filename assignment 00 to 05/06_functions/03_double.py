def double(num: int):
    return num * 2
    
def main():
    num = int(input("\n\033[1;3mEnter a number: \033[0m"))
    
    num_times_2 = double(num)
    print(f"\nDouble that is {num_times_2}")
    
if __name__ == '__main__':
    main()
    