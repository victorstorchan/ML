from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob


#consumer key, consumer secret, access token, access secret.
ckey="blabla"
csecret="blabla"
atoken="blabla"
asecret="blabla"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        testimony = TextBlob(tweet)
        
#subjectivity=0 =>very objective 1=>very subjective, polarity is in [-1,1]
#use patternAnalyser otherwise, can use naivebayses with: 
#     blob = TextBlob("text", analyser=NaiveBayesAnalyser())
# => blob.sentiment is Sentiment(classification='pos',p_pos=..,p_neg=..)

        print(tweet, testimony.sentiment.polarity, testimony.sentiment.subjectivity)
        if testimony.sentiment.subjectivity<0.5:
            output=open("twitter-out.txt",'a')
            output.write(str(testimony.sentiment.polarity))
            output.write('\n')
            output.close()
        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["chegg"])
