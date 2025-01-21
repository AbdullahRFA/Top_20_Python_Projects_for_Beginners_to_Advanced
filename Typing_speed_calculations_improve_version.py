import time
import random


def find_mistake(par_test, user_test):
    """
    Function to find mistakes between the test text and user input.
    Counts character mismatches and missing characters.
    """
    errors = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] != user_test[i]:
                errors += 1
        except IndexError:  # User input shorter than the test text
            errors += 1
    return errors

# TODO improve hobe ei section for better visualizations
def show_mistakes(par_test, user_test):
    """
    Function to highlight mistakes in the user's input.
    Shows mismatched or missing characters.
    """
    result = []  # List to store the output with highlights
    for i in range(len(par_test)):
        try:
            if par_test[i] == user_test[i]:
                result.append(par_test[i])  # Correct characters
            else:
                result.append(f"[{user_test[i]}]")  # Highlight incorrect characters
        except IndexError:  # Missing characters from user input
            result.append("_")  # Use underscore for missing characters
    return ''.join(result)  # Convert list to string


def calculate_speed(start_time, end_time, user_input):
    """
    Calculate typing speed in words per minute (WPM).
    """
    time_taken = end_time - start_time
    words = len(user_input.split())  # Count words typed by the user
    speed = (words / time_taken) * 60  # Words per minute
    return round(speed, 2)


def typing_test():
    """
    Main function to run the typing speed test.
    """
    # Difficulty levels
    levels = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard"
    }
    test_strings = {
        "1": [
            "The cat is on the mat.",
            "Python is a great language.",
            "Hello world, welcome to programming."
        ],
        "2": [
            "Typing fast requires practice and focus.",
            "Artificial intelligence is the future of technology.",
            "Machine learning is a subset of AI."
        ],
        "3": [
            "Quantum computing is an emerging technology.",
            "The quick brown fox jumps over the lazy dog.",
            "Developing strong typing skills takes consistent effort."
        ]
    }

    # Select difficulty level
    print("\nChoose a difficulty level:")
    for key, value in levels.items():
        print(f"{key}: {value}")
    level = input("\nEnter your choice (1, 2, or 3): ").strip()
    if level not in test_strings:
        print("Invalid choice. Exiting the test.")
        return

    # Randomly select a test string based on difficulty level
    test_text = random.choice(test_strings[level])
    print("\nGet ready to type the following text:")
    print("-" * 40)
    print(test_text)
    print("-" * 40)

    input("\nPress Enter when you are ready to start typing...")
    start_time = time.time()  # Record start time

    # Accept user input
    user_input = input("\nStart typing: ")
    end_time = time.time()  # Record end time

    # Calculate results
    speed = calculate_speed(start_time, end_time, user_input)
    mistakes = find_mistake(test_text, user_input)
    accuracy = round(((len(test_text) - mistakes) / len(test_text)) * 100, 2)

    # Display results
    print("\nTyping Test Results")
    print("=" * 40)
    print(f"Typing Speed  : {speed} words per minute")
    print(f"Errors Made   : {mistakes}")
    print(f"Accuracy      : {accuracy}%")
    print("=" * 40)

    # Show where mistakes were made
    print("\nHighlighting Mistakes:")
    print("Correct Text: ", test_text)
    print("Your Input  : ", show_mistakes(test_text, user_input))

    # Provide feedback
    if speed > 60 and accuracy > 90:
        print("\nExcellent typing skills! Keep it up!")
    elif speed > 40:
        print("\nGood typing speed, but you can improve further.")
    else:
        print("\nKeep practicing to improve your typing skills!")


if __name__ == "__main__":
    # Display welcome message
    print("=" * 40)
    print("Welcome to the Online Typing Speed Test")
    print("=" * 40)
    while True:
        choice = input("\nDo you want to take the test again? (yes/no): ").strip().lower()
        if choice == "yes":
            typing_test()
        elif choice == "no":
            print("\nThank you for using the Typing Speed Test. Goodbye!")
            break
        else:
            print("\nPlease press either 'yes' or 'no'")