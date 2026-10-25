# CW1 Outlook Simulator
#   personal Class
#           

# Marthe mayele 

from Mail import *

class Personal(Mail):
    """Represents the personal email type and appends statistics to the body."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        super().__init__(m_id, frm, to, date, subject, tag, body)
        self._body = self.add_stats(body)     # overwrite original body

    # FB.5.b
    def add_stats(self, body):
        """Replace 'Body' with UID_string  and add text statistics."""

        # this extracts the uid_string from body
        uid_string = self._frm.split("@")[0]

        # this replaces the word "Body" with UID_string
        modified_body = body.replace("Body", uid_string)

        # this split the  words into individual words for analysis
        word = modified_body.split()

        if len(word) == 0: # If there are no words, return unchanged body
            return modified_body

        # calculates the statistics of text
        word_lengths = [len(w) for w in word]  # - this list each of the word's length
        word_count = len(word)  # - is the number of words
        average_length = sum(word_lengths) // word_count # - average word length (integer division)
        longest_word = max(word_lengths)  # longest word length

        # this creates a formatted summary stats text.
        stats_text = (
            f" Stats: Word count:{word_count}," f" Average word length:{average_length}," f" Longest word length:{longest_word}."
        )

        return modified_body + stats_text # this Returns the  changed body which including stats

    # FB.5.c
    def show_email(self):
        """the def show_email displays the personal email in required the  format."""
        print("PERSONAL")
        print("From:", self._frm)
        print("Date:", self.date)
        print("Subject:", self.subject)
        print("Body:", self.body)
        print("read:", self.flag) # this shows whether the email is flagged or not flagged


if __name__ == "__main__":
    prsn = Personal(
        m_id="2",
        frm="email142@gre.ac.uk",
        to="friend@gre.ac.uk",
        date="2025-11-20",
        subject="Subject64",
        tag="personal",
        body="Body11332. Isfffffeo sxzmp."

    )
    prsn.show_email()

