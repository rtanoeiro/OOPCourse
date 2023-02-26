"""Does stuff"""

from typing import Optional
import string
import random


class PasswordCreator:
    """
    This class will contain functions to create a password
    """

    def __init__(self, length: Optional[int], strength: Optional[str] = "mid"):
        """
        Basic attributes from the instance of the class
        Args:
            strength (str): strength of the password ["low", "mid", "high"]
            length (int): Optional in case the user wants to define the length of the password
        """
        self.strength = strength
        if isinstance(length, int):
            self.length = length
        elif strength == "low":
            self.length = 8
        elif strength == "mid":
            self.length = 12
        elif strength == "high":
            self.strength = 16

        self.allowed_chars = string.ascii_lowercase + string.digits + string.punctuation

    def create_password(self):
        """
        This function will create password based on the attributes of the class istance
        """
        passcode = ""
        if self.strength == "low":
            for _ in range(self.length):
                passcode = passcode + random.choice(string.ascii_letters)
            while (string.ascii_lowercase not in passcode) and (
                string.ascii_uppercase not in passcode
            ):
                if string.ascii_lowercase not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.lower())
                else:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.upper())

        elif self.strength == "mid":
            for _ in range(self.length):
                passcode = passcode + random.choice(
                    string.ascii_letters + string.digits
                )
            while (
                (string.ascii_lowercase not in passcode)
                and (string.ascii_uppercase not in passcode)
                and (string.digits not in passcode)
            ):
                if string.ascii_lowercase not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.lower())
                elif string.ascii_uppercase not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.upper())
                elif string.digits not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, random.choice(string.digits))

        elif self.strength == "high":
            for _ in range(self.length):
                passcode = passcode + random.choice(
                    string.ascii_letters + string.digits
                )
            while (
                (string.ascii_lowercase not in passcode)
                and (string.ascii_uppercase not in passcode)
                and (string.digits not in passcode)
                and (string.punctuation not in passcode)
            ):
                if string.ascii_lowercase not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.lower())
                elif string.ascii_uppercase not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, to_replace.upper())
                elif string.digits not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, string.digits)
                elif string.punctuation not in passcode:
                    to_replace = random.choice(passcode)
                    passcode.replace(to_replace, string.punctuation)

    def show_input_universe(self):
        """
        This function will just print all allowed chars on the creation of the password
        """
        print(self.allowed_chars)
    


passcode1 = 
