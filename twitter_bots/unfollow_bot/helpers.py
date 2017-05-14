import config, time

from random import randrange
from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError

def authenticate():
    global APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, auth, twitter
    APP_KEY, APP_SECRET = config.key, config.secret
    
    twitter = Twython(APP_KEY, APP_SECRET)
    
    auth = twitter.get_authentication_tokens()
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET = auth['oauth_token'], auth['oauth_token_secret']
    return auth['auth_url']
    
def get_pin():
    while True:
        pin = input("PIN: ")
        if pin.isdigit():
            pin = int(pin)
            break
    return pin

def verify_account(pin_number):
    global APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, auth, twitter
    
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    last_step = twitter.get_authorized_tokens(pin_number)
    
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET = last_step['oauth_token'], last_step['oauth_token_secret']
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    try:
        twitter.verify_credentials()
    except TwythonError as e:
        print(e)
        return False
    
    return True

def get_username():
    global twitter
    
    user = twitter.get_account_settings()
    username = user['screen_name']
    return username

def how_many():
    while True:
        amount = input("number: ")
        if amount.isdigit():
            amount = int(amount)
            break
    return amount

def start_unfollowing(screen_name, amount, whitelist):
    global twitter
    try:
        friends_list = twitter.get_friends_ids(screen_name=screen_name)
    except TwythonError as error:
        print(error)
    except TwythonAuthError as auth_error:
        print(auth_error)

    friends = [friend for friend in friends_list['ids']]

    limit = 0
    i = 0
    while True:
        time.sleep(randrange(21))
        try:
            if friends[i] not in whitelist:            
                twitter.destroy_friendship(user_id=friends[i])            
                friends.pop(i)
                limit += 1
        except TwythonRateLimitError as limit_error:
            print(limit_error)
        i += 1
        if len(friends) < 1:
            break
        if limit == amount or limit == 400:
            break
    print("Success!")
def white_list():
    global twitter
    friends = []
    file = open("whitelist.txt", "r")
    for line in file:
        user = twitter.show_user(screen_name=line.strip("\n"))
        friends.append(user['id'])
    file.close()
    return friends