import time
import random


def highlight_mistakes(par_test, user_test):
    """
    Highlight mistakes in the user's input character by character within each word.
    """
    par_words = par_test.split()
    user_words = user_test.split()
    highlighted_output = []
    total_errors = 0
    missing_words = 0
    extra_characters = 0

    for i in range(max(len(par_words), len(user_words))):
        try:
            # Compare words
            par_word = par_words[i]
            user_word = user_words[i]
            highlighted_word = []

            # Compare characters within words
            for j in range(max(len(par_word), len(user_word))):
                try:
                    if par_word[j] == user_word[j]:
                        highlighted_word.append(par_word[j])
                    else:
                        highlighted_word.append(f"[{user_word[j]}]")  # Incorrect character
                        total_errors += 1
                except IndexError:
                    # User word is shorter
                    highlighted_word.append(f"_[{par_word[j]}]_")  # Missing character
                    total_errors += 1
            highlighted_output.append("".join(highlighted_word))
        except IndexError:
            # Handle missing words
            highlighted_output.append(f"_[{par_words[i]}]_")
            missing_words += 1

    # Handle extra words
    if len(user_words) > len(par_words):
        extra_characters += sum(len(word) for word in user_words[len(par_words):])
        highlighted_output.extend([f"[{word}]" for word in user_words[len(par_words):]])

    return " ".join(highlighted_output), total_errors, missing_words, extra_characters


def calculate_speed(start_time, end_time, user_input):
    """
    Calculate typing speed in words per minute (WPM).
    """
    time_taken = end_time - start_time
    words = len(user_input.split())
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
    highlighted_result, total_errors, missing_words, extra_chars = highlight_mistakes(test_text, user_input)
    accuracy = round(((len(test_text) - total_errors) / len(test_text)) * 100, 2)

    # Display results
    print("\nTyping Test Results")
    print("=" * 40)
    print(f"Typing Speed  : {speed} words per minute")
    print(f"Errors Made   : {total_errors}")
    print(f"Accuracy      : {accuracy}%")
    print("=" * 40)

    # Show detailed error breakdown
    print("\nError Breakdown:")
    print(f"- Missing words     : {missing_words}")
    print(f"- Extra characters  : {extra_chars}")
    print(f"- Total character-level errors : {total_errors}")

    # Highlight mistakes
    print("\nHighlighting Mistakes:")
    print("Correct Text: ", test_text)
    print("Your Input  : ", highlighted_result)

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