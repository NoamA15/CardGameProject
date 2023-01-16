from CardGame import CardGame

print("Enter player #1 name:")
p1 = input()

print("Enter player #2 name:")
p2 = input()


game = CardGame(p1, 26, p2, 26)

print(game.p1)
print(game.p2)

for i in range(10):
    x = game.p1.get_card(game.p1.hand)
    y = game.p2.get_card(game.p2.hand)
    print(x, "vs", y)
    if x > y:
        game.p1.add_card(x)
        game.p1.add_card(y)
        print(game.p1.name)
    else:
        game.p2.add_card(x)
        game.p2.add_card(y)
        print(game.p2.name)

if game.get_winner() is None:
    print("Its a tie!")
else:
    print(game.get_winner())
