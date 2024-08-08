#cinema seats system
import time
print('How many rows are there in the room?')
fileiras = int(input())
print('How many seats per row?')
assentos = int(input())
cinema = []
for i in range(fileiras):
    fila = []
    for j in range(assentos):
        fila.append(j+1)
    cinema.append(fila)
print('What is the price per reservation?')
price = float(input())
def print_(x):
        for i in range(len(x)):
            print((i+1), x[i])
def reservation_process(x):
    tickets_remaining = number_reservations
    for i in range(x):
        row = (int(input('row: '))-1)
        location = (int(input('location: '))-1)
        if cinema[row][location] == 'X':
            print('Sorry, but this place is already reserved!')
            print('Please try again')
            reservation_process(tickets_remaining)
            break
        cinema[row][location] = 'X'
        print_(cinema)
        if awnser1 == 'yes': 
            print('Are you sure this is the seat you want?')
            awnser2 = input().lower()
            if awnser2 == 'yes':
                tickets_remaining -= 1
                print('Okay, your seat has been reserved')
                
            else:
                cinema[row][location] = location+1
                print("Let's try it again")
                reservation_process(tickets_remaining)            
#room generated    
print('Do you want confirmation after each entry?')
awnser1 = input().lower()
while True:
    print_(cinema)
    print('Please enter the corresponding awnser')
    print('How many reservations?')
    number_reservations = int(input('Number of reservations: '))
    if number_reservations == 1000: #this allows the owner of the system to shut it down by entering 1000
        break
    reservation_process(number_reservations)
    price_of_guest = price*number_reservations
    print('That will be: '+ str(price_of_guest)+ ' dollars')
    time.sleep(5)
print_(cinema)