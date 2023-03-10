class Card:
    def __init__(self, value, suit):
        """This function defines the object 'card' with a value and a suit"""
        if type(value) != int:
            raise TypeError("Argument value must be of type int")
        if value < 1:
            raise ValueError("Argument value must be > 1")
        if value > 13:
            raise ValueError("Argument value must be < 13")
        if type(suit) != str:
            raise TypeError("Argument suit must be of type str")
        if suit not in ["Diamond", "Spade", "Heart", "Club"]:
            raise ValueError("Argument suit must be a valid suit")
        self.value = value
        self.suit = suit

    def __repr__(self):
        """This function returns the 'royal cards' with their names and returns the value and suit of each card"""
        if self.value == 1:
            return f"Ace: {self.suit}"
        elif self.value == 11:
            return f"Jack: {self.suit}"
        elif self.value == 12:
            return f"Queen: {self.suit}"
        elif self.value == 13:
            return f"King: {self.suit}"
        else:
            return f"{self.value}: {self.suit}"

    def __gt__(self, other):
        """This function defines that the 'Ace' is the highest card and the order of the suits in the case that
         2 cards have the same value"""
        if type(other) != Card:
            raise TypeError("Argument other must be of type Card")
        if self.value == 1 and other.value != 1:
            return True
        if other.value == 1 and self.value != 1:
            return False
        if self.value > other.value:
            return True
        elif self.value == other.value:
            list1 = ["Diamond", "Spade", "Heart", "Club"]
            return list1.index(self.suit) > list1.index(other.suit)
        else:
            return False

    def __eq__(self, other):
        """This function compares 2 cards"""
        if type(other) != Card:
            raise TypeError("Argument other must be of type Card")
        return self.value == other.value and self.suit == other.suit
