from random import choice

# list of the cars and places that we have.
cars = ['jeep','praid','samand','405 pjo','pjho pars','van','devow',
        'motorcycle','motorboat','bycycle']

places = ['shahrekord','sari','ahwas','shiraz','semnan','tehran',
          'esfhan','karaj','kish','rasht','qom','markazi','tabriz','mashhad',
          'gilan','oromie','ardebil','boshhr']
#f = choice(car)
#print(f"You can rent {f}.")

# car and place that client wants them.
car = input("What car do you want to brow? ")
place =input("Where are you now? ")

# message_messages
messages = f"You can borrow {car.title()} in {place.title()}."
message = f"We can't help you.sorry"

# if test for car
if  car in cars:
    print(messages)
    #print(f"We have {car.title()}.")
if car not in cars:
    print(message)
    #print(f"sorry,wee don't have{car.title()}")

#if test for place
if place in places:
    print(" ")
if place not in places:
    print(" ")

# combines two of the if test.
#if car and place in cars and places:
 #   print(f"We can rent {car} in {place} to you.")
#if car and place not in cars and places:
 #   print(f"Sorry, we don't have this car in that place")

#### it end up having error
