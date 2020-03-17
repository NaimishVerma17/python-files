cut_off = 30

score = int(input('Enter the score'))

if score >= cut_off:
    print('Pass')
else:
    print('False')

user_rating = int(input('Enter the rating b/w 1 and 5'))

if 1 <= user_rating < 2:
    print('Sorry to hear!')

elif 2 <= user_rating < 3:
    print('Improving!')

elif 3 <= user_rating < 4:
    print('Thank you!')

elif 4 <= user_rating < 5:
    print('We almost missed perfect rating from you!')

elif user_rating == 5:
    print('Woopsieeee!!')

else:
    print('Please enter the rating b/w 1 to 5 inclusive')
