PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 23
MAYENGUA_AGE : int = 48

def main():
    user_age = int(input("\n\033[1;3;34mHow old are you? \033[0m"))

    if user_age >= PETURKSBOUIPO_AGE:
        print(f"\nYou can vote in \033[1;3;34mPeturksbouipo\033[0m where the voting age is \033[1;3;34m{PETURKSBOUIPO_AGE}\033[0m. " )
    else:
        print(f"\nYou cannot vote in \033[1;3;34mPeturksbouipo\033[0m where the voting age is \033[1;3;34m{PETURKSBOUIPO_AGE}\033[0m. ")
    
    if user_age >= STANLAU_AGE:
        print(f"You can vote in \033[1;3;34mStanlau\033[0m where the voting age is \033[1;3;34m{STANLAU_AGE}\033[0m." )
    else:
        print(f"You cannot vote in \033[1;3;34mStanlau\033[0m where the voting age is \033[1;3;34m{STANLAU_AGE}\033[0m." )
    
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in \033[1;3;34mMayengua\033[0m where the voting age is \033[1;3;34m{MAYENGUA_AGE}\033[0m. " )
    else:
        print(f"You cannot vote in \033[1;3;34mMayengua\033[0m where the voting age is \033[1;3;34m{MAYENGUA_AGE}\033[0m. " )


if __name__ == '__main__':
    main()