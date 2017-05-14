import webbrowser

from helpers import authenticate, get_pin, verify_account, get_username, how_many, start_unfollowing, white_list

#open browser
auth_url = authenticate()
webbrowser.get().open(auth_url)

#ask for pin code
print("Submit the verification PIN you received on twitter:")
pin = get_pin()

#verify account
if not verify_account(pin):
    exit(1)        

#do not unfollow these accounts
whitelist = white_list()

#get username
username = get_username()

#ask how many people to unfollow
print("How many users do you want to unfollow? (400 by default)")
amount = how_many()

#unfollow them
start_unfollowing(username, amount, whitelist)