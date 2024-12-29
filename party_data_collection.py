import tkinter as tk

# Function to collect party names and votes
def collect_party_data(number_of_elected_parties):
    # Create the main window
    root = tk.Tk()
    root.title("Enter Party Data")

    # Lists to store the party names, votes, and quotas
    party_list = []
    party_votes = []
    quota_list = []

    # Label and entry for party name
    label_party = tk.Label(root, text="Enter Party/Group Name:")
    label_party.pack(pady=5)
    entry_party = tk.Entry(root)
    entry_party.pack(pady=5)

    # Label and entry for party votes
    label_votes = tk.Label(root, text="Enter Number of Votes:")
    label_votes.pack(pady=5)
    entry_votes = tk.Entry(root)
    entry_votes.pack(pady=5)

    # Label to display the list of entered parties and votes
    label_display = tk.Label(root, text="Submitted Entries:")
    label_display.pack(pady=10)

    # Function to handle submit button click
    def submit_data():
        # Get party name and votes from the entries
        new_party = entry_party.get()
        try:
            votes = int(entry_votes.get())
        except ValueError:
            print("Invalid vote count. Please enter a number.")
            return  # Exit the function if votes are not a valid integer
        
        # Add the data to the lists
        party_list.append(new_party)
        party_votes.append(votes)
        quota_list.append(1)  # Assuming a fixed quota value, or adjust as needed

        # Update the display of submitted parties and votes
        display_text = "\n".join([f"{party}: {votes} votes" for party, votes in zip(party_list, party_votes)])
        label_display.config(text=f"Submitted Entries:\n{display_text}")

        # Clear the entry fields for next input
        entry_party.delete(0, tk.END)
        entry_votes.delete(0, tk.END)

        # Check if the desired number of parties have been entered
        if len(party_list) >= number_of_elected_parties:
            root.destroy()  # Destroys the window after collecting the required number of entries
            
    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

    # Return the lists after data collection is complete
    return party_list, party_votes, quota_list