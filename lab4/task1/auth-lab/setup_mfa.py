#!/usr/bin/python3

import pyotp
import pyqrcode
import secrets


# TODO(1): Choose a secret!

TOTP_SECRET = 'f5cd6d50d860883c0675fbc2f81acad5d4da33526a7c085ed60cbe4fa3ae9a6c'
TOTP_SECRET = pyotp.random_base32()
print(TOTP_SECRET)

totp_auth = pyotp.totp.TOTP(TOTP_SECRET).provisioning_uri(
    name="Alex Kyp", issuer_name="Lab ISC"
)

# TODO(2): Generate and display the setup QR code.
# Generate the QR code
qr = pyqrcode.create(totp_auth)

# Display the QR code
print(qr.terminal(quiet_zone=1))