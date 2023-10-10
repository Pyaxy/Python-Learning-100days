import random
from os import system
from time import sleep
from Higher_Lower_Game_art import logo, vs
from Higher_Lower_Game_data import data

# 打印logo
def welcome():
    system("clear")
    print(logo)

# 选择一个随机数据
def choose():
    A = random.choice(data)
    return A

# 显示题目
def display(A, B):
    welcome()
    print(f"Comapre A: {A['name']}, a {A['description']}, from{A['country']}.")
    print(vs)
    print(f"Comapre B: {B['name']}, a {B['description']}, from{B['country']}.")

def game():
    welcome()
    B = choose()
    count = 0
    is_finished = False
    while not is_finished:
        A = B
        B = choose()
        # 防止选到重复的数据
        while B == A:
            B = choose()
        display(A, B)
        answer = input("Who has more followers? Type 'A' or 'B':").lower()
        # 此处用到了同或
        if not ((A['follower_count'] > B['follower_count']) ^ (answer == 'a')):
            count += 1
            print(f"You are right, current score: {count}")
            sleep(2)
        else:    
            is_finished = True
    welcome()
    print(f"Sorry, that's wrong. Final score: {count}")
    
game()