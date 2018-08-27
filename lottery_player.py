#why we need classes

'''
#Solution 1 without using classes

lottery_player = [
    {
    'name': 'Oxford',
    'numbers': (23, 32, 24, 44, 2)
    },
    {
    'name': 'dracus',
    'numbers': (24, 4, 2, 29, 23)
    },
    {
    'name': 'Hans Zimmer',
    'numbers': (23, 1, 4, 44, 2)
    },
    
]

for item in lottery_player:
    print(f"Sum of numbers for {item['name']}: " + str(sum(item['numbers'])))
'''

#solution 2 by using classes
class Player:
    def __init__(self):
        self.name = 'John'
        self.numbers = (12, 13, 13)
    
    def total(self):
        return sum(self.numbers)

player_one = Player()
player_two = Player()