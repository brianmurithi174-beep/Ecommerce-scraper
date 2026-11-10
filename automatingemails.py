import smtplib
from email.message import EmailMessage

# Create email message
email = EmailMessage()
email["From"] = "jgacheri048@gmail.com"  # Use actual email address
recipients = ["brianmurithi174@gmail.com", "brianmurithi754@gmail.com", "sulweemmanuel@gmail.com", "janeforester167@gmail.com"]
email["To"] = ", ".join(recipients)
email["Subject"] = "Daily Updates"

email.set_content("This is an automated email with daily update.")

try:
    # Connect to Gmail SMTP server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()  # Identify yourself to the server
        smtp.starttls()  # Enable TLS encryption
        smtp.ehlo()  # Re-identify after encryption

        # Login with your Gmail credentials
        smtp.login("jgacheri048@gmail.com", "mhcxyyggfchdbczv")

        # Send the email
        smtp.send_message(email)
        print("Email sent successfully!")

except Exception as e:
    print(f"Error sending email: {e}")
