with open("dec05-indata.txt") as indata:
    cards = [card.strip() for card in list(indata)]
    seatIDs = []
    for card in cards:
        (fromRow, toRow) = (1, 128)
        (fromCol, toCol) = (1, 8)
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

        seatIDs.append(seatID)

    seatIDs.sort()
    prevId = 0
    for prospect in seatIDs:
        if prospect == prevId + 2:
            print(prevId, prospect)
        prevId = prospect
