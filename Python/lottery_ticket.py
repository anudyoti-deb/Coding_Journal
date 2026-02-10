# Problem Statement : Generate a list of random lottery ticket numbers. Choose one winning ticket from that list.

# My Solution
import random

def generate_tickets(ticket_required):
        my_list = [i for i in range(1, 51)]
        sel = random.sample(my_list, ticket_required)
        win = random.choice(sel)
        return sel, win
try:
    tickets_required = int(input("How many tickets required (max 50) ?: "))
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
