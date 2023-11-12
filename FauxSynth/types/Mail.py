
class Mail:

    content: str

    def __init__(self, handler, title: str, sender: str, mail_id: int):
        self.handler = handler
        self.title = title
        self.sender = sender
        self.mail_id = mail_id

    def __str__(self):
        return f"<Mail {self.mail_id} | {self.title} / {self.sender} >"

    def get_content(self):
        self.content = self.handler.get_mail(self.mail_id)
        return self.content

