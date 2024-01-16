# create a homepage menu
# menu prompted at first needs to give option for login, register, and Guest play, (exit)
database = []
balance = 0
loan = 0
loggedin = False



def homepage_menu():
    print("            !Python Casino!")
    print("------------------------------------------")
    print("| 1.    Register   | 2.     Login       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("|               3. Guest                   |")
    print("|---------------------------------------|")
    print("----------------4. Exit--------------------")


# Register function
# prompt user to make a username and password 
def register(name, password, database):
    name = input("Enter username choice: ") # username of registered player
    password = input("Enter Password") # usernames password
    if name in database:
        print("Name taken try again")
    if len(password) < 6: # password of at least 6 characters
        print("Password should be at least 6 characters")
    else:
        database[name] = password  
        print(name, "Has been registered")
    return name


# login will put reg user into the next menu after correct name and password

def login(name, password, database):   # Login function 
    if name in database and database[name] == password:   # need to be prompted to put in your registered name and password
        print("Welcome", name,".")
        return name
    elif name in database:
        print("Incorrect password try again")
        return 
    else:
        print("User not registered, Please register!")  # if tried  to login with out reg will be prompted to register
        return 



# Guest menu
# 1. deposit                                2. withdraw

#3. play                                     4.exit 


def guestpage_menu():
    print("!|                Guest Player                        |!")
    print(" <><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("                  1.Deposit!?")
    print("            $$$   2. WithDraw!   $$$")
    print("                  3. Play...                   ")
    print("                  4. Later Loser!    ;)                ")


# user deposit function
def deposit(balance): # allows user to deposit money
    deposit_amount = input("How much you willing to lose?") # amount choosen to put on account to play
    balance += deposit_amount # so deposit amount stacks on top of balance already had
    print("Good luck with just!: " , balance)
    return 

# user withdraw function

def cashout(balance): # withdraw
    cashout = input("Are you sure you wanna cashout?") # withdrawing balance from account
    print("Guess you beat me for! : ", balance)
    balance = 0
    return

# Exit function ( for if a loan was taken/ Cashout otion)
# exit function 
# players can leave unless player has outstanding loan with the casino
def exit(): # play later
    if not loggedin:
        return
    if loan == 0:
        print("Thanks for playing ")
        return
    if loan > 0:
        print("Loan balance of: ", loan)
        print("Pay balance to logoff")
        payloan(loan, balance) # calls payloan function 
        return

# if loan amount it paid down it's taken from players balance
# if a player makes a payment loan amount goes down
#players balance goes down as well

def payloan(loan, balance):
    if loan > 0:
        print("Pay loan amount of: ", loan)
        print("Your current balance is: ", balance)
        print("Your interest rate is 7%") # intrest rate
        makepayment = input("Would you like to make a payment? ") # asking to make payment
    if makepayment == 'yes':
        payment = int(input("Please enter loan payment amount: "  )) # if yes payment amount
        if payment > balance:
            print("Insufficent funds enter a different amount") # if payment bigger than balance
        elif payment > loan:
            print("Loan max payment is", loan, "Enter loan balance") # if payment was bigger than loan  elif to avoid subtraction negative values from the loan and balance
        elif payment > 0:                                 # taking payment from both loan and balance
            loan -= payment
            balance -= payment
            print("New Account balance of: ", balance) # new balance
            print("Loan balance of: ", loan) # balance loan if any
            # calculate interest to loan balnce
            interest = loan * 0.07
            loan += interest
            print("Loan balance with interest ", loan)
    if loan > 0:  # loan still not paid off looping payloan function to ask to pay more / again
        payloan(loan, balance)
    if makepayment == 'no': # if no exit menu
        return
        # if user says yes ask how much and take from loan balance
        # if no return to register menu
        # if user pays off loan amount prompt thank you take from balance and check if additional money needs to be added
        # if not  winner winner chicken dinner
    else:
        print("No money owed have a good one!")
        return


# reg user menu
def reg_menu(name):
    print("|!--------        Welcome", name,        "--------|!")
    print("??????????? What would you like to do? ?????????????")
    print("                  1.Deposit!?")
    print("            $$$   2. WithDraw!   $$$")
    print("                  3. Play...                   ")
    print("               $  4. Loan  $                            ")



# loan request
def loan_request(loan, balance):
    if not loggedin:   # if guest trys to take a loan
        print("Please login to request a loan")
        return
    if loan > 0:  # if user already has a loan
        print("You already have a loan of ", loan)
        return
    # loan amount requested by user
    loan_amount = int(input("Enter loan amount you want: "))
    # loan amout must be greater than 0
    if loan_amount <= 0:
        print("Loan must be more than zero")
        return
    # loan cant be more than twice your balance
    if loan_amount > balance *2:
        print("Loan request cant be more than twice your blance")
        return
    # loan added to balance
    loan = loan_amount
    balance += loan_amount
    print(loan_amount, "Has been added to your account")
    return



# Black jack card game 
import random
# Make and shuffle a deck of cards
# should make list and values of all cards
# this param should be the number of decks returned in the final return of the function
def make_deck(numDecks):
    # final cards will be the list with every card value based on how many decks is asked for. This value will be in order and NOT shuffled
    finalCards = []
    # we make the decks and return them
    # by using a for loop, we can make the function do the deck creation logic as many times as decks requested
    for i in range(numDecks): # 1 - 3 decks 
        # here we do 1 round per suit (since there 4 suits, we do 0, 1, 2, 3, as 4 is excluded in range)
        for j in range(4):
            # default suit will be spades
            suit = '♠'
            if j == 1:
                suit = '♣'
            elif j == 2:
                suit = '♥'
            elif j == 3:
                suit = '♦'
            # here we set the range to 13 so that we can get every card in the suit
            for k in range(13):
                value = k
                name = str(k)
                if k == 0: # set if statements for edge cases so rest of deck will run it's name and value together
                    value = 10
                    name = "King"
                elif k == 1:
                    value = 11
                    name = "Ace"
                elif k == 11:
                    value = 10
                    name = "Jack"
                elif k == 12:
                    value = 10
                    name = "Queen"
                card = {
                    "value": value,
                    "name": name,
                    "suit": suit,
                }
                finalCards.append(card)
                # now we need to check what j is (that will determine the suit)
                # then we need to make sure we account for 0 being a king 1 being a ACE and 11: jack, 12: queen
                # once we create the card (we can use a dictionary for this to make it easily accesible and store data)
                # next we can use a method to add the newly created card to the finalCards list (each card will be a dictionary)
    return finalCards

def shuffleCards(cards):
    # first we declare an empty list to hold all the cards, but in a new order
    shuffledCards = []
    # this will take in a list (all of the cards) and return the exact same cards in a randomized order
    # we set a while loop to continue shuffling until the original list of cards is created
    while len(cards) > 0:
    # every iteration of the loop we generate a random number that will be the index of the random card we choose from the original list
    # has to be held in a variable so we ensure that we only remove the exact card (index) that we added to our new shuffled deck
        start_card = random.randint(0, len(cards) -1)
    # next we append the card into our shuffled list (this is a random card from the sorted list), append places it in the 0 index position
        shuffledCards.append(cards[start_card])
    # we remove the card we just placed in the shuffled list from the original list here
        cards.pop(start_card)
    # we re run the loop with a smaller list (we just removed a card from it), and continue this untill we have a random list
    return shuffledCards



# function to a deal cards from a deck


# need to know value of a hand
def hand_value(hand):
    value = 0
    ace count = 0
    for card in hand:
        if card['name'] == 'Ace':
            ace_count += 1
            value += 11
        else:
            value += card['value']


    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

#show dealer and player hands
def show_hand(hand, player_type="Player", hide_second_card=False):
    print(f"{player_type}'s hand:")
    for i, card in enumerate(hand):
        if player_type == "Dealer" and i == 1 and hide_second_card:
            print("Hidden Card")
        else:
            print(f"{card['name']} of {card['suit']}")
    if not hide_second_card:
        print("Total value:", hand_value(hand))

# function to hit or stay (double, split)         insurance?----------- Player turn / Dealer turn




# determine a winner or push