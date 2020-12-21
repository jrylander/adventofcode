with open("dec05-indata.txt") as indata:
    cards = [card.strip() for card in list(indata)]
    for card in cards:
        fromRow = 1
        toRow = 128
        fromCol = 1
        toCol = 8
        for idx, character in enumerate(card):
            if idx < 7:
                step = int((toRow - fromRow + 1) / 2)
                if character == 'F':
                    toRow -= step
                else:
                    fromRow += step
            else:
                step = int((toCol - fromCol + 1) / 2)
                if character == 'L':
                    toCol -= step
                else:
                    fromCol += step

        row = fromRow - 1
        col = fromCol - 1
        seatID = row * 8 + col

        print(seatID)
    