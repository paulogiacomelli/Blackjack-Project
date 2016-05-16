# Paulo Giacomelli
# BlackJack Game - Project 2
# 12/10/2015

from graphics import *
from CardDeck import *

win = GraphWin("Blackjack Game", 900, 500)
win.setBackground(color_rgb(34,139,34))

# function to create button
def buttonCreation(text, xCord, yCord, win):
    button = Text(Point(xCord, yCord), text)
    button.setTextColor("white")
    button.setFace("arial")
    button.setSize(12)
    button.draw(win)
    return button

# Creates the deck that so I can import the images correctly to the screen
def deck():
    return [ suit + rank for suit in "cdhs" for rank in "123456789tjqk" ]

# Randomize the cards picked from the deck
def shuffleCards(cardList):
    cardList1 = cardList[:]
    random.shuffle(cardList1)
    return cardList1

# Pick cards from the list.
def pickCards(cardList):
    return cardList[:1]

# Function that computes the player/computer hand
def computeScore(hand):
    total = 0

    if hand == ['cj'] or hand == ['cq'] or hand == ['ck'] or hand == ['dj'] or hand == ['dq'] or hand == ['dk'] or hand == ['sj'] or hand == ['sq'] or hand == ['sk'] or hand == ['hj'] or hand == ['hq'] or hand == ['hk'] or hand == ['ct'] or hand == ['dt'] or hand == ['st'] or hand == ['ht']:
        total += 10
    if hand == ['c2'] or hand == ['d2'] or hand == ['s2'] or hand == ['h2']:
        total += 2
    if hand == ['c3'] or hand == ['d3'] or hand == ['s3'] or hand == ['h3']:
        total += 3
    if hand == ['c4'] or hand == ['d4'] or hand == ['s4'] or hand == ['h4']:
        total += 4
    if hand == ['c5'] or hand == ['d5'] or hand == ['s5'] or hand == ['h5']:
        total += 5
    if hand == ['c6'] or hand == ['d6'] or hand == ['s6'] or hand == ['h6']:
        total += 6
    if hand == ['c7'] or hand == ['d7'] or hand == ['s7'] or hand == ['h7']:
        total += 7
    if hand == ['c8'] or hand == ['d8'] or hand == ['s8'] or hand == ['h8']:
        total += 8
    if hand == ['c9'] or hand == ['d9'] or hand == ['s9'] or hand == ['h9']:
        total += 9
    if hand == ['c1'] or hand == ['d1'] or hand == ['s1'] or hand == ['h1']:
        if total > 21:
         total+= 1
        else:
         total+= 11
    return total


