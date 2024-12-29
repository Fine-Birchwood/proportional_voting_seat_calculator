import time
import seat_calculation
import board_submission_GUI
import party_data_collection

# Lists used throughout this program
party_list = []
party_votes = []
quota_list = []
results_list = []

# Creates a GUI where the user describes the board and how many elected parties are participating in the election. 

number_of_seats, number_of_elected_parties = board_submission_GUI.create_and_run_gui()

# Creates a GUI where the user inputs the name of the party/group and the number of votes the party/group has.

party_list, party_votes, quota_list = party_data_collection.collect_party_data(number_of_elected_parties)


#This function ensures that everything is correctly formatted. 
for i in range(len(party_votes)):
    party_votes[i] = party_votes[i] / quota_list[i] 


seat_calculation.calculation(party_list, party_votes, quota_list, number_of_elected_parties, number_of_seats, results_list)


print('Calculating the distribution of seats...')
print(' ')


occurrences = {item: results_list.count(item) for item in party_list}
sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
highest_occurrence = max(occurrences.items(), key=lambda x: x[1])

time.sleep(3)

print(f"{'Party/group':<25} {'Count'}")
print("-" * 35)
for item, count in sorted_occurrences:
    print(f"{item:<25} {count}")

print(' ')
print(f'The party/group with the highest number of won seats are {highest_occurrence[0]} with {highest_occurrence[1]} seats.')
print(' ')