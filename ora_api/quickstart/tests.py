from django.test import TestCase

# Create your tests here.

# Responsibilities:
'''
NodeJs will handle user while django handles game

     STAGE 1
User Sign up and Sign In - nodejs 
        '
        v
Authentication - nodejs
        '
        v
Get game history - will run as user visits page which comes after authentication which will load the game
{
    last_draws : 21,
    last 10 winners : [],
    ...get everything 
}

Get user history - basic history after authentication and others as user visits page for the first time
{
    user_current_balance
}
        '
        v

     STAGE 2
User Sign up and Sign In - nodejs 
        '
        v

'''

''' NOTES

Normalize using last_response_time and last_response_value to always query the server and
see if we will need to fetch updated data and will also make it easier to get updated data


'''