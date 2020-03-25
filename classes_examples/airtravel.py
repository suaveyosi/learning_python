""" Model for aircraft flights."""
# imports
from pprint import pprint as pp 
class Flight():
    def __init__(self,number,aircraft):
        # check that is a valid number uppercase AB and digit from 0 to 9999
        if not number[:2].isalpha():
            raise ValueError(f"No airline name in {number}")
        if not number[:2].isupper():
            raise ValueError(f"Airline code is not in uppercase {number}")
        if (not number[2:].isdigit()) or (int(number[2:]) > 9999):
            raise ValueError(f"Not a valid flight number {number}")
        self._number=number
        self._aircraft=aircraft
        # We define the seats and create a variable seating with the seats
        rows, seats = self._aircraft.seating_plan()
        # Aquí estamos creando para cada fila un diccionario que tiene como keys las letras y como value None {'A': None, 'B': None}, {'A': None, 'B': None}
        # como el numero no lo quiero, solo lo uso para iterar uso _
        # Añadimos una primera file dummy de None para que así los incides coincidan y cuando pongo asiento 1D empiece igual
        self._seating = [None] + [ {letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline_code(self):
        return self._number[:2]

    # We can use other class methods
    def aircraft_model(self):
        return self._aircraft.model()

    # Function to pretty print seat status using imported function
    def print_seating_status(self):
        pp(self._seating)

    # Function to check if a seat is within range. It will return the row and the letter if everything is correct, otherwise it'll raise an error
    def _parse_seat(self,seat):
        # Check the number of seats and the rows 
        rows, seats = self._aircraft.seating_plan()
        letter=seat[-1:]
        row=seat[:-1]
        # Check if letter is correct
        if (not letter.isalpha()) or (letter not in seats):
            raise ValueError(f"Invalid seat letter {letter}")
        # Check if row is within range
        if int(row) >= self._aircraft._num_rows+1:
            raise ValueError(f"Invalid row {row}")
        return int(row), letter

    def _seat_empty(self, row,letter):
        """
        Check if seat is empty or already occupied. If empty return true
        """
        if self._seating[row][letter] is not None:
            return 0
        else:
            return 1

    # Function to allocate passengers
    def allocate_seat(self,seat,passenger):
        """
        Allocate seat to a passenger
        Args:
            seat: to be seated on 12C
            passenger: name of the passenger
        """
        row, letter = self._parse_seat(seat)
        # Check if the seat is occupied
        print("Intentando sentar a {} en el asiento {}".format(passenger,seat))
        if self._seat_empty(row, letter):
            self._seating[row][letter]=passenger
        else:
            raise ValueError(f"Seat {seat} already occupied ")

    # Function to move a passenger to a different seat
    def reallocate_passenger(self,from_seat, to_seat):
        orig_row, orig_letter = self._parse_seat(from_seat)
        dest_row, dest_letter = self._parse_seat(to_seat)
        if self._seat_empty(dest_row, dest_letter):
            self._seating[dest_row][dest_letter], self._seating[orig_row][orig_letter] = self._seating[orig_row][orig_letter], None
        else:
            raise ValueError(f"Seat {to_seat} already occupied")

    def num_available_seats(self):
        seats_not_empties=list()
        available_seats=0
        # Each file of self._seating is a DICTIONARY containing {'A': 'None' 'B': 'David'...} to know if the seat is empty we have to check by its values
        # We create a list of 1s for each empty seat and we sum the list at the end of each iteration
        for i in range(1,len(self._seating)):
            seats_not_empties = [1 for a in self._seating[i].values() if a is None]
            available_seats=available_seats+sum(seats_not_empties)
        print(available_seats)

class Aircraft():
    def __init__(self,registration, model, num_rows, num_seats_per_row):
        self._registration=registration
        self._model=model
        self._num_rows=num_rows
        self._num_seats_per_row=num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model
    
    # Seats in a plane go from A to J without I
    #   A B C D E F G H J
    # 1
    # 2
    def seating_plan(self):
        max_letters="ABCDEFGHJ"
        # we return a tuple (as an double array with files and colums). Each file contains letters from A to num_seats_per_row
        return (range(1, self._num_rows+1),max_letters[0:self._num_seats_per_row])



# Using functions
if __name__ == '__main__':
    f = Flight('SN056',Aircraft("G-EUPT","Airbus 213",4,5))
    print(f.aircraft_model())
    f.allocate_seat("3C","Ana")
    f.allocate_seat("2A","David")
    f.allocate_seat("4B","Juan")
    print(f.print_seating_status())
    #f.allocate_seat("2A","maria")
    f.reallocate_passenger("3C","4A")
    f.reallocate_passenger("3C","4D")
    print(f.print_seating_status())
    f.num_available_seats()