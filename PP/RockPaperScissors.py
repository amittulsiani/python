def rps():
    w1 = 0
    w2 = 0
    tot = 0
    for tot in range(500):
        a1 = raw_input("User 1 - Rock,Paper or Scissors ? ")
        a2 = raw_input("User 2 - Rock,Paper or Scissors ? ")
        if ((a1 == 'quit' or a1 == 'q') or (a2 == 'quit' or a2 == 'q')):
            print ("Game Over")
            break
        elif (a1 == 'Rock') and (a2 == 'Scissor'):
            w1 += 1
            tot += 1
            print 'Player 1 wins '
        elif (a2 == 'Rock') and (a1 == 'Scissor'):
            w2 +=1
            tot += 1
            print 'Player 2 wins '
        elif (a1 == 'Scissor') and (a2 == 'Paper'):
            w1 +=1
            tot += 1
            print 'Player 1 wins '
        elif (a2 == 'Scissor') and (a1 == 'Paper'):
            w2 +=1
            tot += 1
            print 'Player 2 wins '
        elif (a1 == 'Paper') and (a2 == 'Rock'):
            w1 +=1
            tot += 1
            print 'Player 1 wins '
        elif (a2 == 'Paper') and (a1 == 'Rock'):
            w2 +=1
            tot += 1
            print 'Player 2 wins '
        else:
            print 'Invalid Input'
            tot += 1
    print 'Total Player 1 wins ',w1
    print 'Total Player 2 wins ',w2
    print 'Total games played - ', tot

rps()
