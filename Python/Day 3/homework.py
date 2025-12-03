is_logged_in=True
is_subscribed=False
user_credits=100
max_credits=200
min_credits =50
credits_valid= (user_credits >= min_credits) and (user_credits<=max_credits) and (user_credits!= min_credits)
bonus_eligible= not (is_subscribed) or (user_credits > min_credits)
user_credits +=50
user_credits -=20
user_credits *=2
user_credits %=150
power_result=user_credits**2
full_access= is_logged_in and is_subscribed
is_true_login= is_logged_in is True
access_result = is_logged_in or is_subscribed and False
print("logged in :",is_logged_in)
print("Subscribed :",is_subscribed)
print("Credits :",credits_valid)
print("Bonus :",bonus_eligible)
print("Final User Credit :",user_credits)
print("Power :",power_result)
print("Full Access :",full_access)
print("Login : ",is_true_login) 
print("Access Result :",access_result)