import tkinter as tk
from tkinter import ttk

# Function to create and run the GUI
def create_and_run_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Information about the board")

    # Variables to store the selected values
    number_of_seats = None
    number_of_elected_parties = None

    # Function to submit the selected values and close the program
    def submit_values():
        nonlocal number_of_seats, number_of_elected_parties

        # Get the selected values from both comboboxes
        number_of_seats = combobox1.get()
        number_of_elected_parties = combobox2.get()

        # Check if values are selected and assign them to the variables
        if number_of_seats and number_of_elected_parties:
            # Convert to integers
            number_of_seats = int(number_of_seats)
            number_of_elected_parties = int(number_of_elected_parties)

            # Close the program after submission
            root.destroy()  # Ends the mainloop and closes the window
        else:
            print("Please select values from both comboboxes.")

    # Create the Comboboxes for numerical values
    number_of_seats_list = [i for i in range(1, 51)]  # List of numbers 1 to 50
    numbers2 = [i for i in range(1, 151)]  # List of numbers 1 to 150

    # Label for the first combobox
    label1 = tk.Label(root, text="Please select the number of seats the board has:")
    label1.pack(pady=5)

    combobox1 = ttk.Combobox(root, values=number_of_seats_list, state="readonly")  # First combobox
    combobox1.pack(pady=10)

    # Label for the second combobox
    label2 = tk.Label(root, text="Please select the number of elected parties:")
    label2.pack(pady=5)

    combobox2 = ttk.Combobox(root, values=numbers2, state="readonly")  # Second combobox
    combobox2.pack(pady=10)

    # Create a Submit button to save selected values
    submit_button = tk.Button(root, text="Submit", command=submit_values)
    submit_button.pack(pady=10)

    # Start the Tkinter event loop (it will stop once root.quit() is called)
    root.mainloop()

    # Return the values as integers
    return number_of_seats, number_of_elected_parties


if __name__ == "__main__":
    # Call the function and get the returned values once
    number_of_seats, number_of_elected_parties = create_and_run_gui()