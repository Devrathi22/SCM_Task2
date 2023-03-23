import random
print("Welcome to the HANGMAN! ")
print("Instructions: This is a word guessing game.")
print("You only have 10 chances to guess the word.")
print("If you enter a letter that is not in the word, then a chance will be deducted.")
print("If you repeat a wrong letter again, then also chance will be deducted.")
print("")

list_of_animals=['Ant', 'Bat', 'Bear', 'Bee', 'Beetle', 'Blue', 'whale', 'Buffalo', 'Butterfly', 'Camel', 'Cat', 'Caterpillar', 'Catfish', 'Centipede', 'Chameleon', 'Chicken', 'Cockroach', 'Cow', 'Crab', 'Crane', 'Cricket', 'Crocodile', 'Crow', 'Deer', 'Dog', 'Dolphin', 'Donkey', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'panda', 'Giraffe', 'Goat', 'Goldfish', 'Gorilla', 'Grasshopper', 'Hamster', 'Hippopotamus', 'Honeybee', 'Horse', 'Hummingbird', 'Hyena', 'Jaguar', 'Kangaroo', 'Kingfisher', 'Ladybug', 'Lion', 'Lizard', 'Monkey', 'Mosquito', 'Mouse', 'Octopus', 'Ostrich', 'Owl', 'Panda', 'Parrot', 'Peacock', 'Penguin', 'Pig', 'Pigeon', 'Piranha', 'Prawns', 'Rabbit', 'Rhinoceros', 'Rooster', 'Scorpion', 'Sea', 'horse', 'Seal', 'Sealion', 'Shark', 'Sheep', 'Snake', 'Sparrow', 'Spider', 'Squirrel', 'Swan', 'Tick', 'Tiger', 'Turkey', 'Turtle', 'Vulture', 'Walrus', 'Wolf', 'Wolverine', 'Woodpecker', 'Yak', 'Zebra']
list_of_fruits=['Apple', 'Banana', 'Apricot', 'Avocados', 'Blueberry', 'Blackcurrant', 'Cranberry', 'Cantaloupe', 'DragonFruit', 'Dates', 'Fig', 'Coconut', 'Grapefruit', 'Gooseberries', 'Hazelnut', 'Berries', 'Guava', 'Jackfruit', 'Kiwi', 'Lime', 'Litchi', 'Mango', 'Mulberry', 'Pear', 'Passionfruit', 'Olive', 'Oranges', 'Melon', 'Papaya', 'Peach', 'Pomegranate', 'Pineapple', 'Raspberries', 'Strawberries', 'Tangerine', 'Watermelon']
list_of_vegetables=['Broccoli', 'Cucumber', 'Celery', 'Carrot', 'Springonions', 'Potato', 'Capsicum', 'Turnip', 'Brinjal', 'Peas', 'Onion', 'Cauliflower', 'Beetroot', 'Cabbage', 'Mushroom', 'Spinach', 'Beans', 'Corns', 'Pumpkin', 'Bottlegourd', 'Okra', 'Zucchini', 'Arugula', 'Lettuce', 'Coriander', 'Mint', 'Kale', 'Radish', 'Daikon', 'Sugarbeet', 'Parsnip', 'Horseradish', 'Onion', 'Garlic', 'Leek', 'Fennel']
list_of_plants=[ 'Mushroom', 'Weed', 'Fern', 'Cattail', 'Reed', 'Bamboo',  'Palmtree', 'Bush', 'Corn', 'Grass', 'Algae', 'Oregano', 'basil', 'cilantro', 'ginseng', 'dill', 'chives', 'mint', 'parsley', 'rosemary', 'Rose', 'Chrysanthemum', 'Daisy', 'Jasmine', 'Gerbera', 'Carnation', 'Poppy', 'Tulip', 'Lily', 'Lotus', 'Hibiscus', 'Peony', 'Sunflower', 'Lilac', 'Aster', 'Dandelion', 'Marigold', 'Dahlia']
print("What type of word you want to choose?")
print("For Animals enter A")
print("For Fruits enter F")
print("For Vegetables enter V")
print("For Plants enter P")
user_selection=str(input(""))
if user_selection=='A' or user_selection=='a':
    secret_word=random.choice(list_of_animals)
elif user_selection=='F' or user_selection=='f':
    secret_word=random.choice(list_of_fruits)
elif user_selection=='V' or user_selection=='v':
    secret_word=random.choice(list_of_vegetables)
elif user_selection=='P' or user_selection=='p':
    secret_word=random.choice(list_of_plants)
else:
    print("You have entered an unsupported character")
errors_allowed=10
user_guesses=[]
flag_completed=False
while not flag_completed:
    for letter in secret_word:
        if letter.lower()in user_guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")
    guess=input(f"No. of allowed errors left:{errors_allowed} ,Guess please:")
    user_guesses.append(guess.lower())
    if guess.lower() not in secret_word.lower():
        errors_allowed-=1
        if errors_allowed==0:
            break
    flag_completed=True
    for letter in secret_word:
        if letter.lower() not in user_guesses:
            flag_completed=False
print("")
if flag_completed:
    print(f"CONGRATULATIONS!, YOU WON, THE WORD WAS: {secret_word}!")
else:
    print(f"GAME OVER! You lost!, The word was {secret_word}","Better luck next time.")
