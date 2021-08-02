from services.ticket_service import TicketService
from services.user_input_validation_service import UserInputValidationService
import math


class TicketView:
    validation_service: UserInputValidationService
    ticket_service: TicketService = None
    ticket_list: list = None

    def __init__(self):
        # handle ticket loading service (multiple tickets)
        self.ticket_service = TicketService()
        self.validation_service = UserInputValidationService()

    def display_tickets(self):
        current_page = 1
        tickets_per_page = 25
        while True:
            print("\n***** View all tickets *****")
            ticket_list = self.ticket_service.get_ticket_list(
                page_number=current_page, tickets_per_page=tickets_per_page)
            for ticket in ticket_list:
                print(ticket.get_summary())
            total_pages = self.ticket_service.metadata.count/tickets_per_page
            print(
                f'\nCurrent page: {current_page}, Total pages: {math.ceil(total_pages)}')
            print(f'Options:')
            print('[p] <- Previous Page')
            print('[n] Next Page ->')
            print('[m] Return to Main Menu')
            user_input = input('Enter an option: ')
            self.validation_service.validate_display_tickets_input(
                user_input=user_input)
            if user_input == 'p':
                if current_page > 1:
                    current_page -= 1
                else:
                    raise Exception  # TODO: create specific PageOutOfBoundsException
            elif user_input == 'n':
                if current_page < total_pages:
                    current_page += 1
                else:
                    raise Exception  # TODO: create specific PageOutOfBoundsException
            elif user_input == 'm':
                break

    def display_single_ticket(self):
        user_input = input('Enter ticket ID: ')
        self.validation_service.validate_view_single_ticket_input(
            user_input=user_input)
        print(self.ticket_service.get_single_ticket(ticket_id=user_input))
