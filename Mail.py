# CW1 Outlook Simulator
#   Mail Class
#         

# Marthe mayele

# this Boolean here indicates whether the email is important
# this Boolean indicates whether the email is read or unread.

class Mail:
    """ the mail class here allows """
    def __init__(self,m_id, frm, to, date,subject,tag,body):
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._date = date
        self._subject = subject
        self._tag = tag
        self._body = body
        self._flag = False
        self._read = False

    def __str__(self):
        return f"m_id:{self.m_id}\tfrom:{self.frm} \t|{self.to} \t {self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self, value):
        self._read = value

    @flag.setter
    def flag(self, value):
        self._flag = value





 # partner A task

# FA.2
    def show_email(self): # the
        """ this displays all the email details in the required format """
        # this method prints allows each of the attribute of the email in a clear, labelled format,
        # which allows the user to view the full contents of a specific email.

        print("ID:", self.m_id)  # Print the unique email ID
        print("From:", self._frm)  # Print sender address
        print("To:", self._to) # Print receiver address
        print("Date:", self.date) # Print the date the email was sent
        print("Subject:", self.subject)  # Print the email subject line
        print("Tag:", self.tag)  # Print the current tag/folder the email is stored in
        print("Body:", self.body) # Print the message body content
        print("Flag:", self.flag)  # Print whether the email is flagged
        print("read:", self.read) # Print whether the email has been read


if __name__ == "__main__":
    # creates a test email
    test_mail = Mail(
        m_id="28",
        frm="email2@gre.ac.uk",
        to="email64@gre.ac.uk",
        date="20/11/2025",
        subject="subject63",
        tag="tag 66",
        body="body139. kavikaybh idnk swoiabkao favhkais."
    )

    # display it
    test_mail.show_email()


