import twitter
import time

api = twitter.Api(consumer_key='jpgTPcFpC8Xq10CSTlCVM5q9x',
                  consumer_secret='E2jJ2UWsxKaN2CqyrBwiKIfhTZ9oK4NBfynUZ48erpdaJTjzrN',
                  access_token_key='1480882725087289344-CybjKiZvQTIw9WLobFst8w6HneSYWF',
                  access_token_secret='VRaUnBv0NDuipKMHf0PNdwgkdVcXWylfPidHk1VWfJr5y')

tweets = 0
searchs = 0
limitTweets = 50
limitSearchs = 50
word = 0

tab = ("marre de la vie","je me sent seul","je suis trop triste","je suis triste")

def isin(sentence, keyword):
    if(keyword in sentence):
        return(1)

def postStatus(update, inReplyTo):
    global tweets
    tweets += 1
    api.PostUpdate(update, in_reply_to_status_id=inReplyTo)

def search(research, howMany):
    global searchs
    global tweets
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
        if(isin(search.text, research)==1):
            postStatus("@" + search.user.screen_name + "<3", search.id)

def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    global word
    stop = False
    while(not stop):
        try:
            search(tab[word], "100")
            print(tab[word])
            word = word + 1
        except:
            print("Erreur (probablement de quota, on arrete)")
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)
    print("Fini, on attend 3H maintenant et on reprend.")

start()