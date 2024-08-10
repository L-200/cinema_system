#cinema seats system
import time
print('How many rows are there in the room?')
fileiras = int(input())
print('How many seats per row?')
assentos = int(input())
seats_available = fileiras*assentos
cinema = []
for i in range(fileiras):
    fila = []
    for j in range(assentos):
        fila.append(j+1)
    cinema.append(fila)
print('What is the price per reservation?')
price = float(input())
print('What will be the number to stop the system?(type it in the "number of reservations" part to end the program)')
stop = int(input())
def print_(x):  #function to print the cinema 
        for i in range(len(x)):
            print((i+1), x[i])
def reservation_process(x):
    for i in range(x):
        print('Please choose a row and its location')
        row = (int(input('row: '))-1)
        location = (int(input('location: '))-1)
        if cinema[row][location] == 'X':
            print('Sorry, but this place is already reserved!')
            print('Please try again')
            print_(cinema)
            reservation_process(x)
            break #needs to break out of this 'for i' loop
        cinema[row][location] = 'X'
        print_(cinema)
        if awnser1 == 'yes': 
            print('Are you sure this is the seat you want?')
            awnser3 = input().lower()
            if awnser3 == 'yes':
                x -= 1
                print('Okay, your seat has been reserved')
            else:
                cinema[row][location] = location+1
                print("Let's try it again")
                reservation_process(x)  
        else:
            x -= 1
            print('Okay, your seat has been reserved')          
print('Do you want confirmation after each entry?')
awnser1 = input().lower()
#room generated    
while True:
    print_(cinema)
    print('Please enter the corresponding awnser')
    print('How many reservations?')
    number_reservations = int(input('Number of reservations: '))
    if number_reservations == stop: #this allows the owner of the system to shut it down 
        break
    if number_reservations > seats_available:
        print("There aren't enough seats for that!")
        time.sleep(3)
    else:
        price_of_guest = price*number_reservations
        print('That will be: '+ str(price_of_guest)+ ' dollars')
        print('Will you be able to pay?')
        awnser2 = input().lower()
        if awnser2 == 'yes':    
            reservation_process(number_reservations)
        print('Time for the next customer!')
        time.sleep(3)