AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"\nPlease type the following affirmation: \033[1;34m{AFFIRMATION} \033[0m")

    user_feedback = input() 
    while user_feedback != AFFIRMATION: 
        print("That was not the affirmation.")

        print(f"\nPlease type the following affirmation: \033[1;34m{AFFIRMATION} \033[0m")
        user_feedback = input()

    print("\nThat's right! :)")




if __name__ == '__main__':
    main()