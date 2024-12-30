import seat_calculation
import board_submission_GUI
import party_data_collection

# Results list used in the collect_paty_data-function in the party_data_collection-module. 
results_list = []

# Creates a GUI with the help of Ktinker where the user describes the board and how many elected parties are participating in the election. 

number_of_seats, number_of_elected_parties = board_submission_GUI.create_and_run_gui()

# Creates a GUI where the user inputs the name of the party/group and the number of votes the party/group has.

party_list, party_votes, quota_list = party_data_collection.collect_party_data(number_of_elected_parties)

#This function ensures that everything is correctly formatted before it's inputed into the seat_calculation-module.  

for i in range(len(party_votes)):
    party_votes[i] = party_votes[i] / quota_list[i] 

# This calculates the seat distribution and creates a text-file which displays the results of each round. 
# It also displays everything in a GU using Ktinker. 

results_list = seat_calculation.calculation(party_list, party_votes, quota_list, number_of_seats)