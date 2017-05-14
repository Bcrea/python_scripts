# Simple Twitter Bot to easy unfollow

## Requeriments:

* In order to use this bot you will need to register a [developer account on twitter](https://dev.twitter.com).
* Follow these steps to register your account: [Create a twitter application](http://docs.inboundnow.com/guide/create-twitter-application/).
* Create a file called `config.py` on the same directory where the bot is located, the contents of this file will be the following: <br>
```
key = "YOUR CONSUMER KEY"
secret = "YOUR CONSUMER SECRET KEY"
```
## Usage:
simply run `unfollow_bot.py` on your terminal window, the bot will guide you through every step. <br>
After running the bot your default browser will open the twitter website where you will get a verification pin
then you will be prompted the following message on the console:
```
Submit the verification PIN you received on twitter:
PIN:
```
after submitting the verification pin your account will grant access to the bot so it can start unfollowing people, and then you will be asked the following:
```
How many users do you want to unfollow? (400 by default)
number: 
```

by default the bot is going to start unfollowing your most recent friends, if there are certain accounts you don't want to unfollow open the whitelist.txt file and write line by line the usernames of the people you don't want to unfollow without including `@`:
```
special_person1
special_person2
special_person3
...
...
...
```
save the whitelist.txt file and you're good to go. <br>

