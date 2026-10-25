# CW1 Outlook Simulator
#   MailboxAgent Class
#          

# Marthe mayele 

from Mail import *
from Confidential import *
from personal import *

class MailboxAgent:
    """ """

    def __init__(self,email_data):
        self._mailbox = self.__gen_mailbox(email_data)

    @classmethod
    def __gen_mailbox(cls,email_data): # this returns tHe mailbox as a list which contains the received email as a object
        """generates mailbox data structure
        :ivar: string
        :rtype: list"""
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(
                    msg[0].split(":")[1],
                    msg[1].split(":")[1],
                    msg[2].split(":")[1],
                    msg[3].split(":")[1],
                    msg[4].split(":")[1],
                    msg[5].split(":")[1],
                    msg[6].split(":")[1]
                )
            )
        return mailbox

#Partner A - (Marthe)

    # FA.1
    def get_email(self, m_id):
        """ -  here Returns the email object with the given ID."""
        for email in self._mailbox: # this loops through every email sorted in the mailbox.
            if email.m_id == m_id: # this is used if the emails ID matches the one that where looking for.
                return email # this returns the email object
        return None # if there is no email found with specific id, then return none.


    # FA.3
    def del_email(self, m_id):
        """- this Moves the email with m_id to the bin."""
        for email in self._mailbox: # this looks through all the emails in the mailbox
            if email.m_id == m_id: # this finds the email with the matching ID
                email.tag = "bin" # instead of deleting it, it changes the tag to a bin folder.
                return email # this returns the changed email object.
        return None # if there is no email found with specific id, then return none.

    # FA.4
    def filter(self, frm):
        """- Return list of emails sent from the given address."""
        results = [] # is able to create an empty list of emails in the mailbox.
        for email in self._mailbox: # this loops all emails in the mailbox
            if email.frm == frm: # this checks if the sender matches the specified email address
                results.append(email)  #this adds the matching emails to the result list
        return results # this returns a list of all the emails by that specific address

    # FA.5
    def sort_date(self):
        """this here Return emails sorted by date."""
        from datetime import datetime
        # this mainly sorts the mailbox lists using the email's date - value
        # and also changes the string dd/mm/yyyy into a datetime object for clear sorting.
        return sorted(
            self._mailbox,
            key=lambda email: datetime.strptime(email.date, "%d/%m/%Y")
        )

#Partner B  - (Marthe)
     #FB.1
    def show_emails(self):
        """- Display all emails in a formatted table."""
        # this loops through all email's in the mailbox and prints
        #    the key information in a structured and aligned columns to make the list easy to view and read.


        print("ID:  | From:              | To:                 | Date:        | Subject:          |Tag :  | Body:  ")
        print(" " * 90) # this prints of the title/ header for the table:

        for email in self._mailbox:
            print(f"{email.m_id:<4}| "
                  f"{email.frm:<20}| "
                  f"{email.to:<20}| "
                  f"{email.date:<13}| "
                  f"{email.subject:<18}| "
                  f"{email.tag}  | "
                  f"{email.body:<20}") # this prints of each of the email in a formatted row / table structure going down.


    # FB.2
    def mv_email(self, m_id, tag):
        """- this Moves the email to another tag/folder."""
    # the method used here finds the email using get_email() and updates its tag.
    # This simulates moving emails between folders like inbox, bin, conf, prsnl, etc.
        email_to_move = self.get_email(m_id)
        if email_to_move:
            email_to_move.tag = tag # used to change the folder
            return True
        return False



    # FB.3
    def mark(self, m_id, status):
        """- this Marks email as read or unread."""
        # the method used here updates the attribute "read" of the email.
        email_to_mark = self.get_email(m_id)
        if email_to_mark:
            email_to_mark.read = status # this specifically marks it as true or false.
            return True
        return False



    # FB.4
    def find(self, date):
        """- this Returns a list of emails received on a given on a certain date."""
    #and this mainly loops through the whole mailbox and collects emails whose date matches the given date string exactly.
        matches = []
        for email in self._mailbox:
            if email.date == date:
                matches.append(email)
        return matches



    # FB.5
    def sort_from(self):
        """this used to Sort the mailbox in place by sender email address."""
        self._mailbox.sort(key=lambda email: email.frm) # this uses the built in sort() and lamda key

