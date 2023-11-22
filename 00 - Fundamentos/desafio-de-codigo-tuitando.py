T = input()

quantidade_caracter_str = str(T)  

if len(quantidade_caracter_str) <= 140:
    print("TWEET")
else:
    print("MUTE")