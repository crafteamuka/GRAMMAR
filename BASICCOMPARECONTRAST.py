print("COMPARE AND CONTRAST")
# This is a basic code to compare two user inputs.
def compareandcontrast(): 
    # Prevents blank inputs
    def get_non_blank_input(prompt):
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            else:
                print("Input cannot be blank. Please try again.")

    FirstInput = get_non_blank_input("Enter Your First Text Here: ")
    SecondInput = get_non_blank_input("Enter Your Second Text Here: ")

    # Counts the number of letters in each input
    def wordcounter():
        print("Your first input has", len(FirstInput), "letters")
        print("Your second input has", len(SecondInput), "letters")
    
    # Counts the number of words in each input
    def count_words(input_text): 
        words = input_text.split()
        word_count = len(words)
        return word_count

    # Compares the two inputs using difference in length
    def difference():
        if len(FirstInput) > len(SecondInput):
            first_difference = len(FirstInput) - len(SecondInput)
            print("Your first input is longer than your second input by", first_difference, "letters")
        elif len(FirstInput) < len(SecondInput):
            second_difference = len(SecondInput) - len(FirstInput)
            print("Your first input is shorter than your second input by", second_difference, "letters")
        else:
            print("Your first input has the same length as your second input")

    # Compare the two inputs and print the results
    def compare():
        if FirstInput == SecondInput:
            print("No changes in your text")
        else:
            print("First Input:", FirstInput)
            print("Second Input:", SecondInput)
        
        wordcounter()
        difference()

        # Counts and prints the number of words in each input
        def wordchanger():    
            first_word_count = count_words(FirstInput)
            second_word_count = count_words(SecondInput)
        
            if first_word_count == 1:
                print(f"Your first input has {first_word_count} word.")
            else:
                print(f"Your first input has {first_word_count} words.")
        
            if second_word_count == 1:
                print(f"Your second input has {second_word_count} word.")
            else:
                print(f"Your second input has {second_word_count} words.")

        wordchanger()

    compare()

compareandcontrast()
