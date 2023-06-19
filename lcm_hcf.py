def gcd(a, b):
    #Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    #LCM = (a * b) / gcd(a, b)
    return (a * b) // gcd(a, b)

def get_number_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    print("Welcome to LCM and HCF Calculator!")
    print("Enter two positive integers to calculate their LCM and HCF.")
    print()

    while True:
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")

        print(f"Calculating LCM and HCF for {num1} and {num2}...")
        
        lcm_result = lcm(num1, num2)
        hcf_result = gcd(num1, num2)

        print(f"LCM of {num1} and {num2} is: {lcm_result}")
        print(f"HCF of {num1} and {num2} is: {hcf_result}")

        choice = input("Do you want to calculate again? (y/n): ")
        if choice.lower() != 'y':
            break

    print("Thank you for using LCM and HCF Calculator!")

if __name__ == "__main__":
    main()
