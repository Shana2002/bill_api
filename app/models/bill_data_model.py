from datetime import datetime
class BillData:
    def __init__(self,data):
        self.template = data.get("template",1)

        # invoice number
        self.invoice_num = data.get("invoice",str(int(datetime.now().timestamp())))
        # company details
        company_details = data.get("company",{})
        self.company_name = company_details.get("company_name","")
        self.company_email = company_details.get("company_email","")
        self.company_contact = company_details.get("company_contact","")

        # customer details
        customer_details = data.get("customer",{})
        self.customer_name = customer_details.get("customer_name","")
        self.customer_contact = customer_details.get("customer_contact","")
        self.customer_email = customer_details.get("customer_email","")

        # items
        self.items = data.get("items",[])

        #discount
        discount = data.get("discount",0)
        if discount>=0:
            self.discount = discount
        else :
            self.discount = discount*100

        #whats app sent
        self.is_send_whatsapp = False
        sentwhatsapp = data.get("sentwhatsapp")
        message = (
                    f'{datetime.now().strftime("%m/%d/%Y %H:%M")} Your invoice number is: '
                    f'{self.invoice_num}. Thank you for choosing us.\n\n'
                    f'{self.company_name}\n{self.company_contact}\n{self.company_email}'
                )
        if sentwhatsapp:
            if isinstance(sentwhatsapp, str):
                self.whats_number = sentwhatsapp
                self.message = message
                self.is_send_whatsapp = True
            elif isinstance(sentwhatsapp, dict):
                self.whats_number = sentwhatsapp.get("mobile", "")
                self.message = sentwhatsapp.get("message", message)
                if self.whats_number :
                    self.is_send_whatsapp = True


        #whats app sent
        self.is_send_email = False
        mail_data = data.get("sentemail")
        mail_body = (
                    f'{datetime.now().strftime("%m/%d/%Y %H:%M")} Your invoice number is: '
                    f'{self.invoice_num}. Thank you for choosing us.\n\n'
                    f'{self.company_name}\n{self.company_contact}\n{self.company_email}'
                )
        mail_subject = f"Thank you for choosing us {self.company_name}"
        if mail_data:
            if isinstance(mail_data,str):
                self.reciver_mail  = mail_data
                self.mail_body = mail_body
                self.mail_subject = mail_subject
                self.is_send_email=True
            elif isinstance(mail_data,dict):
                self.reciver_mail = mail_data["email"]
                self.mail_body = mail_data.get("body",mail_body)
                self.mail_subject = mail_data.get("subject",mail_subject)
                if self.reciver_mail:
                    self.is_send_email=True
