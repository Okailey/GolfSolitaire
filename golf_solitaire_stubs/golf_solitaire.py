from Card import Card
from Deck import Deck


    
'''
Note: DO NOT MODIFY THIS FUNCTION. If your grid is not displaying properly, check your code first or contact us. 

displays a grid of cards arranged in 7x5 col/row formatted like this:
[   [row1, row2, row3...],  <-col1
    [row1, row2, row3...],  <-col2
    [row1, row2, row3...],  <-col3
    ...
]

params:
    grid - a 2D list in the format shown above

returns:
    None (output from this function is printed)

'''
def displayGrid(grid):

    #generate and display the index header for the grid
    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    #proces through each of the rows in reverse because we need to print top to bottom (ie last index to first)
    for row in range(4, -1, -1):

        #generate the full string for a row before printing it
        rowStr = "|\t"
        for col in range(7):
            #create an index offset so that cards are always aligned at the top
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            #as long as the row index is valid, get the data for that particular card
            if(rowIdx >=0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"
            
            #otherwise print an empty space
            else:
                rowStr += "  \t|\t"
            
        #print the completed row and a row separator
        print(rowStr)
        print()





'''
Initializes a grid of cards for golf solitaire

params:
    deck - an instance of the deck class to draw cards from

returns:
    a 2D list of card objects formatted in a 7x5 configuration for 7 columns and 5 rows
'''
def initGrid(deck):
   #use a nested loop to generate the list
   #get an empty list where they will append to
   theGrid =[]
   #for the columns of the grid in range(7):
   for gridColumn in range(7):
            #another list for the rows since it is a 2D list
            theGridRow =[]
            #for the rows in the grid in range (5):
            for gridRow in range(5):

                #create an instance of the deck so you can draw cards
                card = deck.drawCard()

                #append the rows of the card to thegridrow and append the gridrow to the the grid to form a 2D list
                theGridRow.append(card)
            theGrid.append(theGridRow)
    #now return the grid which showcases the 2D list
   return theGrid

        


'''
Checks whether the grid is empty (ie the grid is a list containing only empty lists). Example is below:

    [ [], [], [], [], [], [], [] ] <--- This grid is empty
    [ [Card, Card], [], [], [Card], [], [], [] ] <--- This grid is NOT empty

params:
    grid - a 2D list in the format shown above

returns:
    True if the grid is empty
    False if the grid is not empty

'''
def checkWin(grid):
    #checks if the grid is empty
    #so iterate through the list which is in a row which is actually the columns for the game
    #  to see if there is an card in it or not
    for theGridrow in grid:
      
      for card in theGridrow:

        #if there is a card in the list
        if card in theGridrow:

            #return false
            return False
    
    #else return true  
    return True
  
    




'''
Calculates the abs between the values of two cards
params:
    card1 - instance of the Card class
    card2 - instance of the Card class

returns:
    the absolute value between the two cards (accounting for A/J/Q/K)

'''
def compareCards(card1, card2):
    #get the absolute value of the two cards when subtracted 
    theAbsoluteVal = abs(card1.getValue() - card2.getValue())
    #return that value
    return theAbsoluteVal



'''
Main game function

params:
    none

returns:
    none

'''
def main():
    deck = Deck()
    grid = initGrid(deck)
    displayGrid(grid)
    wasteCards = []


        # Start the game loop so while it is true true,display the grid and display the waste cards
    while True:
        # Display the grid and waste cards while the game still runs
        displayGrid(grid)
        print("Waste cards:", ", ".join(str(card) for card in wasteCards))

        # Ask the user for their input
        theUserInput = input("What do you want to do? draw/quit/move: ")

        # if they say draw then check if the deck is empty, if it is then print a message saying it is, 
        # if not then append the cards the player draws to the wasteCard list
        if theUserInput == "draw":
           
            if deck.cardsLeft() > 0:
                wasteCards.append(deck.drawCard())
            else:
                print("Sorry! The deck is empty.")
        elif theUserInput == "quit":
            # Exit the game loop by implementing break
            break
        elif theUserInput== "move":
            # if the user says move, then ask which column to move from and if there is nothing in that column, 
            # say it is empty, then continue the game, by popping the input the user gave and then comparing it to the current waste card, if the difference is 1, 
            #  append it to the wasteCard list, else print a message saying you can't move the card

            action = int(input("What column do you want to move from? (0-6): "))

            
            if len(grid[action]) == 0:
                print("The column is empty.")
                continue
            myCard = grid[action].pop(0)

           
            if len(wasteCards) == 0 or compareCards(myCard, wasteCards[-1]) == 1:
               
                wasteCards.append(myCard)
            else:
                print("Hey! that is illegal. You can't move that card.")

        # Check to see if the grid is empty and the player has won, if yes then break the code, 
        # if no then it will start all over again.
        if checkWin(grid):
            print("Congratulations! You have won the game! You're a Champion!!")
            break
        else: 
            displayGrid(grid)
            theUserInput = input("What do you want to do? draw/quit/move: ")


if __name__ == "__main__":
    main()