#################################### BEGIN THE GAME ######################################
def main():

    # Tittle of the game.
    title = Text(Point(450, 30), "Welcome to BLACKJACK!!")
    title.setTextColor("orange")
    title.setFace("courier")
    title.setStyle("bold italic")
    title.setSize(30)
    title.draw(win)

    # Play button
    play = Rectangle(Point(40, 50), Point(100,90))
    play.setFill(color_rgb(255,140,0))
    play.draw(win)

    playButton = buttonCreation("Play",70,70,win)

    # Instructions button.
    rules = Rectangle(Point(40, 100), Point(100,140))
    rules.setFill(color_rgb(255,140,0))
    rules.draw(win)
    rulesButton = buttonCreation('Rules',70,120,win)

    # Quit button.
    quit = Rectangle(Point(40, 150), Point(100,190))
    quit.setFill(color_rgb(255,140,0))
    quit.draw(win)
    quitButton = buttonCreation('Quit',70,170,win)

    warning = Text(Point(450,490), "Do not click the window twice. Only use the buttons to interact with program."
                                    " Rememeber: This is a Beta program in testing.")
    warning.setSize(10)
    warning.setStyle("italic")
    warning.setTextColor("white")
    warning.draw(win)


    # Making px and py coordinates to create conditionals statements for button
    point = win.getMouse()
    px = point.getX()
    py = point.getY()

    # when play button is clicked, moves to next screen to play the game.
    if px > 40 and px < 100 and py > 50 and py < 90:
        rules.undraw()
        rulesButton.undraw()
        # Algorithm that gives the player and the computer their random cards and check who wins.
        win.setBackground(color_rgb(46,139,87))
        while True:

            # Create the first card of the player.
            playerCard = deck()
            playerCard = shuffleCards(playerCard)
            playerCard = pickCards(playerCard)

            # Create the second card of the player
            playerCard2 = deck()
            playerCard2 = shuffleCards(playerCard2)
            playerCard2 = pickCards(playerCard2)

            # Runs through a loop to create an image of whatever card is picked for the player
            for card in playerCard:
                img = Image(Point(400, 400), "Images/"+card+".gif")
                img.draw(win)
            for card in playerCard2:
                img2 = Image(Point(450, 400), "Images/"+card+".gif")
                img2.draw(win)

            # Create the first card of the computer.
            computerCard = deck()
            computerCard = shuffleCards(computerCard)
            computerCard = pickCards(computerCard)

            # Create the second card of the computer
            computerCard2 = deck()
            computerCard2 = shuffleCards(computerCard2)
            computerCard2 = pickCards(computerCard2)

            # Runs through a loop to create an image of whatever card is picked for the computer
            for card in computerCard:
                computerImg = Image(Point(400, 100), "Images/"+card+".gif")
                computerImg.draw(win)

            for card in computerCard2:
                computerImg2 = Image(Point(450, 100), "Images/"+card+".gif")
                computerImg2.draw(win)

            hideCard = Image(Point(450,100), "Images/b1fv.gif")
            hideCard.draw(win)


            # Draw hit button and stand button.

            hit = Rectangle(Point(600, 200), Point(650,250))
            hit.setFill(color_rgb(0,100,0))
            hit.draw(win)
            hitButton = buttonCreation('Hit',625,225,win)

            stand = Rectangle(Point(670, 200), Point(720,250))
            stand.setFill(color_rgb(139,0,0))
            stand.draw(win)
            standButton = buttonCreation('Stand',695,225,win)


