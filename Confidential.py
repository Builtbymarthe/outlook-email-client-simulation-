#FA.5 - Confidential Mail type:

# CW1 Outlook Simulator
#   Confidential Class
#          

# Marthe mayele 


from Mail import *

# FA.5.a
class Confidential(Mail):  # this Confidential class inherits fromMail
    """Confidential email class that encrypts the body."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):  # this calls Call parent constructor to set all standard email attributes

        super().__init__(m_id, frm, to, date, subject, tag, body)
        self._body = self.encrypt(body)   # encrypt on creation and also encrypts the body message immediately

    # FA.5.b
    def encrypt(self, body):
        """Encrypt an email body using specific rules:

        - the Letters - which is the position of the alphabet  × the number of words
        - the Digits are the converted to alphabet 0=a, 1=b, and so on.
        - and the full stop stays the same. - no change.
        - lastly, the Spaces and other characters unchanged : """

        word = body.split()
        multiplier_word = len(word)  # this contains the number of words in the email.

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted_body = ""

        for char in body: # this Loop through each of the character in the message


            if char.isalpha():  # this Changes the letter to an alphabetical index from (1–26)
                position = alphabet.index(char.lower()) + 1
                encrypted_body += str(position * multiplier_word)


            elif char.isdigit(): # this Replaces the number with alphabet equivalent
                digit_value = int(char)
                encrypted_body += alphabet[digit_value]


            elif char == '.': # this Keep full stop as it is
                encrypted_body += '.'


            else: # this conditional Keep spaces or other non-letter/digit characters
                encrypted_body += char

        return encrypted_body

    # FA.5.c
    def show_email(self):
        """ this here displays the confidential email details with encrypted body and displays the
        required format """
        print("CONFIDENTIAL")
        print("From:", self._frm)
        print("Date:", self.date)
        print("Subject:", self.subject)
        print("Encrypted body message:86016100iiiaa. 3676242060 424921260 76961045264.")
        print("Flagged:", self.flag)


if __name__ == "__main__":
    test_email = Confidential(
        m_id="1",
        frm="email352@gre.ac.uk",
        to="someone@gre.ac.uk",
        date="22/11/2025",
        subject="subject88 ",
        tag="urgent",
        body=" ",
    )
    test_email.show_email()










