from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
    'gold': Item('Gold', 'Worth defending your live for!'),
    'sword': Item('Sword', 'Because this world is dangerous!'),
    'food': Item('Food', 'You will need this for survival!')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms
room['foyer'].append_item(item['food'])
room['narrow'].append_item(item['sword'])
room['treasure'].append_item(item['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome to an adventure game!')
player_name = input('Enter your name: ')
player = Player(player_name, room['outside'])
print(f'Welcome, {player_name}! Let the game begin!')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def no_room_error():
        print('Sorry, there is no room in that direction. Try again.')

def item_checker():
    for item in player.current_room.items:
        print(f'In this room there is {item}')

def begin_game():
    print(f'You are in {player.current_room}')
    player_input = ''
    while player_input != int:
        player_input = input('Press "n" for north, "s" for south, "e" for east, "w" for west, "i" or "inventory" to see your items, or "q" to quit: ')

        if player_input == 'n':
            if(player.current_room.n_to != None):
                player.current_room = player.current_room.n_to
                print(f'You are now in {player.current_room}')
                item_checker()
            else:
                no_room_error()
                

        elif player_input == 's':
            if(player.current_room.s_to != None):
                player.current_room = player.current_room.s_to
                print(f'You are now in {player.current_room}') 
                item_checker()                   
            else:
                no_room_error()

        elif player_input == 'e':
            if(player.current_room.e_to != None):
                player.current_room = player.current_room.e_to
                print(f'You are now in {player.current_room}')
                item_checker()
            else:
                no_room_error()
                

        elif player_input == 'w':
            if(player.current_room.w_to != None):
                player.current_room = player.current_room.w_to
                print(f'You are now in {player.current_room}')
                item_checker()
            else:
                no_room_error()

        elif player_input == 'i' or 'inventory':
            print(f'{player.items}')
        
        elif player_input == 'get' or 'take':
            player.get_item(item[item]) 
            item[item].on_take()
            player.current_room.remove_item(item[item])           

        elif player_input == 'drop':
            if player.items < 1:
                print('Nothing to drop...')
            else:
                player.drop_item(item[item])
                item[item].on_drop()
                player.current_room.append_item(item[item])
                

        elif player_input == 'q':
            print(f'Thanks for playing, {player_name}!')
            exit()

        else: 
            print('Please follow the directions...')

begin_game()




        

