def check_food_category():
    try:
        number = int(input("Enter a number: "))
        
        if number % 10 == 0:
            print("non-vegetarian")
        elif number % 5 == 0:
            print("vegetarian")
        else:
            print("The number is not divisible by 5 or 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function
check_food_category()
