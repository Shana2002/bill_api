import os
import base64
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from google.oauth2.credentials import Credentials
import datetime

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TOKEN_PATH = f"{os.getcwd()}/assets/api_auth/token.json"
CREDENTIALS_PATH = f"{os.getcwd()}/assets/api_auth/credentials.json"

class SendMail:
    def __init__(self, data, file_name):
        # Initialize email details
        self.subject = f"Invoice from {data.company_name}"
        self.body = f"{datetime.datetime.now().date()} invoice from {data.company_name}"
        self.recipient_email = data.customer_email
        self.file_name = file_name

    def gmail_api_authenticate(self):
        creds = None
        if os.path.exists(TOKEN_PATH):
            try:
                creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
            except ValueError:
                print("Invalid token.json file. Deleting and re-authenticating.")
                os.remove(TOKEN_PATH)
        
        if not creds or not creds.valid:
            if creds and creds.refresh_token and creds.expired:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    print(f"Error refreshing token: {e}")
                    os.remove(TOKEN_PATH)
            if not creds:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
                with open(TOKEN_PATH, 'w') as token:
                    token.write(creds.to_json())
        return creds

    def create_message(self):
        self.message = MIMEMultipart()
        self.message['Subject'] = self.subject
        self.message['From'] = "warriorlk02@gmail.com"
        self.message['To'] = self.recipient_email
        self.message.attach(MIMEText(self.body))

        file_path = os.path.join(os.getcwd(), f'assets/output_pdf/{self.file_name}.pdf')
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist.")
            return None
        
        with open(file_path, 'rb') as file:
            mime_part = MIMEBase('application', 'octet-stream')
            mime_part.set_payload(file.read())
            encoders.encode_base64(mime_part)
            mime_part.add_header('Content-Disposition', f'attachment; filename="{self.file_name}.pdf"')
            self.message.attach(mime_part)

        raw_message = base64.urlsafe_b64encode(self.message.as_bytes()).decode('utf-8')
        return raw_message

    def send_email(self):
        try:
            creds = self.gmail_api_authenticate()
            service = build('gmail', 'v1', credentials=creds)
            message = self.create_message()

            if message is None:
                return  # Exit if message creation failed

            send_message = service.users().messages().send(userId="me", body={'raw': message}).execute()
            print(f"Message Id: {send_message['id']}")
        except HttpError as e:
            print(f"An error occurred: {e}")
