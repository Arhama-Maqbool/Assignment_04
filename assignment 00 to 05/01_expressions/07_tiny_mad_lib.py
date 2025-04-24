SENTENCE_START: str = "panaversity is fun. I learned to program and used python to make my "

def main():
    adjective = input("Enter an adjective and press enter: ")
    noun = input("Enter a noun and press enter: ")
    verb = input("Enter a verb and press enter: ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()
