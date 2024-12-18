class BillData:
    def __init__(self,data):
        self.template = data.get("template",1)

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
        if data.get("sentwhatsapp","")!="":
            self.is_send_whatsapp = True
            self.whats_number = data["sentwhatsapp"]
        

        #whats app sent
        self.is_send_email = False
        if data.get("sentemail","")!="":
            self.is_send_email = True
            self.send_email = data["sentemail"]
