def check_number():
    try:
        user_input = input("Enter a number: ")
        # Convert input to a float first to check if it's numeric
        num = float(user_input)

        # Check if the input is an integer
        if num.is_integer():
            num = int(num)  # Convert to integer for comparison
            if num > 0:
                print("Positive")
            elif num < 0:
                print("Negative")
            else:
                print("Zero")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")

# Call the function
check_number()
