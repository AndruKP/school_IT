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
        if value in ['J', 'Q','K','A']:
            value=VALUES[value]
        else:
            value=int(value)

        if value in values:
            values[value].append(card)
        else:
            values[value] = [card]
    return values

def check_straight_flush(suits):
    for same_suits_cards in suits.values():
        if len(same_suits_cards)>4:
            power = check_straight(same_suits_cards)
            if power:
                power = power[1]
                if power==14:
                    return [10]
                elif power > 0:
                    return [9,power]
    return 0

def check_flush(suits):
    for same_suits_cards in suits.values():
        if len(same_suits_cards)>4:
            values = [card[:-1] for card in same_suits_cards]

            for i in range(len(values)):
                if values[i] in ['J', 'Q','K','A']:
                    values[i]=VALUES[values[i]]
                else:
                    values[i]=int(values[i])

            values.sort(reverse=True)
            return [6,values[:5]]
    return False

def check_straight(cards):
    # повертає "силу" стріта 
    values = [card[:-1] for card in cards]

    for i in range(len(values)):
        if values[i] in ['J', 'Q','K','A']:
            values[i]=VALUES[values[i]]
        else:
            values[i]=int(values[i])

    values = list(set(values))
    values.sort(reverse=True)
    
    for i in range(len(values)-4):
        if values[i]==values[i+1]+1==values[i+2]+2==values[i+3]+3==values[i+4]+4:
            return [5,values[i]]

    if 14 in values and 2 in values and 3 in values and 4 in values and 5 in values :
        return [5,4]
    
    return 0

def check_four_of_a_kind(values):
    for value in values:
        if len(values[value])==4:
            return [8,value] 

def check_full_house(values):
    lenghts = []
    for value in values:
        lenghts.append([value,len(values[value])])
    
    lenghts.sort(reverse=True)
    res = []

    for i in lenghts:
        if i[1]==3:
            res.append(i[0])
            break

    if len(res)==0:
        return 0

    for i in lenghts:
        if i[1]>=2 and i[0]!=res[0]:
            res.append(i[0])
            break
    
    if len(res)<2:
        return 0
    
    return [7,res]

def check_three_of_a_kind(values):
    lenghts = []
    for value in values:
        lenghts.append([value,len(values[value])])
    
    lenghts.sort(reverse=True)
    for i in lenghts:
        if i[1]==3:
            return [4,i[0]]
    
    return 0

def check_two_pairs(values):
    lenghts = []
    for value in values:
        lenghts.append([value,len(values[value])])
    
    lenghts.sort(reverse=True)
    res = []
    for i in lenghts:
        if i[1]==2:
            res.append(i[0])
        if len(res)==2:
            return [3,res]
    return 0


def check_pair(values):
    lenghts = []
    for value in values:
        lenghts.append([value,len(values[value])])
    
    lenghts.sort(reverse=True)
    for i in lenghts:
        if i[1]==2:
            return [2,i[0]]

def find_max(cards):
    values = [card[:-1] for card in cards]

    for i in range(len(values)):
        if values[i] in ['J', 'Q','K','A']:
            values[i]=VALUES[values[i]]
        else:
            values[i]=int(values[i])
    
    return max(values)

Vlad = list(input().split())
Sofiia = list(input().split())
Vitia = list(input().split())
Natalia = list(input().split())
table = list(input().split())

#-> [power_between_diff_combs,[power_among_same_combs],high_hand_value,Name]
def check_hand(hand, table, name):
    cards = hand + table
    suits = make_suits(cards)
    values = make_values(cards)

    result = []

    if check_straight_flush(suits)==[10]:
        result = [10,14,14,name]
        
    elif check_straight_flush(suits):
        result = check_straight_flush(suits)
        result.append(find_max(cards))
        result.append(name)

    elif check_four_of_a_kind(values):
        result = check_four_of_a_kind(values)
        result.append(find_max(cards))
        result.append(name)

    elif check_full_house(values):
        result = check_full_house(values)
        result.append(find_max(cards))
        result.append(name)

    elif check_flush(suits):
        result = check_flush(suits)
        result.append(find_max(cards))
        result.append(name)

    elif check_straight(cards):
        result = check_straight(cards)
        result.append(find_max(cards))
        result.append(name)

    elif check_three_of_a_kind(values):
        result = check_three_of_a_kind(values)
        result.append(find_max(cards))
        result.append(name)

    elif check_two_pairs(values):
        result = check_two_pairs(values)
        result.append(find_max(cards))
        result.append(name)

    elif check_pair(values):
        result = check_pair(values)
        result.append(find_max(cards))
        result.append(name)

    else:
        result = [1,find_max(cards)]
        result.append(find_max(cards))
        result.append(name)

    return result

game = [check_hand(Vlad, table, name='Vlad'),
check_hand(Sofiia, table, name='Sofiia'),
check_hand(Vitia, table, name='Vitia'),
check_hand(Natalia, table, name='Natalia')]

game.sort(reverse=True)

#print(game)

print(game[0][-1])
