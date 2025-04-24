MAX_LENGTH = int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"\n\033[1;3mRemoved: {last_elem} \033[0m")
    print(f"\n\033[1;3mShortened list: {lst} \033[0m")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\nPlease enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("\nPlease enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    print("\nThe full list is:", lst)
    shorten(lst)


if __name__ == '__main__':
    main()