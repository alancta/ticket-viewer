
from exceptions import TicketException
from requests.exceptions import RequestException
import sys


class ErrorHandlingService:

    def __init__(self):
        pass

    def load_ticket_handler(self, response):
        if response.status_code == 401:
            print(
                'Oops! Authorization failed. Please check your credentials and restart the program.')
            sys.exit(1)
        elif response.status_code == 404:
            print('Ticket not found. Please check ticket ID.')
            raise TicketException

        print('The request was sent successfully, but the tickets failed to load.')
        sys.exit(1)

    def timeout_error_handler(self):
        print('Request took too long to respond and timed out, please check your internet connection.')
        sys.exit(1)

    def connection_error_handler(self):
        print('There was a problem with sending the request to the Tickets API, please check your connection and restart the program.')
        sys.exit(1)