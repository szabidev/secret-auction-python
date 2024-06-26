from logo import logo

print(logo)

auction_members = {}
play_again = True
winner = ''
while play_again:
    auctioneer = input('What is your name?\n').lower()
    bid_price = int(input('What is your bid?\n'))

    auction_members[auctioneer] = bid_price
    winner = max(auction_members, key=auction_members.get)

    more_players = input("Are there other users who want to bid? Type 'yes' or 'no'\n")
    if more_players == 'no':
        play_again = False

print(f"The winner is {winner} with {auction_members[winner]}")




