from caesar_cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position  = alphabet.index(letter)
            new_pos = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_pos]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_type = input("type yes to continue, type no to exit:\n")
    if user_type == "no":
        should_continue = False
        print("GoodBye")
    