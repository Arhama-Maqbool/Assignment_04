def main():
    
    lst = []
    value = input("\n\033[1;3mEnter a value: \033[0m")
    
    while value != "":
        lst.append(value)
        value = input("\n\033[1;3mEnter a value: \033[0m")
        
    print("\n📜 Here's the list:", lst)
    
if __name__ == '__main__':
    main()