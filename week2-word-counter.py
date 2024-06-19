def count_words(input_text):
  """
  This function takes a string as input and returns the number of words in it.
  A word is defined as a sequence of characters separated by whitespace.
  """
  # Split the input text by whitespace and filter out empty strings
  words = input_text.split()
  return len(words)

def main():
  """
  Main function to handle user input, word counting, and output display.
  """
  # Prompt the user to enter a sentence or paragraph
  input_text = input("Please enter a sentence or paragraph: ").strip()

  # Check if the input is empty
  if not input_text:
      print("Error: The input is empty. Please enter a valid sentence or paragraph.")
      return

  # Count the number of words in the input
  word_count = count_words(input_text)

  # Display the word count to the user
  print(f"The number of words in the input is: {word_count}")

# Run the main function if this script is executed
if __name__ == "__main__":
  main()

