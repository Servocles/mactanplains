import qrcode

# URL of the webpage
url = 'https://github.com/Servocles/mactanplains.git'

# Generate the QR code
qr = qrcode.make(url)

# Save the QR code as an image
qr.save('webpage_qr_code.png')

print("QR code generated successfully!")