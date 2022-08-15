from twilio.rest import Client 
 
account_sid = 'ACCOUNT_SID' 
auth_token = 'AUTH_TOKEN' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                                  from_='whatsapp:+1**********',  
                                  body=' Hello Namsthe Whatsapp! ',      
                                  to='whatsapp:+91**********' 
                              ) 
     
    print(message.sid)
