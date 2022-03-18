import game

shakhtar = game.Room("Shakhtar Sanatorium")
shakhtar.set_description("A health resort sanatorium in Truskavets.")

bandera_street = game.Room("Stepan Bandera Street")
bandera_street.set_description("A calm and peaceful street laying through a residential area.")

franko_street = game.Room("Ivan Franko Street")
franko_street.set_description("An old street completely covered in trees headed towards the central park.")

central_park = game.Room("Central Park.")
central_park.set_description("A busy, but quiet place where people come to play chess or drink mineral water.")

naftusya_source = game.Room("Naftusya source №1")
naftusya_source.set_description("A soviet-looking building in the heart of the park")

shakhtar.link_room(bandera_street, "north")
bandera_street.link_room(shakhtar, "south")
bandera_street.link_room(franko_street, "west")
franko_street.link_room(bandera_street, "east")
central_park.link_room(franko_street, "east")
franko_street.link_room(central_park, "west")
central_park.link_room(naftusya_source, "north")
naftusya_source.link_room(central_park, "south")

frog_king = game.Enemy("Frog King", "A giant smelly frog.")
frog_king.set_conversation("Wag-wag! Give me some Naftusya or I`ll eat you!")
frog_king.set_weakness("caviar")
frog_king.set_bounty(200)
shakhtar.set_character(frog_king)

gopnik = game.Enemy("Gopnik Andriukha", "A bald gapnik in an Adidas costume.")
gopnik.set_conversation("Wassup! Give me a cigarette or i`ll beat you up!")
gopnik.set_weakness("pepper spray")
gopnik.set_bounty(200)
bandera_street.set_character(gopnik)

crazy_grandma = game.Enemy("Crazy grandma", "An old and grumpy grandma that's about to beat you with a stick.")
crazy_grandma.set_conversation("What business do you have walking at my yard?! Get out!")
crazy_grandma.set_weakness("stick")
crazy_grandma.set_bounty(100)
franko_street.set_character(crazy_grandma)

pigeon = game.Enemy("The Unbeatable Pigeon", "This flying fury is almost impossible to catch and defeat.")
pigeon.set_conversation("Catch me if you can, loser! I'll poop all over your house!")
pigeon.set_weakness("hunting rifle")
naftusya_source.set_character(pigeon)
pigeon.set_bounty(1000)

stick = game.Item("stick")
stick.set_description("A simple wooden stick.")
bandera_street.set_item(stick)

caviar = game.Item("caviar")
caviar.set_description('A can of fresh and tasty caviar.')

consultant = game.Friend('Consultant', 'Will help you find your room and provide you with everything needed.')
consultant.set_conversation("Hi! What can I help you with? If you need some caviar, you'll have to solve my quiz!")
consultant.set_quiz("What starts with t, ends with t and is full of t?", "teapot")
consultant.set_item(caviar)

shakhtar.set_friend(consultant)

pepper_spray = game.Item('pepper spray')
pepper_spray.set_description('Ukrainian-manufactured pepper spray that will make your enemies cry!')

policeman = game.Friend('Policemen', 'Will prevent anything illegal from happening')
policeman.set_conversation('Greetings! Policed to meet you! What can I help you with, dear citizen?')
policeman.set_quiz("What number on a police car in America makes people want to steal it?", "911")
policeman.set_item(pepper_spray)

central_park.set_friend(policeman)

hunter_rifle = game.Item("hunting rifle")
hunter_rifle.set_description('An old hunting rifle decorated with wooden carvings.')

hunter = game.BossFriend('Hunter', 'An old fat hunter with a rifle and a long mustache.')
hunter.set_conversation("Ya need a rifle? I ain't no seller, but I can sell ya dat if ya gimme enough loot, old sport!")
hunter.set_demand(500)
hunter.set_item(hunter_rifle)
naftusya_source.set_friend(hunter)

current_room = shakhtar
backpack = []
money = 0

dead = False

while not dead:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    friend = current_room.get_friend()
    if friend is not None:
        friend.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print(f"Hooray, you won the fight! You collected {inhabitant.bounty} coins!")
                    money += inhabitant.bounty
                    print(f"You now have {money} coins!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 4:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "friend":
        if friend is not None:
            friend.talk()
            if friend.question is not None:
                print(friend.question)
                answer = input()
                if answer.lower() == friend.answer:
                    print(f"You got the question right! {friend.name} has given you [{friend.item.get_name()}]!")
                print("You put the " + friend.item.get_name() + " in your backpack")
                backpack.append(friend.item.get_name())
                current_room.set_friend(None)
            elif friend.demand is not None:
                print(f'In order to get {friend.item.get_name()}, you have to pay {friend.name} {friend.demand}!')
                if money < friend.demand:
                    print("You don't have enough money! Come back later!")
                elif money >= friend.demand:
                    print("You have enough money!")
                    print(f'Would you like to pay {friend.demand}?')
                    answer = input("y or n\n>>> ")
                    if answer.lower() == 'y':
                        money -= friend.demand
                    print("You put the " + friend.item.get_name() + " in your backpack")
                    backpack.append(friend.item.get_name())
                    current_room.set_friend(None)
            else:
                print('There are no friends in this room!')

    else:
        print("I don't know how to " + command)
