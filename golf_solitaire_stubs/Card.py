class Card:
    def __init__(self, suit, value):
        #now create the properties
        self.suit = suit
        self.value = value

    #getter for suit
    def getSuit(self):
        return self.suit
    
    #getter for value
    def getValue(self):
        return self.value
    
    #string method of how you want the card to be displayed so number and the suit
    def __str__(self):
        form = str(self.value) + self.suit
        return form
        


        