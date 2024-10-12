# File Creation and Writing
def create_and_write_file():
    try:
        # Create a new file and write three lines of text
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 123.\n")
            file.write("And this is line 3 with some more text.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# File Reading and Display
def read_and_display_file():
    try:
        # Open the file in read mode and display its contents
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File Appending
def append_to_file():
    try:
        # Open the file in append mode and add three new lines
        with open("my_file.txt", "a") as file:
            file.write("Appending line 4 with some text.\n")
            file.write("Appending line 5 with a number: 456.\n")
            file.write("Appending line 6 as the last line.\n")
        print("New lines appended to the file successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Main function to execute all tasks
def main():
    try:
        # Create and write to the file
        create_and_write_file()

        # Read and display the file's contents
        read_and_display_file()

        # Append to the file
        append_to_file()

        # Read and display the updated contents
        read_and_display_file()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nScript execution completed.")

# Execute the main function
if __name__ == "__main__":
    main()
