class Email():
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def is_send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
command = input()

while command != 'Stop':
    current_command = command.split(' ')
    sender_name = current_command[0]
    receiver_name = current_command[1]
    content_text = current_command[2]
    email = Email(sender_name, receiver_name, content_text)
    emails.append(email)
    command = input()

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].is_send()

for email in emails:
    print (email.get_info())




