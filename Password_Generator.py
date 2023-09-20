#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
nr_sum = nr_letters + nr_symbols + nr_numbers

# 遍历每一位
for i in range(1, nr_sum + 1):
  pool = []
  # 如果该字符还有要求则加入选择池
  if nr_letters > 0:
    pool.append(letters)
  if nr_symbols > 0:
    pool.append(symbols)
  if nr_numbers > 0:
    pool.append(numbers)
    
  # 从选择池中选择字符类型
  choice = random.choice(pool)
  # 再具体选择字符
  char_choice = random.choice(choice)
  # 每新增一个则减少一个要求
  if char_choice in letters:
    nr_letters -= 1
  elif char_choice in numbers:
    nr_numbers -= 1
  else:
    nr_symbols -= 1
  # 最终字符加入password
  password += char_choice

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P