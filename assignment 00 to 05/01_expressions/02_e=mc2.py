c: int = 2997924858

def main():

    mass_in_kg: float = float(input("Enter Kilos of mass: "))

    energy_in_joules: float = mass_in_kg * (c ** 2)

    print("e = m * C^2...")
    print("m = "  + str(mass_in_kg) + "kg" )
    print("c = "  + str(c) + "m/s")
    print(str(energy_in_joules) +  "joules_of_energy!")
if __name__ == "__main__":
  main()
    
