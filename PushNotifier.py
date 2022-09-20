# Import the following modules
from pushbullet import PushBullet
#from pywebio.input import *
#from pywebio.output import *
#from pywebio.session import *
import time

# Get the access token from Pushbullet.com
access_token = "o.Q5r0HKnq9GEPi9Q7ZHqFZScJmzVNbbeF"

def send_push(message):
    # Taking input from the user
    title = "MTA course Listener"

    # Taking large text input from the user
    text = message

    # Get the instance using access token
    pb = PushBullet(access_token)

    # Send the data by passing the main title
    # and text to be send
    push = pb.push_note(title, text)

    # Put a success message after sending
    # the notification

    def clear():
        pb = PushBullet(access_token)


