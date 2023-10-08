############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## start
from blackjack_art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True

# 打印结果
def print_winner(winner, user, computer):
    
    if winner == 1:
        print("You lose! 😭")
    elif winner == 0:
        print("You win! 😄")
    else:
        print("Draw! 🙃")
    print(f"Your end cards is {user}, in total {cal(user)}")
    print(f"Comupter's end cards is {computer}, int total {cal(computer)}")

# 询问是否继续
def ask_wether_continue():
    user_continue = input("Do you want to continue?(y or n):").lower()
    if user_continue == 'y':
        return True
    else:
        return False
    
# 判断是否是blackjack
def judge_blackjack(list):
    if cal(list) == 21:
        return True
    else:
        return False
    
# 计算点数
def cal(list):
    total = sum(list)
    if total > 21:
        total -= list.count(11) * 10
        return total
    else:
        return total
    
# main函数
def start():
    os.system("clear")
    print(logo)
    user = []
    computer = []
    user.append(random.choice(cards))
    user.append(random.choice(cards))
    computer.append(random.choice(cards))
    computer.append(random.choice(cards))
    
    # 判断是否直接胜利
    if judge_blackjack(user) or judge_blackjack(computer):
        if judge_blackjack(computer):
            print_winner(1, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
        elif judge_blackjack(user):
            print_winner(0, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
    
    
    # 玩家抽卡
    print(f"The dealer's first card is {computer[0]}")
    print(f"Your card is {user}")
    user_draw = input("Do you want to draw a new card?(y or n):").lower()
    print(user_draw)
    while user_draw == 'y':
        user.append(random.choice(cards))
        print(f"Your cards is {user}")
        if cal(user) > 21:
            print_winner(1, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
        elif judge_blackjack(user):
            print_winner(0, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
        else:
            # print(f"Your card is {user}")
            user_draw = input("Do you want to draw a new card?(y or n):").lower()
    
    # 电脑抽卡
    while cal(computer) <= 16:
        computer.append(random.choice(cards))
        if cal(computer) > 21:
            print_winner(0, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
        elif judge_blackjack(computer):
            print_winner(1, user=user, computer=computer)
            if ask_wether_continue():
                start()
            return
    
    # 判断大小
    if cal(user) > cal(computer):
        print_winner(0, user=user, computer=computer)
    elif cal(user) < cal(computer):
        print_winner(1, user=user, computer=computer)
    else:
        print_winner(2, user=user, computer=computer)
    if ask_wether_continue():
        start()
        return
        
start()
