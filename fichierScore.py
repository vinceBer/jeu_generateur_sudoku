def concatenate(scoreN):
    score = scoreN[0] +":" + scoreN[1] +":" + scoreN[2] +":" + scoreN[3]+":" + scoreN[4]+":"+ scoreN[5]
    return score

def group(score):
    scoreN = score.split(":")
    return scoreN

def writeScore(scoreTab):
    with open("score.txt", "w") as filout:
        for scoreN in scoreTab :
            score = concatenate(scoreN) +"\n"
            filout.write(score)
        filout.close()

def readScore():
    scoreAll=[]
    try:
        with open("score.txt", "r") as filin:
            for ligne in filin:
                print(ligne)
                scoreN = group(ligne.strip())
                scoreAll.append(scoreN)
            filin.close()
    except:
        scoreAll = [['Facile', '', '', '', '', ''],
                    ['Moyen', '', '', '', '', ''],
                    ['Difficile', '', '', '', '', '']]
        print(scoreAll)

    return scoreAll

scoreTab=[['Facile', '30', '5', 'Paul', 'Smith', '20'], ['Moyen', '30', '5', 'Paul2', 'Smith', '20'], ['Difficile', '30', '5', 'Paul3', 'Smith', '20']]
print("scoreTab[2][0]=",scoreTab[2][0])

#allscore = readScore()
#writeScore(scoreTab)