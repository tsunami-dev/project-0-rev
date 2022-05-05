def menu():
    print("[1] Option 1 / Start your adventure!")
    print("[0] Option 2/ Quit")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print('welcome to your very own adventure!')
    else:
        print('invalid option')

    
    print("every great story starts with a name!")
    name = input('enter your name: ')
    if name == None:
        name == "Player"
    print (f'ahhh looks like your awake {name} ')
    start = input('well, now that your are up you ready to start? Yes/No ')
    if start == 'yes':
        print('well what are we waiting for lets go')
        settings = input('where should we start the war room or the garden ')
    else:
        print('please you have been sleeping for so long, Ending 1/6')
        quit()

    if settings == 'the war room':
        print('WARRRRRR!!!! you can only solve these issues with our armed forces ')
        response = input (f' {name} you\'re awake! can you please tell these fools the only way to win is to fight not talk! ')
        if response == 'fight':
            print('thank you finally someone with some sense! ') 
        elif response == 'talk':
            print(f'i can\'t believe you! the {name} i knew would never turn down a fight! ')
    else:
        print(f'your not {name}, you get brought to jail Ending 2/6! ')
        quit()
    if settings == 'the garden':   
        print(f'HEY!! {name} it\'s been a long time! ')
        response:str == input (f'have you come to escape your duties again? YES/NO ')
        if response:str == 'YES'
        print (f'same old {name} rather relax then get work done ')
        if response:str == 'NO'
        print('oh! well then let me leave you to it!')
    else:
        ('wait.. who are you.. GUARDS!!!!, you are surrounded no where left to run, Ending 3/6')

#menu()

print('too bad hopefully we will see you soon!')