#FA.6
#Both partner A and B:

    def add_email(self, frm, to, date, subject, tag, body):
        """this Creates a  email with unique ID and adds that to the mailbox."""

        #the method used here/integrated:

        # this automatically generate/ creates an email ID that is unique based on the size of the mailbox.
        #when Choosing the correct class email using the inheritance ( Mail, Personal or Confidential).
       #this also makes sure that all new emails are stored in the shared mailbox so all FA/FB features can access them.

        new_id = len(self._mailbox) # The ID is generated by counting how many emails already exist

        match tag.lower():
            # The match-case structure here selects the right class which is based on the tag.
            # This shows both inheritance + polymorphism.

            case "conf": # this creates the Confidential email object
                new_email = Confidential(new_id, frm, to, date, subject, tag, body)

            case "prsnl": # this creates the Personal email object
                new_email = Personal(new_id, frm, to, date, subject, tag, body)

            case _: # this creates a normal Mail object
                new_email = Mail(new_id, frm, to, date, subject, tag, body)

        self._mailbox.append(new_email) # this creates a email object into the mailbox list


if __name__ == "__main__": # this allows me to test all of the features in And B
    email_data = [
        "ID:0\nFrom:email5@gre.ac.uk\nTo:email46@gre.ac.uk\nDate:9/8/2025\nSubject:subject48\nTag:tag1\nBody:Body95.tusjhsu  yagdhai uagcsjaj zxysujwhujw",
        "ID:1\nFrom:email8@gre.ac.uk\nTo:email178@gre.ac.uk\nDate:16/4/2025\nSubject:subject12\nTag:tag2\nBody:Body167.ckhsin jsavyhsm  ushujad  yshakbdv",
        "ID:2\nFrom:email29@gre.ac.uk\nTo:email14@gre.ac.uk\nDate:4/6/2025\nSubject:subject34\nTag:tag3\nBody:Body135.qbdjs dbsbssuvd ubjcsksy cbskfbdy",
        "ID:3\nFrom:email16@gre.ac.uk\nTo:email70@gre.ac.uk\nDate:24/7/2025\nSubject:subject83\nTag:tag4\nBody:Body44.pbdhjs mjbhsmai shbajdnakd javdksb",
        "ID:4\nFrom:email7@gre.ac.uk\nTo:email132@gre.ac.uk\nDate:18/5/2025\nSubject:subject95\nTag:tag5\nBody:Body198.gugahi udguand hnabkdsyb ubsjhshkd",
        "ID:5\nFrom:email56@gre.ac.uk\nTo:email19@gre.ac.uk\nDate:30/2/2025\nSubject:subject17\nTag:tag6\nBody:Body174.ugsjdh hsus usvaihdu hihshis yajhi",
        "ID:6\nFrom:email9@gre.ac.uk\nTo:email88@gre.ac.uk\nDate:7/2/2025\nSubject:subject62\nTag:tag7\nBody:Body88.yvvsjhg hsg jvyhjsv yvakdbhsn yvbjs",
        "ID:7\nFrom:email10@gre.ac.uk\nTo:email14@gre.ac.uk\nDate:3/9/2025\nSubject:subject86\nTag:tag8\nBody:Body038.vajbusu ihg bsisjdy isgei ohskajhd",
        "ID:8\nFrom:email8@gre.ac.uk\nTo:email11@gre.ac.uk\nDate:29/10/2025\nSubject:subject11\nTag:tag9\nBody:Body345.kffwhsb suvs nknsnsbjbyhs bsiabusvh",


    ]
    agent = MailboxAgent(email_data)
    agent.show_emails()
