# Importing the required libraries
import qrcode
import validators   # Import the validators library for URL validation

# Creating function to collect the link and convert it into a QR Code
def  generate_qrcode(text):
    # Checking if the input text is a valid URL
    if not validators.url(text):
        print('Invalid URL. Please enter a valid URL.')     # Inform the user about the invalid input
        return
    
    try:
        # Creating a QRCode object with specified parameters
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )

        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color = 'black', back_color = 'white')

        img.save('QR Code.png')     #Saving the generated QR Code as an image
        print('QR Code generated successfully!')
    except Exception as e:
        print(f'Error: {e}')

# Taking the user url as an input
url = input('Enter your URL: ')

# Running the function to generate QR code
generate_qrcode(url)