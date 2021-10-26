VALUES={'J':11,'Q':12,'K':13,'A':14}

def make_suits(cards):
    suits = {'D':[],
    'H':[],
    'C':[],
    'S':[]}
    
    for card in cards:
        suits[card[-1]].append(card)
    
    return suits

def make_values(cards):
    values = dict()
    for card in cards:
        value = card[:-1]
        if value in values:
            values[value].append(card)
        else:
            values[value] = [card]
    return values

def check_straight_flush(suits):
    for same_suits_cards in suits.values():
        if len(same_suits_cards)>4:
            power = check_straight(same_suits_cards)
            if power==14:
                return 'Royal Flush'
            elif power > 0:
                return 'Straight Flush'
    return 0

def check_flush(suits):
    for same_suits_cards in suits.values():
        if len(same_suits_cards)>4:
            return True
    return False

def check_straight(cards):
    # повертає "силу" стріта 
    values = [card[:-1] for card in cards]

    for i in range(len(values)):
        if values[i] in ['J', 'Q','K','A']:
            values[i]=VALUES[values[i]]
        else:
            values[i]=int(values[i])

    values.sort(reverse=True)

    for i in range(len(values)-4):
        if values[i]==values[i+1]+1==values[i+2]+2==values[i+3]+3==values[i+4]+4:
            return values[i]

    if 14 in values and 2 in values and 3 in values and 4 in values and 5 in values :
        return 4
    
    return 0

def check_four_of_a_kind(values):
    lenghts = []
    for value in values:
        lenghts.append(len(values[value]))
    
    if max(lenghts)==4:
        return True
    else:
        return False

def check_full_house(values):
    lenghts = []
    for value in values:
        lenghts.append(len(values[value]))
    
    if 3 in lenghts and (2 in lenghts or lenghts.count(3)>=2):
        return True
    else:
        return False

def check_three_of_a_kind(values):
    lenghts = []
    for value in values:
        lenghts.append(len(values[value]))
    
    if 3 in lenghts:
        return True
    else:
        return False

def check_two_pairs(values):
    lenghts = []
    for value in values:
        lenghts.append(len(values[value]))
    
    if lenghts.count(2)>1:
        return True
    else:
        return False

def check_pair(values):
    lenghts = []
    for value in values:
        lenghts.append(len(values[value]))
    
    if 2 in lenghts:
        return True
    else:
        return False

hand = list(input().split())
table = list(input().split())

cards = hand + table

suits = make_suits(cards)
values = make_values(cards)

if check_straight_flush(suits):
    print(check_straight_flush(suits))
elif check_four_of_a_kind(values):
    print('Four of a Kind')
elif check_full_house(values):
    print('Full House')
elif check_flush(suits):
    print('Flush')
elif check_straight(cards):
    print('Straight')
elif check_three_of_a_kind(values):
    print('Three of a Kind')
elif check_two_pairs(values):
    print('Two Pairs')
elif check_pair(values):
    print('One Pair')
else:
    print('High Hand')