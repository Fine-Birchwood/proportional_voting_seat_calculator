import random
import tkinter as tk
from tkinter import scrolledtext
import datetime

def calculation(party_list, party_votes, quota_list, number_of_seats):
    # Counter used to keep track of number of seats left
    counter = 0

    # Results list to be populated
    results_list = []

    # Create Tkinter window
    window = tk.Tk()
    window.title("Election Results")
    
    # Create a ScrolledText widget for displaying results
    output_text = scrolledtext.ScrolledText(window, width=80, height=20, wrap=tk.WORD)
    output_text.grid(row=0, column=0, padx=10, pady=10)

    # Function to perform calculations and show results
    def start_calculation():
        nonlocal counter  # Access the outer counter variable

        # Open a file to log the results with a timestamp
        with open('election_results.txt', 'a') as file:
            while counter < number_of_seats:
                # Timestamp for each round
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if counter == 0:
                    max_value = max(party_votes)
                    max_indices = [i for i, value in enumerate(party_votes) if value == max_value]
                    selected_index = random.choice(max_indices)
                    results_list.append(party_list[selected_index])
                    quota_list[selected_index] += 1
                    counter += 1

                    # Display the results in the Tkinter window
                    output_text.insert(tk.END, f"\nRound {counter} - {timestamp}\n")
                    output_text.insert(tk.END, f"The votes for round {counter} are as follows:\n")
                    output_text.insert(tk.END, f"{'Item':<25} {'Value'}\n")
                    output_text.insert(tk.END, "-" * 35 + "\n")

                    for item, value in zip(party_list, party_votes):
                        output_text.insert(tk.END, f"{item:<25} {value:.2f}\n")

                    output_text.insert(tk.END, f"\nThe highest number of round {counter} is {party_votes[selected_index]:.2f}\n")
                    output_text.insert(tk.END, f"The winner of the round is {party_list[selected_index]}\n")
                    
                    # Log results to text file
                    file.write(f"Round {counter} - {timestamp}\n")
                    for item, value in zip(party_list, party_votes):
                        file.write(f"{item:<25} {value:.2f}\n")
                    file.write(f"The highest number of round {counter} is {party_votes[selected_index]:.2f}\n")
                    file.write(f"The winner of the round is {party_list[selected_index]}\n")
                    file.write("\n")

                else:
                    party_votes_dummy = party_votes.copy()
                    for i in range(len(party_votes)):
                        party_votes_dummy[i] = party_votes[i] / quota_list[i]

                    max_value = max(party_votes_dummy)
                    max_indices = [i for i, value in enumerate(party_votes_dummy) if value == max_value]
                    selected_index = random.choice(max_indices)
                    results_list.append(party_list[selected_index])
                    quota_list[selected_index] += 1
                    counter += 1

                    # Display the results in the Tkinter window
                    output_text.insert(tk.END, f"\nRound {counter} - {timestamp}\n")
                    output_text.insert(tk.END, f"The votes for round {counter} are as follows:\n")
                    output_text.insert(tk.END, f"{'Item':<25} {'Value'}\n")
                    output_text.insert(tk.END, "-" * 35 + "\n")

                    for item, value in zip(party_list, party_votes_dummy):
                        output_text.insert(tk.END, f"{item:<25} {value:.2f}\n")

                    output_text.insert(tk.END, f"\nThe highest number of round {counter} is {party_votes_dummy[selected_index]:.2f}\n")
                    output_text.insert(tk.END, f"The winner of the round is {party_list[selected_index]}\n")
                    
                    # Log results to text file
                    file.write(f"Round {counter} - {timestamp}\n")
                    for item, value in zip(party_list, party_votes_dummy):
                        file.write(f"{item:<25} {value:.2f}\n")
                    file.write(f"The highest number of round {counter} is {party_votes_dummy[selected_index]:.2f}\n")
                    file.write(f"The winner of the round is {party_list[selected_index]}\n")
                    file.write("\n")

                # Make sure the Tkinter window updates immediately
                window.update_idletasks()
                window.update()

            # Once the rounds are complete, display occurrences
            occurrences = {item: results_list.count(item) for item in party_list}
            sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
            highest_occurrence = max(occurrences.items(), key=lambda x: x[1])

            # Display occurrences in the Tkinter window
            output_text.insert(tk.END, "\n" + f"{'Party/group':<25} {'Count'}\n")
            output_text.insert(tk.END, "-" * 35 + "\n")
            for item, count in sorted_occurrences:
                output_text.insert(tk.END, f"{item:<25} {count}\n")

            output_text.insert(tk.END, '\n')
            output_text.insert(tk.END, f'The party/group with the highest number of won seats is {highest_occurrence[0]} with {highest_occurrence[1]} seats.\n')

            # Log occurrences to text file
            file.write("\n" + f"{'Party/group':<25} {'Count'}\n")
            file.write("-" * 35 + "\n")
            for item, count in sorted_occurrences:
                file.write(f"{item:<25} {count}\n")

            file.write('\n')
            file.write(f'The party/group with the highest number of won seats is {highest_occurrence[0]} with {highest_occurrence[1]} seats.\n')

            # Close the Tkinter window after the results are displayed
            window.update_idletasks()
            window.update()

    # Create a start button for the user to trigger the calculation
    start_button = tk.Button(window, text="Start Calculation", command=start_calculation)
    start_button.grid(row=1, column=0, padx=10, pady=10)

    # Create a close button to close the window
    close_button = tk.Button(window, text="Close", command=window.destroy)
    close_button.grid(row=2, column=0, padx=10, pady=10)

    # Run the Tkinter event loop
    window.mainloop()

    return results_list
