import random
print("Welcome to the HANGMAN! ")
print("Instructions: This is a word guessing game.")
print("You only have 10 chances to guess the word.")
print("If you enter a letter that is not in the word, then a chance will be deducted.")
print("If you repeat a wrong letter again, then also chance will be deducted.")
print("")

list_of_animals=['Ant', 'Bat', 'Bear', 'Bee', 'Beetle', 'Blue', 'whale', 'Buffalo', 'Butterfly', 'Camel', 'Cat', 'Caterpillar', 'Catfish', 'Centipede', 'Chameleon', 'Chicken', 'Cockroach', 'Cow', 'Crab', 'Crane', 'Cricket', 'Crocodile', 'Crow', 'Deer', 'Dog', 'Dolphin', 'Donkey', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'panda', 'Giraffe', 'Goat', 'Goldfish', 'Gorilla', 'Grasshopper', 'Hamster', 'Hippopotamus', 'Honeybee', 'Horse', 'Hummingbird', 'Hyena', 'Jaguar', 'Kangaroo', 'Kingfisher', 'Ladybug', 'Lion', 'Lizard', 'Monkey', 'Mosquito', 'Mouse', 'Octopus', 'Ostrich', 'Owl', 'Panda', 'Parrot', 'Peacock', 'Penguin', 'Pig', 'Pigeon', 'Piranha', 'Prawns', 'Rabbit', 'Rhinoceros', 'Rooster', 'Scorpion', 'Sea', 'horse', 'Seal', 'Sealion', 'Shark', 'Sheep', 'Snake', 'Sparrow', 'Spider', 'Squirrel', 'Swan', 'Tick', 'Tiger', 'Turkey', 'Turtle', 'Vulture', 'Walrus', 'Wolf', 'Wolverine', 'Woodpecker', 'Yak', 'Zebra']