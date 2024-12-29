import time
import seat_calculation

# Empty lists used throughout this program
party_list = []
party_votes = []
quota_list = []
results_list = []

# Introductory questions regarding the current board
number_of_seats = int(input('How many seats are there in the current board? '))
number_of_elected_parties = int(input('How many parties have been elected to the current board? '))
print(' ')

print('The board has', number_of_seats, 'seats')
print('The board has', number_of_elected_parties, 'elected parties')
print(' ')

print(f'Thanks for the information. Please input party/group name and their number of votes.')
print(' ')

time.sleep(2)

#This function creates two lists that will be used to count the seats per party/group. 
while True:
    new_party = str(input('What is the party’s or group’s name? '))
    party_list.append(new_party)
    votes = int(input('How many votes did the party/group get? '))
    party_votes.append(votes)
    quota_list.append(1)
    print(' ')

    if len(party_list) >= number_of_elected_parties:
        break


print(f'Simulating each round...')
print(' ')
time.sleep(3)

#This function ensures that everything is correctly formattede before it's submitted to the seat calculation function.

for i in range(len(party_votes)):
    party_votes[i] = party_votes[i] / quota_list[i] 

#This calls the seat calculation function from seat_calculation.py.

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