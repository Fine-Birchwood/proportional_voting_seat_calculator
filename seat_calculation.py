import random

def calculation(party_list, party_votes, quota_list, number_of_elected_parties, number_of_seats, results_list):
   
    counter = 0

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

                print(f"{'Item':<25} {'Value'}")
                print("-" * 35)

                for item, value in zip(party_list, party_votes):
                    print(f"{item:<25} {value:.2f}")

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

                print(f"{'Item':<25} {'Value'}")
                print("-" * 35)

                for item, value in zip(party_list, party_votes_dummy):
                    print(f"{item:<25} {value:.2f}")

                print(' ')

                print(f'The highest number of round {counter} is {party_votes_dummy[selected_index]:.2f}')
                print(f'The winner of the round is {party_list[selected_index]}')
                print(' ')
    
        if counter >= number_of_seats:
            break

    return

