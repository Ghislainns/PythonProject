german_cars = ['audi','bmw','volkswagen']
italian_cars = ['fiat','alpha-romeo','ferrari']

my_car = 'renault'
print(f"I have a new car, this is a {my_car.title()}.")

if my_car in german_cars:
    print(f"My {my_car.title()} car come from Germany!")
elif my_car in italian_cars:
    print(f"My {my_car.title()} car come from Italia!")
else:
    print("We doesn't know until now from wich country come this car...")
