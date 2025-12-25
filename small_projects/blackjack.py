import random , sys

# set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print(''' Blackjack by Siberian Huskey
          Rules:
                Try to get as close to 21 without going over.
                Kings, Queens, and Jacks are worth 10 points.
                Aces are worth 1 or 11 points.
                Cards 2 through 10 are worth their face value.
                (H)it to take another card.
                (S)tand to stop taking cards.
                On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
                In case of a tie, the bet is returned to the player.
                The dealer stops hitting at 17.         
          ''')
    money = 5000
    while True:
        if money <= 0:
            print('Thanks for playing')
            sys.exit()
        
        #Player enters his bet for this round
        print('Money' , money)
        bet = getBet(money)

        #Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop() , deck.pop()]
        playerHand = [deck.pop() , deck.pop()]
        
        #handle player actions:
        print('Bet: ' , bet)
        while True:
            displayHands(playerHand , dealerHand , False)
            print()
            
            if getHandValues(playerHand) > 21 :
                break
            
            move = getMove(playerHand , money - bet)
            
            if move == 'D':
                #player is doubling down , he can increase their bet
                additionalBet = getBet(min(bet , (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet : ' , bet)
                
            if move in ('H' , 'D'):
                newCard = deck.pop()
                rank , suit = newCard
                print('You drew a {} of {}'.format(rank , suit))
                playerHand.append(newCard)
                              
                if getHandValues(playerHand) > 21:
                    continue
            
            if move in ('S' , 'D'):
                break
                
        if getHandValues(playerHand) <= 21:
            while getHandValues(dealerHand) < 17 :
                print('Dealer hits....')
                dealerHand.append(deck.pop())
                displayHands(playerHand , dealerHand , False)
                
                if getHandValues(dealerHand) > 21:
                    break
                input('Press enter to continue')
                print('\n\n')
                
                displayHands(playerHand , dealerHand , True)
                
                playerValue = getHandValues(playerHand)
                dealerValue = getHandValues(dealerHand)
                
                if dealerValue > 21:
                    print('You win $${}'.format(bet))
                    money += bet
                elif(playerValue > 21) or (playerValue < dealerValue):
                    print('You have lost....')
                    money -= bet
                elif playerValue > dealerValue:
                    print('You win $${}'.format(bet))
                    money += bet
                elif playerValue == dealerValue:
                    print('Nobody wins, lets play again')
                                    
                input('Press Enter to continue')
                print('\n\n')
            
                
    

def getBet(maxBet):
    """_summary_ 
    Ask player how much they want to bet for this round.
    Keep asking until they enter a valid amount.
    Args:
        maxBet (_type_): amount in integer
    """
    while True:
        print("How much do you want to bet? (1 - {} , or QUIT)".format(maxBet))
        bet = input('>> ').upper().strip()
        if bet == 'QUIT':
            print('Thank\'\s for playin')
            sys.exit ()
            
        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    """_summary_
    Returns a list of (rank , suit) tuples for all 52 cards.
    A standard 52-card French deck divides the cards into four suits
    """
    deck = []
    for suit in(HEARTS , DIAMONDS , SPADES , CLUBS):
        for rank in range(2 , 11):
            deck.append((str(rank) , suit))     #adds the numbered cards
        for rank in ('J' ,'Q' ,'K' ,'A'):
            deck.append((rank , suit))          #adds the face and ace cards
        random.shuffle(deck)
        return deck          

def displayHands(playerHands , dealerHand, showdealerHand):
    """_summary_
    Show the player's and dealer's cards. 
    Hide the dealer's first card , if showDealerHand is False
    Args:
        playerHands (_type_): player's cards.
        dealerHand (_type_): dealer's cards.
        showdealerHand (_type_): True or False
    """
    print()
    if showdealerHand:
        print('DEALER: ' , getHandValues(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # hide dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
        displayCards(playerHands)
        
    

def getHandValues(cards):
    """_summary_
    Returns the value of the cards.
    Face cards are worth 10 , aces are worth 11 or 1 
    Args:
        cards (_type_): card from 1 to K
    """
    value = 0
    numberOfAces = 0
    # adds the value for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K' , 'Q' , 'J'):
            value += 10
        else:
            value += int(rank)
            
    # adds the value for the aces:
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10    
    return value    


def displayCards(cards):
    """
    Display all the cards in the card list.

    Args:
        cards (_type_): list of cards
    """
    rows = ['' , '' , '' , ''] # the text to display on each row
    for i , card in enumerate(cards):
        rows[0] +=  ' __ ' # prints the top of the card  
        if card == BACKSIDE:
            # prints a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # prints a card's front:
            rank , suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2 , '_'))
            
    for row in rows:
        print(row)


def getMove(playerHand , money):
    """_summary_
    Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D' for double down.
    Args:
        playerHand (_type_): player's cards
        money (_type_): player's money
    """
    while True:
        moves = ['(H)it' , '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        # gets player's move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('S' , 'H'):
            return move     # Player has entered a valid move.
        if move == 'D':
            return          # Player has entered a valid move.

if __name__ == '__main__':
    main()
    