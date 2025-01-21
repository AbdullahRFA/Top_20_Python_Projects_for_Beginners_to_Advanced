from time import time  # Import time module to measure typing speed
import random as ran  # Import random module for random text selection


# Function to find mistakes between the test text and user input
def find_mistake(par_test, user_test):
    error = 0  # Initialize error count
    for i in range(len(par_test)):  # Loop through each character in the test text
        try:
            if par_test[i] != user_test[i]:  # Check if characters don't match
                error += 1  # Increment error count for mismatches
        except IndexError:  # Handle cases where user input is shorter than test text
            error += 1  # Increment error count for missing characters
    return error


# Function to calculate typing speed
def speed_time(time_s, time_e, user_input):
    time_delay = round(time_e - time_s, 2)  # Calculate time taken in seconds
    speed = len(user_input) / time_delay  # Calculate speed as characters per second
    return round(speed)  # Return rounded speed value


# List of test strings for the typing test
test_string = [
    'This is Abdullah Nazmus-Sakib',
    'I am a student of Jahangirnagar University',
    'I came from Bagmara, Rajshahi',
    'I completed my HSC from N.S Govt College Natore'
]

# Randomly select a test string
test = ran.choice(test_string)

print("***** Typing Speed Test *****")
 # Display the test string
print(test, "\n")


# Main logic for the typing speed test
if __name__ == "__main__":
    while True:
        # Ask the user if they are ready to start the test
        check = input("Ready to start typing? (yes or no): ").strip()

        if check.lower() == 'yes':
            # Record the start time
            start_time = time()
            print(test, "\n")
            # Accept user input for typing test
            test_input = input("Enter: ")

            # Record the end time
            end_time = time()
            # Calculate typing accuracy
            mistakes = find_mistake(test, test_input)
            accuracy = round(((len(test) - mistakes) / len(test)) * 100, 2)

            # Display results
            print("Speed: ", speed_time(start_time, end_time, test_input), "W/Sec")  # Words per second
            print("Error: ", mistakes)  # Number of errors
            print("Accuracy: ", accuracy, "%")  # Accuracy percentage

        elif check.lower() == 'no':
            print("Thank you for participating")
            break  # Exit the loop if user is not ready

        else:
            print("Enter your choice as 'yes' or 'no'")