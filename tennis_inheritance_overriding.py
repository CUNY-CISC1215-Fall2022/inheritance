# This file contains the TableTennisPlayer classes we designed in class.
# This approach uses overriding to enhance the behavior of the TableTennisPlayer class.

class TableTennisPlayer:
    def __init__(self, name, has_table):
        self.name = name
        self.has_table = has_table

    def __str__(self):
        string = f"Name: {self.name}"

        if self.has_table:
            string = string + " (owns table)"

        return string


class RatedPlayer(TableTennisPlayer):
    def __init__(self, name, has_table, rating):
        # Here, we override the TableTennisPlayer __init__() method.
        # This allows us to fully customize its behavior, but we also have
        # to reimplement any behaviors from the parent __init__() we want to keep.
        self.name = name
        self.has_table = has_table
        self.rating = rating
    
    def __str__(self):
        # We override the __str__() method too. Again, this requies us to
        # reimplement all functionality we want to keep from the parent
        # __str__() method.
        string = f"Name: {self.name}"

        if self.has_table:
            string = string + " (owns table)"     
        
        string = string + " Rating: " + str(self.rating)
        return string



player1 = TableTennisPlayer("Matt", True)
player2 = RatedPlayer("Alice", True, 300)

print(player1)
print(player2)