class Email:
    def __init__ (self):
        self.is_sent = False
    
    def send_email(self):
        self.is_sent = True

my_email = Email()
my_email.is_sent
#change object's value
my_email.send_email()
my_email.is_sent