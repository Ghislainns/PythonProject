guests = ['Deborah', 'Charlotte', 'Laureline']

for guest in guests:
    print(f"Dear {guest.title()} you are invited to a dinner!")

not_available = guests.pop(1)
print(f"Dear {not_available.title()} I'm sorry to hear that you are not available for this dinner ...")

guests.append('Juliette')

for guest in guests:
    print(f"Dear {guest.title()} you are invited to a dinner!")

print ("Good news, a bigger table is available, we are looking for new guess")

guests.insert(0, 'Manon')
guests.insert(2, "Virginie")
guests.append("Stephanie")

for guest in guests:
    print(f"Dear {guest.title()} you are invited to a dinner!")

print ("Bad news, only 2 persons could be invited")

del guests[2:]

for last_guest in guests:
    print(f"Dear {last_guest.title()} you are still invited...")

print(f"We have now only {len(guests)} guests")

