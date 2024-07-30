from xtra import new_ticket
from xtra import next_id
from xtra import ticket_spread
from xtra import update_ticket_status


service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def main() :
    while True:
        ans = input('''
SERVICE TICKETS
Enter the number of what you'd like to do.
    1 - open a new service ticket
    2 - Display all service tickets
    3 - Update a open service ticket
    4 - Quit


''')
        if ans =='1' :
            new_ticket()
        elif ans =='2': #create a function that displays all service tickets
            ticket_spread()
        elif ans =='3': # create a function that updates a open service ticket
           update_ticket_status()
        elif ans =='4':
            print("Thanks for using our service ticket app.")
            break
        else:
            print("Invalid option please pick one")

main()
