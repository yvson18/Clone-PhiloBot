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




consumer_key = ""
consumer_secret = ""

access_token = ""

access_token_secret = ""


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

def replying():

    tweets = twitter.get_mentions_timeline(since_id = read_last_seen("reply_control.txt"))
    
    if("#randosophyimg" in tweets[0]['text'].lower()):
        r = requests.get(f"http://127.0.0.1:8000/img/{frase_filtrada(tweets[0]['text'])}")
        time.sleep(1)            
        with open("cache_img_generated/img_gerada.jpg","wb") as f:
            f.write(r.content)
    
        response = twitter.upload_media(media="cache_img_generated/img_gerada.jpg")
        twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']],in_reply_to_status_id=tweets[0]['id'])

        store_last_seen("reply_control.txt",tweets[0]['id'])

    print(tweets[0]['user']['screen_name'])

replying()


