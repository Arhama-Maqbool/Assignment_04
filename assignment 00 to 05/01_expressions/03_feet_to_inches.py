INCHES_IN_FOOT: int = 12
def feet_to_inches():

    print("This operation is convert feet to inches")

    feet: int = float(input("Enter your feet here: "))
    inches: float = feet * INCHES_IN_FOOT

    print("There is" , inches , "inches in" , feet , "feet")
     
if __name__ == "__main__":
    feet_to_inches()     