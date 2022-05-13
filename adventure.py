import pymongo
from pymongo import MongoClient 
import json 
import re 
##the lines seting up the basic CRUD Operations

try: 
    client = pymongo.MongoClient(host="localhost",port=27017)
    db = client["Adventure0"] 
    Collection = db["demo_collection"]

except Exception:
    print("Error:" + Exception)


def menu():
    print("[1] Option 1 / Start your adventure!")
    print("[2] Option 2 / View Data")
    print("[3] Option 3 / Delete Data")
    print("[0] Option 0 / Quit")
#defining the properties of the menu and all inupt instruions listed in "[]"
menu()
option = int(input("Enter your option: "))
#remove = str(input("user_name"))

while option != 0:
    if option == 1:
        print('welcome to your very own adventure!')
    
    if option == 2:
        print("ahh you want to look in to past travlers!")
        adv = Collection.find()
        for x in adv:
            print (x)
        quit()
        #this would be our Read Operation in CRUD
    if option == 3:
        print("What!! you dare tamper with the anticent scrolls of history?")
        remove = input("user_name ") 
        Collection.delete_one({"user_name":remove})
        print("what have you done!! that was a story of legend")
        quit()
        #this would be our Delete Operation in CRUD
    print("every great story starts with a name!")
    name = input('enter your name: ')
    Collection.insert_one({"user_name":name})
    #this would be our Create Operation in CRUD
    if name == None:
        name == "Player"
    print (f'ahhh looks like your awake {name} ')
    start = input('well, now that your are up you ready to start? Yes/No ')
    if start == 'yes':
        print('well what are we waiting for lets go')
        settings = input('where should we start the war room or the garden ')
    else:
        print('please you have been sleeping for so long, Ending 1/9')
        Collection.update_one({"user_name":name},{"$set": {"progress": "ending 1/9"} })
        quit()
        #one of many diffrent Updates with the Crud Operation

    if settings == 'the war room':
        print('WARRRRRR!!!! you can only solve these issues with our armed forces ')
        response = input (f' {name} you\'re awake! can you please tell these fools the only way to win is to fight not talk! ')
        if response == 'fight':
            print('thank you finally someone with some sense! since your ready how about we talk about our plan of attack ') 
            transport = input('a map sits in front of you, would you want to take to the frontline or come up the rear ')
            if transport == 'the frontline':
                print('you and your troops fall without even touching the border, Ending 2/9')
                Collection.update_one({"user_name":name},{"$set": {"progress": "ending 2/9"} })
                quit()

            if transport == 'the rear':
                print('you took over the base camp but lost everything in the process, Ending 3/9')
                Collection.update_one({"user_name":name},{"$set": {"progress": "ending 3/9"} })
                quit()

        if response == 'talk':
            print(f'i can\'t believe you! the {name} i knew would never turn down a fight! Ending 4/9')
            Collection.update_one({"user_name":name},{"$set": {"progress": "ending 4/9"} })
            quit()
        else:
            print(f'your not {name}, you get brought to jail Ending 5/9! ')
            Collection.update_one({"user_name":name},{"$set": {"progress": "ending 5/9"} })
            quit()

    if settings == 'the garden':   
        print(f'HEY!! {name} it\'s been a long time! ')
        response:str = input (f'have you come to escape your duties again? YES/NO ')
        if response == 'YES':
            print (f'same old {name} rather relax then get work done ')
        transport = input('you fell asleep, you wake to the cool breeze of night, do you stay or go inside ')
        if transport == 'stay':
            print('you start to get hungry, but when you go to the door its locked, Ending 6/9')
            Collection.update_one({"user_name":name},{"$set": {"progress": "ending 6/9"} })
            quit() 
        if transport == 'go inside':
            print('you go inside and lock yourself in the room to prepare for another day of doing nothing, Ending 7/9')
            Collection.update_one({"user_name":name},{"$set": {"progress": "ending 7/9"} })
            quit()

        if response == 'NO':
            print('oh! well then let me leave you to it!, Ending 8/9')
        Collection.update_one({"user_name":name},{"$set": {"progress": "ending 8/9"} })
        quit()
    else:
        print('wait.. who are you.. GUARDS!!!!, you are surrounded no where left to run, Ending 9/9')
        Collection.update_one({"user_name":name},{"$set": {"progress": "ending 9/9"} })
        quit()

#menu()
#to avoid menu loop

print('too bad hopefully we will see you soon!')
