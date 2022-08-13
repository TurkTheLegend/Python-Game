import random
def blackjack() :
    #สร้างเด็ค
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    #สับไพ่
    random.shuffle(deck)
    #จั่วไพ่ฝ่ายละ 2 ใบ
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    #เปิดไพ่
    print("Player: " + str(player_hand) + " = " + str(sum(player_hand)))
    print("Dealer: " + str(dealer_hand) + " = " +str(sum(dealer_hand)))
    #ตาผู้เล่น
    while True:
        choice = input("Hit or stand? ")
        if choice == "hit":
            player_hand.append(deck.pop())
            print("Player: " + str(player_hand) + " = " + str(sum(player_hand)))
            if sum(player_hand) > 21:
                print("You lose!")
                break
        elif choice == "stand":
            break
    #if sum(dealer_hand) >= 17 and sum(dealer_hand) <= 21 :
    #   print("Dealer: " + str(dealer_hand) + " = " + str(sum(dealer_hand)))
    #ตาบอท
    while sum(dealer_hand) < 17 and sum(player_hand) <= 21:
        dealer_hand.append(deck.pop())
        print("Dealer: " + str(dealer_hand) + "  = " + str(sum(dealer_hand)))
        if sum(dealer_hand) > 21:
            print("You win!")
            break
    #เปรียบเทียบไพ่
    if sum(player_hand) <= 21 and sum(dealer_hand) <= 21:
        if sum(player_hand) > sum(dealer_hand):
            print("You win!")
        elif sum(player_hand) < sum(dealer_hand):
            print("You lose!")
        else:
            print("Tie!")

blackjack()