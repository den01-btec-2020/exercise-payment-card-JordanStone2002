import PaymentCard

def main():
    #write your code below this line
   def test_exercise(Bananas):
    card = PaymentCard(30)
    print(card)

    out, err = Bananas.readouterr()
    assert out == "The card has a balance of 30 pounds\n"

    card = PaymentCard(30)
    card.add_money(15)
    print(card)


if __name__ == '__main__':
    main()
