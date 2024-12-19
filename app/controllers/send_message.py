from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv
baseurl= os.getenv("BASE_URL")

def send_whatsapp(file_name,data):
    sid = os.getenv("TWILLO_SID")
    authToken = os.getenv("TWILLO_AUTH_TOKEN")
    client = Client(sid,authToken)
    print(baseurl)
    try:
        message = client.messages.create(
            to=f"whatsapp:{data.whats_number}",
            from_="whatsapp:+14155238886",
            body=f"{data.message}",
            media_url=[f"https://0836-112-135-79-121.ngrok-free.app/get/output_pdf/{file_name}.pdf"]
            )
        return True
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return False