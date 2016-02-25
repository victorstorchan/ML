
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import tweepy
import time

#consumer key, consumer secret, access token, access secret.
ckey="CZ6rIRwD5SqXsEn6bqzeUhhYk"
csecret="02yypBc0q32y17yFlSl1hf6KfKwpNuEm8XJr6J1fN3utp2JOhP"
atoken="4085761879-q7auMSt1CbgQfL9q9NI9fufFkfdMBNGZFMAyudc"
asecret="YIHBattoKq1O6bVWS1QfwFoPtq4JgsapaO4M61FPYekNQ"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)



h=open('id_followers_chegg.txt','r')
l=[]
for i in h:
	l.append(i.split(','))
for i in range(len(l)):
	l[i][0]=l[i][0][1:]
for i in range(len(l)):
	l[i][len(l[i])-1]=l[i][len(l[i])-1][:-3]

for i in range(len(l)):
	for j in range(len(l[i])):
		l[i][j]=int(l[i][j])

list_id_chegg = []
for i in range(len(l)):
	for j in range(len(l[i])):
		list_id_chegg.append(l[i][j])
#print(list_id_chegg)

c = tweepy.Cursor(api.friends_ids, id = list_id_chegg[0],count = 200)
ids = []
k=0
for page in c.pages():
	k+=1
	if k==15:
		break
	else:
		print(k)
		ids.append(page)
print(ids)
