import random

when = ['A few years ago ','Yesterday ','Last night','A long time ago' , 'On 11th feb']
name=['John','Daniel','James','Aanya','Mahi']
residence=['India','America','Singapur','Italy','Germany']
wentto=['school','university','seminar','school','college']
happended=['made a lots of friends','study','found a key','solved a mistery','wrote a book']
#random.choice wil take random valus from the list
print(random.choice(when)+','+random.choice(name)+' , lived in '+random.choice(residence)+','+'went to '+random.choice(wentto)+' and '+random.choice(happended))




