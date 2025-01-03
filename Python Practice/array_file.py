def display_menu():
    print("\nChoose an operation:")
    print("1. Add an element to the array")
    print("2. Remove an element from the array")
    print("3. Sort the array")
    print("4. Reverse the array")
    print("5. Find the length of the array")
    print("6. Display the array")
    print("7. Exit")

# Initialize the array
arr = [1, 2, 3, 4, 5]

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add an element
        element = int(input("Enter the element to add: "))
        arr.append(element)
        print(f"After adding {element}: {arr}")

    elif choice == 2:
        # Remove an element
        element = int(input("Enter the element to remove: "))
        if element in arr:
            arr.remove(element)
            print(f"After removing {element}: {arr}")
        else:
            print(f"{element} not found in the array.")

    elif choice == 3:
        # Sort the array
        arr.sort()
        print("After sorting:", arr)

    elif choice == 4:
        # Reverse the array
        arr.reverse()
        print("After reversing:", arr)

    elif choice == 5:
        # Find the length of the array
        print("Length of the array:", len(arr))

    elif choice == 6:
        # Display the array
        print("Current array:", arr)

    elif choice == 7:
        # Exit the loop
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please choose a valid option.")