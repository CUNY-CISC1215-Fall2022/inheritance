# This file contains the TableTennisPlayer classes we designed in class.
# This approach uses extending to enhance the behavior of the TableTennisPlayer class.

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
        # Here, we use the super() function to briefly return to the TableTennisPlayer class.
        # We call the TableTennisPlayer __init__ method, allowing us to defer to the parent
        # class to perform initializations before adding our own.
        super().__init__(name, has_table)
        self.rating = rating
    
    def __str__(self):
        # We call the TableTennisPlayer __str__ method, allowing us to defer to the parent
        # class to construct the majority of the output string before adding our own information
        output = super().__str__()
        output = output + " Rating: " + str(self.rating)
        return output



player1 = TableTennisPlayer("Matt", True)
player2 = RatedPlayer("Alice", True, 300)

print(player1)
print(player2)