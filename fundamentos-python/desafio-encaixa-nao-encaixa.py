N = int(input())

for _ in range(N):
    a, b = input().split()
    
    if len(a) < len(b):
        print("nao encaixa")
    elif a[-len(b):] == b:
        print("encaixa")
    else:
        print("nao encaixa")