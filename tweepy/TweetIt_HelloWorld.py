def tweetit(msg):
    import tweepy
    access_token = ""
    access_token_secret = ""
    consumer_key = ""
    consumer_secret = ""
    if(msg != ""):
        print("Message Tweet")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweet = msg
        print(tweet)
        if(debug == False):
            api.update_status(tweet)
        if(debug == True):
            print("Post not uploaded due to debug mode being on")
    if(msg == ""):
        print("Error no message")

tweetit("Fill with your message")

