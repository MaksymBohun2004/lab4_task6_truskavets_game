# lab4_task6_truskavets_game
A short RPG-ish minigame taking place in Truskavets


The modified module "game" now consists of 6 classes:

Room - the room where action takes place, where the items and the characters are located;
```python
>>> room1 = Room('kitchen')
>>> room1.set_description('A nice room where food is cooked')
>>> room1.get_details() #doctest: +ELLIPSIS
kitchen
--------------------
A nice room where food is cooked
```
Item - usable item that is located in a room and can be taken and used to fight an enemy;
```python
>>> item = Item('Laptop')
>>> item.set_description('Can be used to study programming.')
>>> item.describe()
The [Laptop] is here! - Can be used to study programming.
```
Character - the parent class of classes enemy and friend. Saves the info about a character that is located in a room and can be interacted with;
```python
>>> character = Character('Batman', 'A brave superhero!')
>>> character.describe()
Batman is here!
A brave superhero!
```
Friend(Character) - a character that you don't have to fight, intstead, friend can give you can item for solving a riddle.
```python
>>> friend = Friend('Zelenskiy', 'A gigachad president!')
>>> friend.name
'Zelenskiy'
```
Enemy(Character) - a character that is located in a room, that you have to defeat by fighting with a previously collected item.
```python
>>> enemy = Enemy('putin', 'An ugly ogre')
>>> enemy.set_weakness('Bandera-mobil')
>>> enemy.weakness
'Bandera-mobil'
>>> enemy.fight('Bandera-mobil')
True
```
BossFriend(Character) -     The friend that doesn't care about your riddle-solving skills. Just give the friend your money!
```python
>>> hunter = BossFriend('Hunter', 'An old fat hunter with a rifle and a long mustache.')
>>> hunter.set_demand(500)
```
