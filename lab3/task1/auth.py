# Main authentication routines
# Do not modify this file!


import base64
import time

from Crypto.Cipher import AES


# Analyze this function to find the vulnerability!
def check_password1(password: str) -> bool:
    """
    A timing side-channel attack vulnerable password checking routine.
    """
    if len(password) != len(SECRET_PASSWORD):
        return False

    correct_password = True
    for i in range(len(SECRET_PASSWORD)):
        if SECRET_PASSWORD[i] != password[i]:
            correct_password = False

    if correct_password:
        return True
    return False


# Analyze this too!
def check_password2(password: str) -> bool:
    """
    Another timing side-channel attack vulnerable password checking routine.
    """
    if len(password) != len(SECRET_PASSWORD):
        return False

    for i in range(len(SECRET_PASSWORD)):
        if not compare_chars(password[i], SECRET_PASSWORD[i]):
            return False
    return True


# ----------------------------------------------------
# The rest of this file is not relevant to the attack.
# ----------------------------------------------------


def compare_chars(c1: str, c2: str) -> bool:
    """
    Compares two characters in a way that is vulnerable to timing attacks.
    """
    duration = 0.00001

    end_time = time.time() + duration
    while time.time() < end_time:
        pass

    return c1 == c2


def init_password() -> None:
    """
    Initializes the SECRET_PASSWORD variable.
    """
    # HEY, DON'T CHEAT!
    global SECRET_PASSWORD

    key = base64.b64decode("YLqYjHSxHgH8wrzcPh3jH07onvlFn8ohhQfpULPNhGM=")
    data = base64.b64decode("auSkbCpPQDtaVS8kDq563Q==")

    cipher = AES.new(key, AES.MODE_ECB)

    decrypted_data = cipher.decrypt(data)
    padding = decrypted_data[-1]

    # DON'T PEEK AT THE PASSWORD!
    SECRET_PASSWORD = decrypted_data[:-padding].decode()
    print("PSWD: " + SECRET_PASSWORD)
