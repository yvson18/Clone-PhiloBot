import requests, re
from twython import Twython
import time

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = file_read.read().strip()
    file_read.close()
    return int(last_seen_id)

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
  
def frase_filtrada(frase):
    words_pattern = '[a-z]+'
    palavras = re.findall(words_pattern, frase, flags=re.IGNORECASE)
    frase_completa = " ".join([palavrinha for palavrinha in palavras if((palavrinha != "BotJaguar")and(palavrinha != "randosophyimg"))])
    return frase_completa


consumer_key = "N8E2mQgqM53VGDpGVZZ6vLozV"
consumer_secret = "O1no11MKOGq5zcUVi8ru4MXWtSyqnrWGBxRSvMkzJU6JY7LbLa"

access_token = "1367106253655314432-rb8SGaykgI09OpPeAU5ri7tbTkOjL1"

access_token_secret = "1P9gQ7cKSx7KfRNagnQJjdFkjatAfyLvne7uAZca63Mdl"


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

def replying():

    tweets = twitter.get_mentions_timeline(since_id = read_last_seen("reply_control.txt"))
    for tweet in tweets:
        if("#randosophyimg" in tweet['text']):
            r = requests.get(f"http://127.0.0.1:8000/img/{frase_filtrada(tweet['text'])}")
            with open("cache_img_generated/img_gerada.jpg","wb") as f:
                f.write(r.content)

            photo = open('cache_img_generated/img_gerada.jpg', 'rb')
            response = twitter.upload_media(media=photo)
            twitter.update_status(media_ids=[response['media_id']],in_reply_to_status_id = tweet["id"], auto_populate_reply_metadata = True)
            store_last_seen("reply_control.txt",tweet["id"])
    time.sleep(15)
while(True):
    replying()
    
    