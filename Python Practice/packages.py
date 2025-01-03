# main.py

def greet_user(N):
    print(f"Hello,{N}! Welcome!")

# Function to display the user's age
def display_age(age):
    print(f"You are {age} years old.")

def main():
    try:
        # Input for name
        while True:
            name = input("Enter your name: ").strip()
            if name.isdigit():
                print("Invalid input: Name cannot be a number. Please try again.")
            elif name == "":
                print("Name cannot be empty. Please try again.")
            else:
                break 
        

            # Input for age
        while True:
            try:
                age = int(input("Enter your age: "))
                
            except ValueError:
                print("Error: Age must be a valid number. Please try again.")
            else:
                break


        # Call functions
        greet_user(name)
        display_age(age)

       
    except Exception as e:
     print(f"Unexpected error: {e}")

# Run the program
main()