# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def __str__(self):
        return f'name: {self.name}, current_room: {self.current_room}, items: {self.items}'

    def inventory(self):
        return f'{self.items}'
    
    def append_item(self, item):
        self.items.append(item)
        return f'{self.items}'
    
    def remove_item(self, item):
        self.items.remove(item)
        return f'{self.items}'

