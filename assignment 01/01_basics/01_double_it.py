def main():
    user_input = int(input("\n\033[1;34mEnter a number: \033[0m"))
    curr_value = user_input * 2
    
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value *= 2
        
    print(curr_value)
    
    
    
if __name__ == "__main__":
    main()    