#### START GAME ####

            # get the mouse attention
            point = win.getMouse()
            px = point.getX()
            py = point.getY()

            # compute players hand.
            card1 = computeScore(playerCard)
            card2 = computeScore(playerCard2)
            playerHand = card1+card2

            # total Player hand.
            totalPlayer = playerHand

            # Computes computer hand.
            computerCard1 = computeScore(computerCard)
            computerCard2 = computeScore(computerCard2)
            computerHand = computerCard1+computerCard2

            # totals computer's hand
            totalComputer = computerHand

            # when hit is selected
            if px > 600 and px < 650 and py > 200 and py < 250:
                hideCard.undraw()

                # draws an extra random card from deck.
                hitCard = deck()
                hitCard = shuffleCards(hitCard)
                hitCard = pickCards(hitCard)

                # compute the value of the card and adds to the previous cards.
                card3 = computeScore(hitCard)
                totalPlayer += card3

                # draws the image
                for card in hitCard:
                    hitImg = Image(Point(500, 400), "Images/"+card+".gif")
                    hitImg.draw(win)

                if totalPlayer > 21:
                    player1Busted = Text(Point(400,240), "Player: BUSTED!!")
                    player1Busted.setStyle("bold")
                    player1Busted.setSize(16)
                    player1Busted.draw(win)
                    break

                elif totalPlayer == 21:
                    player1BlackJack = Text(Point(450,250), "Player: BLACKJACK!!")
                    player1BlackJack.setStyle("bold")
                    player1BlackJack.setSize(16)
                    player1BlackJack.draw(win)
                    break

                elif totalComputer > 21:
                    computerBusted = Text(Point(450,240), "Computer: BUSTED!!")
                    computerBusted.setStyle("bold")
                    computerBusted.setSize(16)
                    computerBusted.draw(win)
                    break

                elif totalComputer == 21:
                    computerBlackJack = Text(Point(450,240), "Computer: BLACKJACK!!")
                    computerBlackJack.setStyle("bold")
                    computerBlackJack.setSize(16)
                    computerBlackJack.draw(win)
                    break

                elif totalPlayer > totalComputer and totalPlayer < 21:
                    player1Wins = Text(Point(450,250),"Player: Wins!!")
                    player1Wins.setStyle("bold")
                    player1Wins.setSize(16)
                    player1Wins.draw(win)

                elif totalComputer > totalPlayer and totalComputer < 21:
                    computerWins = Text(Point(450,250),"Computer: Wins!!")
                    computerWins.setStyle("bold")
                    computerWins.setSize(16)
                    computerWins.draw(win)

                elif totalComputer == totalPlayer:
                    playersDraw = Text(Point(450,250),"It is a draw!!")
                    playersDraw.setStyle("bold")
                    playersDraw.setSize(16)
                    playersDraw.draw(win)

            # when stand is selected:
            elif px > 670 and px < 720 and py > 200 and py < 250:
                hideCard.undraw()

                if totalPlayer > 21:
                    player1Busted = Text(Point(400,240), "Player: BUSTED!!")
                    player1Busted.setStyle("bold")
                    player1Busted.setSize(16)
                    player1Busted.draw(win)
                    break

                elif totalPlayer == 21:
                    player1BlackJack = Text(Point(450,250), "Player: BLACKJACK!!")
                    player1BlackJack.setStyle("bold")
                    player1BlackJack.setSize(16)
                    player1BlackJack.draw(win)
                    break

                elif totalComputer > 21:
                    computerBusted = Text(Point(450,240), "Computer: BUSTED!!")
                    computerBusted.setStyle("bold")
                    computerBusted.setSize(16)
                    computerBusted.draw(win)

                elif totalComputer == 21:
                    computerBlackJack = Text(Point(450,240), "Computer: BLACKJACK!!")
                    computerBlackJack.setStyle("bold")
                    computerBlackJack.setSize(16)
                    computerBlackJack.draw(win)

                elif totalPlayer > totalComputer and totalPlayer < 21:
                    player1Wins = Text(Point(450,250),"Player: Wins!!")
                    player1Wins.setStyle("bold")
                    player1Wins.setSize(16)
                    player1Wins.draw(win)

                elif totalComputer > totalPlayer and totalComputer < 21:
                    computerWins = Text(Point(450,250),"Computer: Wins!!")
                    computerWins.setStyle("bold")
                    computerWins.setSize(16)
                    computerWins.draw(win)

                elif totalComputer == totalPlayer:
                    playersDraw = Text(Point(450,250),"It is a draw!!")
                    playersDraw.setStyle("bold")
                    playersDraw.setSize(16)
                    playersDraw.draw(win)
            break # stop drawing pictures

    # when instructions is clicked, show instructions
    elif px > 40 and px < 100 and py > 100 and py < 140:
        playButton.undraw()
        play.undraw()
        instructions = Text(Point(450, 240), "This is a very simple blackjack game\n\n"
            "1. in the game the cards have the following values:\n\n"
            "2. ace: 11 or 1.\n\n"
            "3. J, Q, K are 10.\n\n"
            "4. Cards 2 - 10 are face value.\n\n"
            "5. You will start with two cards and add them up.\n\n"
            "6. If you have 21, then you have the best score, a blackjack.\n\n"
            "7. If you have between 18 and 21, you should stand (no more cards).\n\n"
            "8. If you have less then 18, you can hit (one more card).\n\n"
            "10. Once you stand the computer plays.\n\n"
            "11. The better score not exceeding 21 wins.\n\n"
            "12. Equal scores is a draw (no winner).\n\n"
            "13. Any score over 21 is a bust (busted player loses, both bust --> no winner).\n\n"
            "14. Casino blackjack games have additional options and rules.")
        instructions.setTextColor("black")
        instructions.setSize(12)
        instructions.draw(win)

    elif px > 40 and px < 100 and py > 150 and py < 200:
        win._onClick(exit())

    win.getMouse()

if __name__ == "__main__":
    main()
