service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def d():
    '='*50

def next_id() : 
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id :
            last_id= id
    return last_id + 1


def new_ticket(): 
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (y/n)").lower()
        if correct == 'y': 
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else:
            continue

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
        if ans == '1' :
            new_ticket()
        elif ans == '2': #create a function that displays all service tickets
           ticket_spread()
        elif ans == '3': # create a function that updates a open service ticket
         pass
        elif ans == '4':
            print("Thanks for using our service ticket app.")
            break
        else:
            print("Invalid option please pick one")

def ticket_spread():
    for key, value in service_tickets.items() :
        print (f"Service Ticket : {key}")
        print (f"Customer : {value['Customer']}")
        print (f"Issue : {value['Issue']},")
        print (f'Status : {value['Status']}\n') 


def update_ticket_status():
    ticket_id = int(input("Enter the ticket ID to update: "))
    
    if ticket_id not in service_tickets:
        print(f"Ticket {ticket_id} does not exist.")
        return
    
    current_status = service_tickets[ticket_id]['Status']
    
    if current_status == 'closed':
        print(f"Ticket {ticket_id} is already closed.")
        return
    
    if current_status == 'open':
        user_input = input("Are you sure you want to close this ticket? (This cannot be reversed) y/n: ").strip().lower()
        if user_input == 'y':
            service_tickets[ticket_id]['Status'] = 'closed'
            print(f"Ticket {ticket_id} status updated to 'closed'.")
            print(f'Ticket {ticket_id} has been closed.')
        elif user_input == 'n':
            print("Ticket status update cancelled.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }