suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]
    def __str__(self):
        return self.rank+' of '+self.suit
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    def __str__(self):
        self.deck_comp = ''
        for card in self.deck:
            self.deck_comp += '\n' + card.__str__()
        return self.deck_comp   
    def __len__(self):
        return len(self.deck)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        global dealed_card
        dealed_card = self.deck.pop()
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self):
        self.cards.append(dealed_card)
        self.value += dealed_card.value
        if dealed_card.rank == 'Ace':
            self.aces += 1
    def ace_handling(self):
        if self.value > 21 and self.aces >= 1:
            self.value -= 10
            self.aces -= 1
    def __str__(self):
        self.hand_comp = ''
        for card in self.cards:
            self.hand_comp += '\n' + card.__str__()
        return self.hand_comp+'\n'+'which adds up to: '+str(self.value)
    def reset(self):
        self.cards = []
        self.value = 0
        self.aces = 0
class Chips:
    def __init__(self,chips):
        self.chips = chips
        self.money = chips*25
    def add(self,chips):
        self.chips += chips
        self.money += chips*25
    def bet(self,chips):
        self.chips -= chips
        self.money -= chips*25
    def __str__(self):
        return 'You have '+str(self.chips)+' chips which is worth '+str(self.money)+'$'                        
def bet():
    global playing
    while True and playing == True:
        if player_chips.chips == 0:
              
                playing = False
                print('You are out of chips')
                break     
        try:
            global bet_amount
            print(player_chips.__str__())
            bet_amount = int(input('please enter the number of chips you want to bet: '))
        except:
            print('You have not entered a valid number')
            continue
        else:
            if bet_amount > player_chips.chips:
                print('You dont have that much chips.Please try again')
                continue
            elif bet_amount <= 0:
                print('You cant bet '+str(bet_amount)+' chips.Please try again')
                continue
            else:
                player_chips.bet(bet_amount)
                print('Chips accepted\nYou have '+str(player_chips.chips)+' chips left in your balance\nYou have bet '+str(bet_amount)+' chips')
                break
def giveCards():
    global gamedeck
    while True:
        if len(gamedeck) > 4 and playing == True:
            gamedeck.deal()
            player_hand.add_card()
            gamedeck.deal()
            player_hand.add_card()
            gamedeck.deal()
            dealer_hand.add_card()
            gamedeck.deal()
            dealer_hand.add_card()
            print('\nYou have:'+player_hand.__str__())
            print('\nDealer has:\n'+dealer_hand.cards[0].__str__()+'\n..........'+'\nwhich adds up to: '+str(dealer_hand.cards[0].value))
            break
        elif len(gamedeck) <= 4 and playing == True:
            gamedeck = Deck()
            gamedeck.shuffle
            print('\nCARDS ARE ADDED TO THE DECK AND SHUFFLED')
            continue
        else:
        	break
            
def h_or_s():
    global bet_amount
    global player_diff
    global dealer_diff
    global playing
    
    while True and playing == True:
        if player_hand.value == 21:
            print('BlackJack')
            player_chips.add(bet_amount*3)
            player_hand.reset()
            dealer_hand.reset()
            break
        try:
            decision = str(input('Do you want to Hit or Stay?(h/s)'))
        except:
            print('Please enter Hit or Stay')
        else:
            if decision.lower() == 'h':
                gamedeck.deal()
                player_hand.add_card()
                player_hand.ace_handling()
                print('\nYou have'+player_hand.__str__())
                if player_hand.value > 21:
                        print('busted')
                        player_hand.reset()
                        dealer_hand.reset()
                        break
                else:
                     continue
            elif decision.lower() == 's':
                player_diff = 21-player_hand.value
                dealer_diff = 21-dealer_hand.value
                while dealer_diff > 4:
                        gamedeck.deal()
                        dealer_hand.add_card()
                        dealer_hand.ace_handling()
                        dealer_diff = 21-dealer_hand.value
                print('\nYou have:'+player_hand.__str__())
                print('\nDealer has:'+dealer_hand.__str__())
                if dealer_diff < player_diff and dealer_diff <= 4 and dealer_diff >= 0:
                        print('Dealer win!')
                        player_hand.reset()
                        dealer_hand.reset()
                        break
                elif player_diff == dealer_diff:
                        print('Push')
                        player_chips.add(bet_amount)
                        player_hand.reset()
                        dealer_hand.reset()
                        break
                else:
                    print('You win!')
                    player_chips.add(bet_amount*2)
                    player_hand.reset()
                    dealer_hand.reset()
                    break

print('Welcome to Black Jack')
while True:
    try:
        player_chips = Chips((int(input('Please enter the amount of chips you want to play with(1 chip = 25$)'))))
        print(player_chips)
    except:
        print('You have not entered a valid number')
    else:
        result = str(input('Are you ready?(y/n)'))
        if result.lower() == 'y':           
            gamedeck = Deck()
            gamedeck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand()
            playing = True
        else:
            continue
        while playing:
            bet()
            giveCards()
            h_or_s()
        playagain = input('Do you want to play again?(y/n)')
        if playagain.lower() == 'y':
            continue
        else:
            break
                                                 