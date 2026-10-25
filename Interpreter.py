# CW1 Outlook Simulator
#   interpreter Class
#          

# Marthe mayele 

from MailboxAgent import *
import random, string

# Generate a random email body
def gen_bdy():
    snt = '' # the snt here Creates random words that are between 3–10 letters and also choose 1–10 words total
    for i in range(random.randint(1, 10)):
        snt += ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) + ' '
    return f"Body {str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."
 # this Returns the formatted body string.


#this Generates a list of emails that random for the mailbox
def gen_emails():
    """Generate multiple randomly formatted email strings for testing the mailbox """
    msgs, msg_id = [], 0
    for i in range(40): #Outer loop repeats batches
        msg = ''
        for j in range(30): # Inner loop generates 30 emails per batch
            msg += f"ID:{str(msg_id)}\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:tag{random.randint(0, 6)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
            msgs.append(msg) # Appends structured email fields
            msg_id += 1
    return msgs  # this ensures each of the email has a ID that is unique



def display_commands(): # the def Display supports the interpreter commands
    """  """
    print(" The interpreter commands:")
    print(" get <m_id>  | Shows one email")
    print(" lst         | List all of the emails e.g - email87@gre.ac.uk, email15@gre.ac.uk, email6@gre.ac.uk")
    print(" del <m_id>  | Delete all of the email e.g - email35@gre.ac.uk ")
    print(" mv <m_id>   | this Moves email to the archive (if its implemented)")
    print(" mrkr <id>   | Marks the email as read")
    print(" mrku <id>   | Marks the email as unread")
    print(" flt <from>  | Filter by sender")
    print(" fnd <date>  | Find by date")
    print(" add <email> | Adds new email")
    print(" end         | Quit or exits")
    print()

def loop(): #def loop is the Main interpreter loop
    mba = MailboxAgent(gen_emails())   # this Creates the  mailbox with emails generated randomly
    display_commands()

    line = input("mba > ").strip()  # this Reads the first user command
    words = line.split(" ")
    commands, args = words[0], words[1:]

    while commands != "end": # the while command continues to read the commands until the user types in 'end'
        match commands:

    #FA/B.6
            case "add":

                email_str = " ".join(args)
                mba.add_email(email_str)
                print("Email added.")

            case "del":
                mba.delete_email(args[0])  # this deletes an email by ID

            case "flt":
                mba.filter_by_sender(args[0])  # this filters the by sender email

            case "fnd":
                mba.find_by_date(args[0]) # this locates the emails the by date

            case "get":
                mba.get_email(args[0]) # this gets a single email by the ID

            case "lst":
                mba.show_emails() # this list all of the  emails in table form

            case "mrkr":
                mba.mark_read(args[0]) # this mark the email as read

            case "mrku":
                mba.mark_unread(args[0])  # this also marks email as unread

            case "mv":
                mba.move_email(args[0])  # this moves the email to archive (if it is implemented in the MailboxAgent)

            case _:
                print("Unknown command.") # this used as a fallback for commands that are unknown

        line = input("mba > ").strip() # this continues to read the next command
        words = line.split(" ")
        commands, args = words[0], words[1:]

    print("bye!")


if __name__ == "__main__": # the conditional Runs if the interpreter only when this file is executed directly.
    loop()
