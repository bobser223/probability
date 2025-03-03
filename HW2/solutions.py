import numpy as np

############################### 4.2 #################################

def find(arr, target):
  counter = 0
  for el in arr:
    if el == target:
      counter +=1

  return counter


def P(n, direct_case):

  return direct_case / n


for n in [10,50,100,250,500,1000,2500,5000,10000]:
  all_tosses = np.random.randint(6, size=n)
  print(f"n = {n} : ", end=' ')

  check = 0

  for i in range(6):
    curr_P = P(n, find(all_tosses, i))
    print(f"P({i}) = {curr_P}", end=', ')
    check += curr_P
  print('\n')
  # print(f"check = {check}")


############################ 5.2 #####################################

prob = {2:0, 4:0, 6:0, 8:0, 10:0}
arr = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 10000000]
for n in arr:
  random_numbers = np.random.randint(52 / 4, size=n)
  counter = 0
  for i in random_numbers:
    if i == 2 or i == 4 or i == 6 or i==8 or i == 10:
      counter += 1
  print(f"n = {n}, P = {counter / n}")


########################### 5.3 #######################################


import numpy as np

Ranks = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
Suits = ['♢', '♠', '♣', '♡']

s1 = [(Rank, Suit) for Rank in Ranks for Suit in Suits[0]]
s2 = [(Rank, Suit) for Rank in Ranks for Suit in Suits[1]]
s3 = [(Rank, Suit) for Rank in Ranks for Suit in Suits[2]]
s4 = [(Rank, Suit) for Rank in Ranks for Suit in Suits[3]]



s_n = [s1, s2, s3, s4]

# for s in s_n:
#     print(s)

p1 = []
p2 = []
p3 = []
p4 = []

p_n = [p1, p2, p3, p4]


def is_in(player, suit_number):
    for card in player:
        if card[1] == Suits[suit_number]:
            return True
    return False


def give4(p_n, s_n):
    used_players = []
    used_suits = []

    while (len(used_players) != 4):
        rn_p = np.random.randint(4)
        rn_s = np.random.randint(4)

        if rn_p in used_players or rn_s in used_suits:
            continue

        used_players.append(rn_p)
        used_suits.append(rn_s)

        give(p_n[rn_p], s_n[rn_s], 4)


def give3(p_n, s_n):
    used_players = []
    used_suits = []
    while len(used_players) != 4:
        rn_p = np.random.randint(4)
        rn_s = np.random.randint(4)
        if rn_p in used_players or rn_s in used_suits:
            continue
        if len(p_n[rn_p]) == 13 or len(s_n[rn_s]) == 0:
            continue
        if is_in(p_n[rn_p], rn_s):
            continue

        used_players.append(rn_p)
        used_suits.append(rn_s)
        give(p_n[rn_p], s_n[rn_s], 3)


def give(player, cards, amount):
    for _ in range(amount):
        rn_card = np.random.randint(len(cards))
        player.append(cards[rn_card])
        cards.pop(rn_card)


give4(p_n, s_n)
for _ in range(3):
    give3(p_n, s_n)

for p in p_n:
    print(p)


###########################3 5.3_2 ##############

import random

# 1. Визначимо масті та ранги
suits = ['♣', '♠', '♦', '♥']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Створимо колоду, розбиту за мастями
deck_by_suit = {suit: [f"{suit}{rank}" for rank in ranks] for suit in suits}

# 2. Створимо 4 гравців і випадково призначимо кожному “головну” масть
players = [[] for _ in range(4)]
major_suits = suits.copy()
random.shuffle(major_suits)
player_major = {i: major_suits[i] for i in range(4)}

print("Головні масті гравців:")
for i in range(4):
    print(f"Гравець {i+1}: {player_major[i]}")

# 3. Роздача карт за мастями
for suit in suits:
    # Перемішуємо карти даної масті
    cards = deck_by_suit[suit].copy()
    random.shuffle(cards)
    
    # Знаходимо, який гравець отримує 4 карти цієї масті (головна масть)
    major_player = None
    for player, m_suit in player_major.items():
        if m_suit == suit:
            major_player = player
            break
            
    # Гравець з головною мастю отримує 4 карти
    players[major_player].extend(cards[:4])
    
    # Решта гравців отримують по 3 карти
    remaining_cards = cards[4:]
    # Отримуємо список гравців, крім major_player
    non_major_players = [p for p in range(4) if p != major_player]
    for i, player in enumerate(non_major_players):
        players[player].extend(remaining_cards[i*3:(i+1)*3])

# 4. Перевіримо та виведемо руки гравців
print("\nРоздані руки гравців:")
for i, hand in enumerate(players):
    # Можна відсортувати руку для кращого перегляду (наприклад, за мастями)
    print(f"Гравець {i+1} (головна масть {player_major[i]}): {hand}")
