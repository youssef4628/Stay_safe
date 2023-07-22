import smtplib
from getpass import getpass
info=register()
state = input()
current=1
battery = 0
co2=0
lock=0
state = False


def register():
    user_email=input("what is your email:")
    while len(user_pass)<8 :
        user_pass=getpass("what is your pass")
    confirm =getpass("confirm your password")
    while confirm != user_pass:
        print("please enter the same pass")
        confirm =getpass("confirm your password")
    info=[user_email,user_pass]
    return info

def login ():
    user_email= input("The email")
    user_pass=getpass("what is your password")
    # check if the pass is correct and if the email is foud 
    return [user_pass,user_email]
    
    
    

def turn_off ():
    global current
    battery=1
    current=0
    co2=1

def put_out ():
    lock=1
    co2=1
    
def call_for_help(user_email,user_pass):
    # Email details
    sender_email = user_email # Write your email
    sender_password = user_pass # Your password
    receiver_email = "essam2007moh@gmail.com" # Email of police
    subject = "Emergency: Fire in a Home" # sended title
    body = "There is a fire in a home at location at cairo, Please send help immediately."
    # Body
    # SMTP server details
    smtp_server = "smtp.gmail.com" # Server of emergency in your counter
    smtp_port = 465
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start TLS encryption
        server.starttls()
    # Login to the email account
        server.login(sender_email, sender_password)
    # Construct the email message
        message = f"Subject: {subject}\n\n{body}"
    # Send the email
        server.sendmail(sender_email, receiver_email, message)

def thermal_cam():
    t= input()
    if t >850:
        turn_off()
    else:
        put_out()

def main ():
    global info
    call_for_help(info[0],info[1])
    thermal_cam()


if state == True:
    main ()
