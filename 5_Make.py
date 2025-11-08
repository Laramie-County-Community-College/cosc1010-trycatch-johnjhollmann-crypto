'''
A pedometer treats walking 2,000 steps as walking 1 mile. 

Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. 

The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
 Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the 
 steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345
the output of the program is:

2.67
Ex: If the input of the program is:

-3850
the output of the program is:

Exception: Negative step count entered.
'''

# Define your method here
def steps_to_miles(steps):
    """
    Converts a number of steps to miles walked, assuming 2000 steps equals 1 mile.

    Args:
        steps: The number of steps taken.

    Returns:
        The distance walked in miles.

    Raises:
        ValueError: If the number of steps is negative.
    """
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    # The problem statement specifies 2000 steps = 1 mile
    miles = steps / 2000.0
    return miles

def main():
    """
    Reads steps from the user, calls steps_to_miles, and prints the result or error message.
    """
    try:
        # Read input from the user
        steps_input = input("Enter the number of steps: ")
        # Convert the input string to an integer
        steps = int(steps_input)
        
        # Call the steps_to_miles function
        miles_walked = steps_to_miles(steps)
        
        # Output the result formatted to two decimal places
        print(f'{miles_walked:.2f}')
        
    except ValueError as excpt:
        # Catch the ValueError from steps_to_miles or an invalid integer conversion
        print(excpt)
    except Exception as excpt:
        # Catch any other potential exceptions
        print(f"An unexpected error occurred: {excpt}")

if __name__ == "__main__":
    main()
