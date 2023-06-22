import random
from Card import Card

class Deck:

    def __init__(self):
       self.deckList = []
       self.generateDeck()
       self.shuffle()
      
       
    '''
    shuffles the deck of cards by making 150 random swaps
    '''
    def shuffle(self):
       

        # PSEUDOCODE FOR THIS METHOD
        # repeat the following (indented lines of code) 150 times: use loop

       
                    
        for value in self.deckList:
            # declare a variable called index1 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index1 = random.randint(0, len(self.deckList)-1)
            # declare a variable called index2 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index2 = random.randint(0, len(self.deckList)-1)
            # declare a variable called temp and assign it to the element of the deck of Cards located at index1
            temp = self.deckList[index1]
            # set the element of the deck of Cards located at index1 to the element of the deck located at index2
            self.deckList[index1] = self.deckList[index2]
            # set the element of the deck of Cards located at index2 to temp
            self.deckList[index2] = temp

    



    '''
    generates a deck of un-shuffled cards
    '''
    def generateDeck(self):
        
        #make the list of the suit and value
        theSuit = ["♠", "♣", "♥", "♦"]
        theValue =[1,2,3,4,5,6,7,8,9,10,11,12,13]
        
        #for each in the value
        for suit in theSuit:

            #for each in suit
            for value in theValue :

                #create an instance of Card
                card = Card(suit, value)

                #append to the empty list
                self.deckList.append(card)
        

    '''
    draws a card from the deck and return a card object
    '''
    def drawCard(self):
        #create a card object(make use of the pop) so it leaves the list and becomes a waste
            thedrawnCard= self.deckList.pop(0)

        #return it but it should be smaller each time so -1
            return thedrawnCard
    '''
    returns the number of cards left in the deck as an int
    '''
    def cardsLeft(self):
       #find the length of the deckList now and return it
       theCardsLeft= len(self.deckList)
       return theCardsLeft
      