import qrcode

# 1. SET YOUR URL HERE
# This should be your GitHub Pages link
github_url = "https://chbo70.github.io/christmas-gift/"

# 2. CONFIGURE THE QR CODE
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. ADD DATA
qr.add_data(github_url)
qr.make(fit=True)

# 4. CREATE IMAGE (Using your website colors)
# fill_color is the QR code itself, back_color is the background
img = qr.make_image(fill_color="#ff4d6d", back_color="#ffdae0")

# 5. SAVE
img.save("christmas_qr.png")

print(f"✨ Success! QR code for {github_url} saved as christmas_qr.png")