import random

while 1:
    def ai_move(plh, aih, tb):
        aihand = [a[0] for a in aih]

        if table != 'X':
            for indx, aicard in enumerate(aihand):
                if aicard == tb:
                    return aih[indx]

        plh = [c[0] for c in plh]
        possible_moves = [itm for itm in aih if itm[0] not in plh]
        return random.choice(possible_moves) if len(possible_moves) > 0 else random.choice(aih)


    deck = list({'1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '0A', 'JA', 'QA', 'KA', '1B', '2B', '3B', '4B',
                 '5B', '6B', '7B', '8B', '9B', '0B', 'JB', 'QB', 'KB', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C',
                 '9C', '0C', 'JC', 'QC', 'KC', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD',
                 'KD'})
    table = deck[:4]
    for item in table:
        deck.remove(item)  # deck.remove(item for item in table) didn't work there.
    plp = 0
    aip = 0
    aitable = []
    pltable = []
    for i in range(1, 7):
        PlayerHand = deck[:4]
        for a0 in PlayerHand:
            deck.remove(a0)
        ai = deck[:4]
        for a1 in ai:
            deck.remove(a1)
        for j in range(1, 5):
            # PL MOVE SECTION
            plmove = random.choice(PlayerHand)

            if len(table) > 0:  # one more control due to jack card

                if plmove[0] == 'J':  # if card is jack

                    if not len(table) == 1:
                        plp += 1
                    else:
                        plp += 30
                    pltable.append(table)
                    table = []

                else:  # if move is not jack

                    if plmove[0] == table[-1][0]:  # if cards are same with table
                        if len(table) == 1:  # if pisti
                            plp += 10
                        pltable.append(table)
                        table = []
                    else:
                        if plmove != 'J':
                            table.append(plmove)

            else:  # if table is empty
                table.append(plmove)

            PlayerHand.remove(plmove)

            # AI MOVE SECTION
            if len(table) > 0:

                aimove = ai_move(PlayerHand, ai, table[-1][0])

                if aimove[0] == 'J':
                    if not len(table) == 1:
                        aip += 1
                        aitable.append(table)
                        table = []

                if len(table) > 0:  # one more control due to JACK CARD

                    if aimove[0] == table[-1][0]:  # if cards match !

                        if not len(table) > 1:  # if only one card is on the table
                            if aimove[0] == 'J':
                                aip += 30
                            else:
                                aip += 10

                        else:  # if there are more than one card

                            aitable.append(table)
                            if '2B' in table:
                                aip += 2
                            if '10D' in table:
                                aip += 3

                        table = []

                    else:
                        if aimove[0] != 'J':
                            table.append(aimove)

                ai.remove(aimove)

            else:
                table.append(ai_move(PlayerHand, ai, 'X'))
                ai.remove(table[0])
        if i == 6:
            aitable = ''.join([''.join(a) for a in aitable])
            pltable = ''.join([''.join(b) for b in pltable])
            if len(aitable) > len(pltable):
                aip += 3
            else:
                plp += 3
            print(f"""
        |--------------------------------------|
        |---- -------GAME IS OVER!----  ---- --|
        |----*** PLAYER POINTS: {plp} ***------|
        |--  ---*** AI POINTS : {aip} *** --- -|
        |********WINNER:{'ai' if aip > plp else 'YOU'}****--|
        |---------------------------------------------|
        |data is writing into data file...|
        ----------------------------------|""")
    # WRITE THE DATA

    with open('pistidata', 'a') as dta:
        dta.write(str(plp))
        dta.write('\t')
        dta.write(str(aip))
        dta.write('\t')
        dta.write('1' if aip > plp else '0')  # the game
        dta.write('\n')
