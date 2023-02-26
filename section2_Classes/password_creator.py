"""Does stuff"""


from typing import Optional
import string
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class PasswordCreator:
    """
    This class will contain functions to create a password
    """

    def __init__(self, length: Optional[int] = 8, strength: Optional[str] = "mid"):
        """
        Basic attributes from the instance of the class
        Args:
            strength (str): strength of the password ["low", "mid", "high"]
            length (int): Optional in case the user wants to define the length of the password
        """
        if strength == "low" and length is not None:
            self.length = length
            self.strength = "low"
            self.allowed_chars = string.ascii_letters
        elif strength == "low" and length is None:
            self.length = 8
            self.strength = "low"
            self.allowed_chars = string.ascii_letters
        elif strength == "mid" and length is not None:
            self.length = length
            self.strength = "mid"
            self.allowed_chars = string.ascii_letters + string.digits
        elif strength == "mid" and length is None:
            self.length = 12
            self.strength = "mid"
            self.allowed_chars = string.ascii_letters + string.digits
        elif strength == "high" and length is not None:
            self.length = length
            self.strength = "high"
            self.allowed_chars = (
                string.ascii_letters + string.digits + string.punctuation
            )
        elif strength == "high" and length is None:
            self.length = 16
            self.strength = "high"
            self.allowed_chars = (
                string.ascii_letters + string.digits + string.punctuation
            )

    def create_password(self):
        """
        This function will create password based on the attributes of the class istance
        """
        passcode = ""
        passcode = "".join(random.choices(self.allowed_chars, k=self.length))
        while not self.has_required_strength(passcode):
            passcode = self.replace_characters(passcode)

        logging.info("Passcode %s is valid\n", passcode)

        return passcode

    def has_required_strength(self, passcode: str) -> bool:
        if self.strength == "low":
            condition = any(char.islower() for char in passcode) and any(
                char.isupper() for char in passcode
            )
            if condition:
                pass
            else:
                logging.info("Passcode %s is invalid, replacing characters", passcode)

            return condition

        elif self.strength == "mid":
            condition = (
                any(char.islower() for char in passcode)
                or any(char.isupper() for char in passcode)
            ) and any((char in string.digits) for char in passcode)
            if condition:
                pass
            else:
                logging.info("Passcode %s is invalid, replacing characters", passcode)
            return condition

        elif self.strength == "high":
            condition = (
                (
                    any(char.islower() for char in passcode)
                    or any(char.isupper() for char in passcode)
                )
                and any((char in string.digits) for char in passcode)
                and any((char in string.punctuation) for char in passcode)
            )
            if condition:
                pass
            else:
                logging.info("Passcode %s is invalid, replacing characters", passcode)
            return condition

    def replace_characters(self, passcode: str) -> str:
        lower_case_indexes = [
            index
            for index, char in enumerate(passcode)
            if char in string.ascii_lowercase
        ]
        upper_case_indexes = [
            index
            for index, char in enumerate(passcode)
            if char in string.ascii_uppercase
        ]
        digit_indexes = [
            index for index, char in enumerate(passcode) if char in string.digits
        ]
        punctiation_indexes = [
            index for index, char in enumerate(passcode) if char in string.punctuation
        ]

        if self.strength == "low":
            logging.info("Old Passcode: %s", passcode)
            if any(lower_case_indexes):
                passcode = passcode.replace(
                    passcode[random.choice(lower_case_indexes)],
                    random.choices(string.ascii_uppercase)[0],
                    1,
                )
            else:
                passcode = passcode.replace(
                    passcode[random.choice(upper_case_indexes)],
                    random.choices(string.ascii_lowercase)[0],
                    1,
                )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "mid"
            and ((upper_case_indexes) or (lower_case_indexes))
            and not digit_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choice(lower_case_indexes + upper_case_indexes)
            passcode = passcode.replace(
                passcode[to_replace_index],
                random.choices(string.digits)[0],
                1,
            )
            logging.info("New Passcode: %s", passcode)
        elif (
            self.strength == "mid"
            and not ((upper_case_indexes) or (lower_case_indexes))
            and digit_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choice(digit_indexes)
            passcode = passcode.replace(
                passcode[to_replace_index],
                random.choices(string.ascii_uppercase + string.ascii_lowercase)[0],
                1,
            )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and ((upper_case_indexes) or (lower_case_indexes))
            and not digit_indexes
            and not punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choices(
                lower_case_indexes + upper_case_indexes, k=2
            )
            for index in to_replace_index:
                passcode = passcode.replace(
                    passcode[index],
                    random.choices(string.digits + string.punctuation)[0],
                    1,
                )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and ((upper_case_indexes) or (lower_case_indexes))
            and digit_indexes
            and not punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choice(
                lower_case_indexes + upper_case_indexes + digit_indexes
            )
            passcode = passcode.replace(
                passcode[to_replace_index],
                random.choices(string.punctuation)[0],
                1,
            )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and ((upper_case_indexes) or (lower_case_indexes))
            and not digit_indexes
            and punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choice(
                lower_case_indexes + upper_case_indexes + punctiation_indexes
            )
            passcode = passcode.replace(
                passcode[to_replace_index],
                random.choices(string.digits)[0],
                1,
            )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and not ((upper_case_indexes) or (lower_case_indexes))
            and digit_indexes
            and punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choice(digit_indexes + punctiation_indexes)
            passcode = passcode.replace(
                passcode[to_replace_index],
                random.choices(string.ascii_lowercase + string.ascii_uppercase)[0],
                1,
            )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and not ((upper_case_indexes) or (lower_case_indexes))
            and not digit_indexes
            and punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choices(punctiation_indexes, k=2)
            for index in to_replace_index:
                passcode = passcode.replace(
                    passcode[index],
                    random.choices(
                        string.ascii_lowercase + string.ascii_uppercase + string.digits
                    )[0],
                    1,
                )
            logging.info("New Passcode: %s", passcode)

        elif (
            self.strength == "high"
            and not ((upper_case_indexes) or (lower_case_indexes))
            and digit_indexes
            and not punctiation_indexes
        ):
            logging.info("Old Passcode: %s", passcode)
            to_replace_index = random.choices(digit_indexes, k=2)
            for index in to_replace_index:
                passcode = passcode.replace(
                    passcode[index],
                    random.choices(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.punctuation
                    )[0],
                    1,
                )
            logging.info("New Passcode: %s", passcode)

        return passcode

    def show_input_universe(self):
        """
        This function will just print all allowed chars on the creation of the password
        """
        print(self.allowed_chars)


passcodes_low = []
passcodes_mid = []
passcodes_high = []

for i in range(1000):
    passcodes_low.append(PasswordCreator(length=2, strength="low").create_password())

for i in range(1000):
    passcodes_mid.append(PasswordCreator(length=3, strength="mid").create_password())

for i in range(1000):
    passcodes_high.append(PasswordCreator(length=4, strength="high").create_password())

print(passcodes_low)
print("\n")

print(passcodes_mid)
print("\n")

print(passcodes_high)
print("\n")
print("\n")
