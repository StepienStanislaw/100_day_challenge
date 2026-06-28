# TODO-1: Import and print the logo from art.py when the program starts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount):
    enc = ''
    if direction == 'encode':


        for i in original_text:
            if i not in alphabet:
                enc += i
            else:
                indx = alphabet.index(i)
                indxSh = indx + shift_amount
                if indxSh<=25:
                    enc += alphabet[indxSh]
                else:
                    indxSh = 0+(indxSh%26)
                    enc += alphabet[indxSh]
        print(enc)
    else:
        temp = ''
        for i in original_text:
            if i not in alphabet:
                temp += i
            else:
                indx = alphabet.index(i)
                indxSh = indx - shift_amount
                temp += alphabet[indxSh]
        print(temp)


# TODO-3: Can you figure out a way to restart the cipher program?



should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


