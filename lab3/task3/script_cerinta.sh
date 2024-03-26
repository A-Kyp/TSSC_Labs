#! /bin/bash

# install IsoApplet usign a APDU script
opensc-tool --card-driver default --send-apdu 80b800001a0cf276a288bcfba69d34f310010cf276a288bcfba69d34f3100100
opensc-tool -n

# create PKCS#15 structure on our smart card (also set a PIN and a PUK, for security purposes)
pkcs15-init --create-pkcs15 --so-pin 123456 --so-puk 0123456789abcdef
# generate an RSA key pair to use for signing (note: auth-id is a PIN slot)
pkcs15-init --generate-key rsa/2048  --id 1 --key-usage decrypt,sign --label MyRSAKey --auth-id FF --pin 123456
# download the generated public key to your machine
pkcs15-tool --read-public-key "1" --output "smartcard-pubkey.pem"

echo "Sunt de acord să cedez toată averea mea asistenților de ISC. Adevăraaat\!" > textToSign.txt
openssl dgst -engine pkcs11 -sign "pkcs11:object=MyRSAKey;type=private;pin-value=123456" -keyform ENGINE -sha256 -out textSignature.sig textToS>
# now everyone can check whether the document is correctly signed using the public key:
openssl dgst -sha256 -verify smartcard-pubkey.pem -keyform PEM -signature textSignature.sig textToSign.txt
# modificați fișierul textToSign.txt și re-verificați semnătura digitală... ce se întâmplă?
