def highest_score(sentence):
    max=0
    L=sentence.split(' ')
    list_len=len(L)
    max=0
    
    for i in range(list_len):#petla po slowach
        suma=0
        for letter in L[i]:#petla po literach
            if(ord(letter)<65 or ord(letter)>122):
                #print("extra: "+letter)
                continue 
            if(letter.upper()==letter):#jesli wielka litera
                suma+=ord(letter)-64
               # print("upper"+letter)
            else:
                suma+=ord(letter)-96
               # print("lower:"+letter)
        if suma> max:
            word=L[i]
            max=suma
    
    word = word.replace(',', '')
    word = word.replace('.', '')
   # print(word)
    return word
"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

Make your function case insensitive.

Treat all special characters as 0.

"""
assert highest_score("I would have gotten the promotion, but my attendance wasn't good enough.") == 'promotion'
assert highest_score("She finally understood that grief was her love with no place for it to go.") == 'understood'
assert highest_score("He invested some skill points in Charisma and Strength.") == 'Strength'
assert highest_score("The waitress was not amused when he ordered green eggs and ham.") == 'waitress'
assert highest_score("She had some amazing news to share but nobody to share it with.") == 'nobody'
assert highest_score("She saw the brake lights, but not in time.") == 'lights'
assert highest_score("He wondered if she would appreciate his toenail collection.") == 'collection'
assert highest_score("Stop waiting for exceptional things to just happen.") == 'exceptional'
assert highest_score("Mary plays the piano.") == 'plays'
assert highest_score("He had concluded that pigs must be able to fly in Hog Heaven.") == 'concluded'
assert highest_score("I purchased a baby clown from the Russian terrorist black market.") == 'terrorist'
assert highest_score("The Japanese yen for commerce is still well-known.") == 'well-known'
assert highest_score("Everyone says they love nature until they realize how dangerous she can be.") == 'Everyone'
assert highest_score("Never underestimate the willingness of the greedy to throw you under the bus.") == 'underestimate'
assert highest_score("It didnt make sense unless you had the power to eat colors.") == 'unless'
assert highest_score("The view from the lighthouse excited even the most seasoned traveler.") == 'lighthouse'
assert highest_score("Pink horses galloped across the sea.") == 'horses'
assert highest_score("She wanted a pet platypus but ended up getting a duck and a ferret instead.") == 'platypus'
assert highest_score("If you don't like toenails, you probably shouldn't look at your feet.") == 'shouldn\'t'
assert highest_score("Wisdom is easily acquired when hiding under the bed with a saucepan on your head.") == 'Wisdom'
print('noice')
