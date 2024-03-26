#!/usr/bin/python3

import crypt


# TODO(1)
password = 'yourSudoIsMine9'
# glROPWiu1YFPE

# TODO(2)
salt = crypt.mksalt(crypt.METHOD_CRYPT)

# TODO(3)
hash = crypt.crypt(password, salt)

print(hash)
