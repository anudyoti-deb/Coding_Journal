# Problem Statement : Generate a list of random lottery ticket numbers. Allow the user to pick one ticket to see if it's the winning ticket.

# My Solution
import random

def generate_tickets(ticket_required):
        my_list = [i for i in range(1, 51)]
        sel = random.sample(my_list, ticket_required)
        win = random.choice(sel)
        return sel, win
try:
    tickets_required = int(input("How many tickets required (max 50) ?: ")) # arbitrary number 50
    if tickets_required > 50:
        tickets_required = 50
    else:
        tickets_required = tickets_required
except ValueError:
    print("Invalid Value")
else:
    ticket_numbers, winning_ticket = generate_tickets(tickets_required)
    print('Below are the list of tickets to choose from \n', ticket_numbers)
    while True:
        selected_ticket = int(input("Please choose your ticket."))
        if selected_ticket in ticket_numbers:
            break
        else:
            print("Please select ticket number from the above list")
    if selected_ticket == winning_ticket:
        print(f'The winning ticket is {winning_ticket}. Congratulations!! You won.')
    else:
        print(f'The winning ticket is {winning_ticket}. You Lost!! Better luck next time.')

# My Approach
'''
- Input from user → Ask how many tickets should be generated.
- Generate tickets → Create a list of random numbers with that count.
- User selection → Prompt the user to choose one ticket number from the list.
- Winning ticket → Randomly select one ticket internally as the winner.
- Comparison → Compare the user’s choice with the winning ticket.
- Result → If they match, the user wins; otherwise, they lose.
'''

# Complexity Analysis
'''
- Time: O(n) for generating the list of tickets, where n = number of tickets.
- Space: O(n) to store the list of tickets.
'''

# Source : PCAP Python Essentials 2 Module : String Manipulation


