from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv
baseurl= os.getenv("BASE_URL")

def send_whatsapp(file_name):
    sid = os.getenv("TWILLO_SID")
    authToken = os.getenv("TWILLO_AUTH_TOKEN")
    client = Client(sid,authToken)

    try:
        message = client.messages.create(
            to="whatsapp:+94712875690",
            from_="whatsapp:+14155238886",
            body="Hello brohh",
            media_url=[f"{baseurl}/get/output_pdf/{file_name}.pdf"]
            )
        return True
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return False