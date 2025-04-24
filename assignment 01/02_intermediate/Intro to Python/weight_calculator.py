GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0 
}

def main():
    while True:
        
        earth_weight_str = input('\nEnter a weight on Earth (or type "exit" to quit): ')
        
        if earth_weight_str.lower() == "exit":
            print("\nThanks for using the Planetary Weight Calculator! Goodbye.")
            break
        
        try:
            earth_weight = float(earth_weight_str)
        except ValueError:
            print("\nPlease enter a valid number for Earth weight.")
            continue 
        
        planet = input("\nEnter a planet: ").capitalize()
        
        if planet in GRAVITY_CONSTANTS:
            gravity_constant = GRAVITY_CONSTANTS[planet]
            
        else:
           print("\nThat planet is not supported. Please try again.")
           continue
       
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)
        
        print(f"\nThe equivalent weight on {planet}: {rounded_planetary_weight}")
        print('-' * 40)
        
if __name__ == "__main__":
    main()