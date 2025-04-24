def get_name():
    name = input("\n\033[1;3;34mEnter your name: \033[0m")
    return name

def main():
    name = get_name()
    print(f"\nHowdy, {name}! 🤠")
    
if __name__ == '__main__':
    main()