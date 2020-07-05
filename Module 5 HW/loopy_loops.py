#Pokemon Tuples

if __name__ == "__main__":

    pokemon_1 = ['Pikachu', 'Charmander', 'Bulbasaur']
    starter1 = {'Pikachu'}
    starter2 = {'Charmander'}
    starter3 = {'Bulbasaur'}

    print('Pikachu' in pokemon_1)
    

#Tuple for John

    name = "John"
    my_tuple = tuple(name)
    print(my_tuple)

    i = 0
    while i < len(name):
        print(name[i])
        i += 1

# For Loops in range

    for i in range(2, 11):
        print(i)

# While Loops

    num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

    i = 1
    while i < len(num):
        print(num[i])
        i += 1           


# For loop over string

    sentence = ('This is a simple string')


    for character in sentence:
        print(character)

# Nested for loop

    for i in range(3):
        print('This,', 'is,', 'a,', 'simple,', 'set')
