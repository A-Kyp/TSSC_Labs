#!/usr/bin/python3

import grp
import hashlib
import os
import pyotp
import sys


PASSWORD_HASH = "13412ffd6149204f40e546ffa9fbd7124b410198a6ba3924f788622b929c8eb2"
# poochiedontsurf
"TODO" # TODO(7.1): Choose a secret!
TOTP_SECRET = 'KHDSCSATFRPUPKVTVPIGFJHSQCWSFPVC'

def generate_sha256_hash(text):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes-like object representing the text
    sha256_hash.update(text.encode('utf-8'))

    # Retrieve the hexadecimal representation of the hash digest
    hashed_text = sha256_hash.hexdigest()

    return hashed_text

def login():
    user = os.environ.get("PAM_USER")

    user_groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]

    # TODO(6.1): We want this script to be used only for our special group of users.
    special_group = 'top_10_manelisti'
    if special_group not in user_groups:
        return False
    
    user_secret = input()
    user_password = user_secret[:-6]
    
    # TODO(7.2): Extract the password and the TOTP. Hint: you know the length of the TOTP.
    user_totp = user_secret[-6:]


    # TODO(6.2): Calculate the hash of the provided password.
    user_hash = generate_sha256_hash(user_password)
    print(user_hash)

    if user_hash != PASSWORD_HASH:
        print("Ai gresit buzunarul!")
        return False

    # TODO(7.3): Check the TOTP from the user and uncomment the code below.
    otp_checker = pyotp.TOTP(TOTP_SECRET)
    totp_correct = otp_checker.verify(user_totp)
    
    if not totp_correct:
       print("S-a rezolvat, nu se poate!")
       return False

    print("Ma distrez si bine fac!")
    return True


if __name__ == "__main__":
    sys.tracebacklimit = 0

    if not login():
        raise Exception("Python script rejected login: trying default authentication")
