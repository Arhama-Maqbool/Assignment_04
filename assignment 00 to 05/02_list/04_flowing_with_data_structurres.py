def copies(list,data):
    for i in range(3):
        list.append(data)

def main():
    user_input = input("Enter a message to copy! :")
    my_list = []
    print("list before: ", my_list)
    copies(my_list , user_input)
    print("list after :" , my_list)

if __name__ == "__main__":
    main()    