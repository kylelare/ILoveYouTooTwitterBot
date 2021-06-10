import tweepy
import time

consumer_key = #API Key
consumer_secret =  #Access Secret
key =  #Access Key
secret = #Access Secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


#MAKING SURE NOT TO CONTINUOUSLY REPLY TO LAST TWEET
FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME): #READING
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id): #WRITING
        file_write = open(FILE_NAME, 'w')
        file_write.write(str(last_seen_id))
        file_write.close()
        return

#api.update_status('Twitter bot reporting in live')

#tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
#print(tweets[0].text)

#REPLYNG TO TWEETS THAT SAY LOVE YOU
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        #print(str(tweet.id) + ' - ' + tweet.full_text)
        if 'love you' in tweet.full_text.lower():
            if 'love you too :)' not in tweet.full_text.lower():
                print(str(tweet.id) + ' - ' + tweet.full_text)
                api.update_status("@" + tweet.user.screen_name + " Auto reply is working :)", tweet.id)
                store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(5)
