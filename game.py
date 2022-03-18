class Room:
    """
    Saves info about a room
    """
    def __init__(self, name):
        """
        Saves the name about info
        >>> room = Room('kitchen')

        >>> room.name
        'kitchen'
        """
        self.name = name
        self.description = None
        self.linked_rooms = []
        self.character = None
        self.item = None
        self.friend = None

    def set_description(self, description):
        """
        Saves a room's description
        >>> room = Room('kitchen')
        >>> room.set_description('A nice room where food is cooked')
        >>> room.description
        'A nice room where food is cooked'
        """
        self.description = description

    def link_room(self, room, direction):
        """
        Links two rooms together
        >>> room1 = Room('kitchen')
        >>> room2 = Room('Dining Room')
        >>> room1.link_room(room2, 'south')
        >>> room1.linked_rooms #doctest: +ELLIPSIS
        [(<__main__.Room object at...
        """
        self.linked_rooms.append((room, direction))

    def get_details(self):
        """
        Returns the details about the room
        >>> room1 = Room('kitchen')
        >>> room1.set_description('A nice room where food is cooked')
        >>> room1.get_details() #doctest: +ELLIPSIS
        kitchen...
        """
        info = f"{self.name}\n\
--------------------\n\
{self.description}"
        for room in self.linked_rooms:
            room_info = f"The {room[0].name} is {room[1]}."
            info += '\n' + room_info
        print(info)

    def move(self, command):
        """
        Moves the character to another room
        >>> room1 = Room('kitchen')
        >>> room2 = Room('Dining Room')
        >>> room1.link_room(room2, 'south')
        >>> room1.move('south') #doctest: +ELLIPSIS
        <__main__.Room object at...
        """
        for room in self.linked_rooms:
            if command in room:
                return room[0]

    def set_character(self, character):
        """
        Sets the character located in the room
        >>> room1 = Room('kitchen')
        >>> room1.set_character('John')
        >>> room1.character
        'John'
        """
        self.character = character

    def set_item(self, item):
        """
        Sets an item located in the room
        >>> room1 = Room('kitchen')
        >>> room1.set_item('Ball')
        >>> room1.item
        'Ball'
        """
        self.item = item

    def get_character(self):
        """
        Returns the character located in the room
        >>> room1 = Room('kitchen')
        >>> room1.set_character('John')
        >>> room1.get_character #doctest: +ELLIPSIS
        <bound method Room.get_character of <__main__.Room object at...
        """
        return self.character

    def get_item(self):
        """
        Returns the item located in the room
        >>> room1 = Room('kitchen')
        >>> room1.set_item('Ball')
        >>> room1.get_item #doctest: +ELLIPSIS
        <bound method Room.get_item of <__main__.Room object at...
        """
        return self.item

    def set_friend(self, friend):
        """
        Sets a friend in the room
        >>> room1 = Room('kitchen')
        >>> room1.set_friend('John')
        """
        self.friend = friend

    def get_friend(self):
        """
        Returns the name of a friend
        >>> room1 = Room('kitchen')
        >>> room1.set_friend('John')
        >>> room1.get_friend() #doctest: +ELLIPSIS
        'John'
        """
        return self.friend


class Item:
    """
    Saves the info about an item
    """
    def __init__(self, name):
        """
        Saves the info about an item
        >>> item = Item('Laptop')
        >>> item.name
        'Laptop'
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Sets the description of an item
        >>> item = Item('Laptop')
        >>> item.set_description('Can be used to study programming.')
        >>> item.description
        'Can be used to study programming.'
        """
        self.description = description

    def get_name(self):
        """
        Returns the name of the item
        >>> item = Item('Laptop')
        >>> item.get_name()
        'Laptop'
        """
        return self.name

    def describe(self):
        """
        Returns the description of an item
        >>> item = Item('Laptop')
        >>> item.set_description('Can be used to study programming.')
        >>> item.describe()
        The [Laptop] is here! - Can be used to study programming.
        """
        print(f"The [{self.name}] is here! - {self.description}")


