import random
import time

#Counter value used for this program
counter = 0

# Lists used throughout this program
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

print(f'Thanks for the information. Please input party/group name and their number of votes')
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

#This function ensures that everything is correctly formatted. 
for i in range(len(party_votes)):
    party_votes[i] = party_votes[i] / quota_list[i] 


#This function go through and calculates who has one each seat. 
while True:
    if counter < number_of_seats:
        
        if counter == 0: 
            max_value = max(party_votes)
            max_indices = [i for i, value in enumerate(party_votes) if value == max_value]
            selected_index = random.choice(max_indices)
            results_list.append(party_list[selected_index])
            quota_list[selected_index] += 1
            counter += 1 

            print(f'The votes for round {counter} is as following')
            print(' ')

            print(f"{'Item':<15} {'Value'}")
            print("-" * 20)

            for item, value in zip(party_list, party_votes):
                print(f"{item:<15} {value:.2f}")

            print(' ')

            print(f'The highest number of round {counter} is {party_votes[selected_index]:.2f}')
            print(f'The winner of the round is {party_list[selected_index]}')
            print(' ')


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

            print(f'The votes for round {counter} is as following')
            print(' ')

            print(f"{'Item':<15} {'Value'}")
            print("-" * 20)

            for item, value in zip(party_list, party_votes_dummy):
                print(f"{item:<15} {value:.2f}")

            print(' ')

            print(f'The highest number of round {counter} is {party_votes_dummy[selected_index]:.2f}')
            print(f'The winner of the round is {party_list[selected_index]}')
            print(' ')
 
    if counter >= number_of_seats:
        break

print('Calculating the distribution of seats...')
print(' ')


occurrences = {item: results_list.count(item) for item in party_list}
sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
highest_occurrence = max(occurrences.items(), key=lambda x: x[1])

time.sleep(3)

print(f"{'Party/group':<15} {'Count'}")
print("-" * 25)
for item, count in sorted_occurrences:
    print(f"{item:<15} {count}")

print(' ')
print(f'The party/group with the highest number of won seats are {highest_occurrence[0]} with {highest_occurrence[1]} seats.')
print(' ')