class Character:
    """
    Saves the info about a character
    """
    def __init__(self, name, description):
        """
        Saves the info about a character
        >>> character = Character('Batman', 'A brave superhero!')
        >>> character.name
        'Batman'
        """
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        """
        >>> character = Character('Batman', 'A brave superhero!')
        >>> character.describe()
        Batman is here!
        A brave superhero!
        """
        print(f"{self.name} is here!\n{self.description}")

    def set_conversation(self, coversation):
        """
        Saves the conversation of a friend
        >>> character = Character('Batman', 'A brave superhero!')
        >>> character.set_conversation('I will demolish the russian army!')
        """
        self.conversation = coversation

    def talk(self):
        """
        Return the conversation of a friend
        >>> friend = Character('Zelenskiy', 'A gigachad president!')
        >>> friend.set_conversation('I will demolish the russian army!')
        >>> friend.talk()
        [Zelenskiy says]: I will demolish the russian army!
        """
        print(f"[{self.name} says]: {self.conversation}")


class Friend(Character):
    """
    Saves the info about a friend
    """
    def __init__(self, name, description):
        """
        Saves the info about a friend
        >>> friend = Friend('Zelenskiy', 'A gigachad president!')
        >>> friend.name
        'Zelenskiy'
        """
        super().__init__(name, description)
        self.conversation = None
        self.item = None
        self.question = None
        self.answer = None

    def set_item(self, item):
        """
        Sets the item that the friend is going to carry
        >>> friend = Friend('Zelenskiy', 'A gigachad president!')
        >>> item = Item('Book')
        >>> friend.set_item(item)
        """
        self.item = item

    def set_quiz(self, question, answer):
        """
        Set a question and an answer for player to answer.
        >>> friend = Friend('Zelenskiy', 'A gigachad president!')
        >>> friend.set_quiz('What starts with t, end with t and is full of t?', 'teapot')
        >>> friend.question
        'What starts with t, end with t and is full of t?'
        >>> friend.answer
        'teapot'
        """
        self.question = question
        self.answer = answer

    def get_item(self):
        """
        Return the name of the item a friend is carrying.
        >>> friend = Friend('Zelenskiy', 'A gigachad president!')
        >>> item = Item('Book')
        >>> friend.set_item(item)
        >>> friend.get_item()
        'Book'
        """
        name = self.item.get_name()
        return name

    def describe(self):
        """
        >>> character = Character('Batman', 'A brave superhero!')
        >>> character.describe()
        Batman is here!
        A brave superhero!
        """
        print(f"*FRIEND*{self.name} is here!\n{self.description}")


get_defeated = 0


class Enemy(Character):
    """
    Saves info about an enemy
    """
    def __init__(self, name, description):
        """
        Saves info about an enemy
        >>> enemy = Enemy('putin', 'An ugly ogre')
        >>> enemy.description
        'An ugly ogre'
        """
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None
        self.bounty = None

    def get_defeated(self):
        """
        Saves the number of enemies defeated
        >>> enemy = Enemy('putin', 'An ugly ogre')
        >>> type(enemy.get_defeated()) == int
        True
        """
        global get_defeated
        return get_defeated

    def set_weakness(self, weakness):
        """
        Saves the weakness of a character
        >>> enemy = Enemy('putin', 'An ugly ogre')
        >>> enemy.set_weakness('Bandera-mobil')
        >>> enemy.weakness
        'Bandera-mobil'
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Checks if the weapon is matching the enemie's weakness
        >>> enemy = Enemy('putin', 'An ugly ogre')
        >>> enemy.set_weakness('Bandera-mobil')
        >>> enemy.weakness
        'Bandera-mobil'
        >>> enemy.fight('Bandera-mobil')
        True
        """
        if fight_with == self.weakness:
            global get_defeated
            get_defeated += 1
            return True
        return False

    def describe(self):
        """
        >>> character = Character('Batman', 'A brave superhero!')
        >>> character.describe()
        Batman is here!
        A brave superhero!
        """
        print(f"*ENEMY*{self.name} is here!\n{self.description}")

    def set_bounty(self, bounty):
        self.bounty = bounty

    def get_bounty(self):
        return self.bounty


class BossFriend(Friend):
    """
    The friend that doesn't care about your riddle-solving
    skills. Just give the friend your money!
    """
    def __init__(self, name, description):
        """
        Saves the info about the boss friend
        >>> hunter = BossFriend('Hunter', 'An old fat hunter with a rifle and a long mustache.')
        """
        super().__init__(name, description)
        self.conversation = None
        self.item = None
        self.question = None
        self.answer = None
        self.demand = None

    def set_demand(self, demand):
        """
        Sets the amount of money you need to give
        to the friend to get the item
        >>> hunter = BossFriend('Hunter', 'An old fat hunter with a rifle and a long mustache.')
        >>> hunter.set_demand(500)
        """
        self.demand = demand
