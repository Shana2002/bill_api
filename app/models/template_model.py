class Template:
    template_data={
    1:{"company_name":"A1",
         "email":"A3",
         "contact":"A4",
         "customer":"A7",
         "cus_contact":"A8",
         "start":10,
         "item_col":1,
         "qty_col":5,
         "unit_col":4,
         "price_col":6,
         "no_col_show":True,
         "no_col":1,
         "total":"F28",
         "discount":"F29",
         "sub_totla":"F30"},
    2:{"company_name":"A1",
         "email":"A5",
         "contact":"A4",
         "customer":"A8",
         "cus_contact":"A9",
         "start":16,
         "item_col":1,
         "qty_col":6,
         "unit_col":7,
         "price_col":8,
         "no_col_show":False,
         "total":"H31",
         "discount":"H32",
         "sub_totla":"H34"}
}
    def __init__(self,template_id):
        self.id = template_id
        self.company_name = Template.template_data[self.id]["company_name"]
        self.email = Template.template_data[self.id]["email"]
        self.contact = Template.template_data[self.id]["contact"]
        self.customer = Template.template_data[self.id]["customer"]
        self.cus_contact = Template.template_data[self.id]["cus_contact"]
        self.start = Template.template_data[self.id]["start"]
        self.item_col = Template.template_data[self.id]["item_col"]
        self.qty_col = Template.template_data[self.id]["qty_col"]
        self.unit_col = Template.template_data[self.id]["unit_col"]
        self.price_col = Template.template_data[self.id]["price_col"]
        self.no_col_show = Template.template_data[self.id]["no_col_show"]
        self.no_col = Template.template_data[self.id].get("no_col",0)
        self.total = Template.template_data[self.id]["total"]
        self.discount = Template.template_data[self.id]["discount"]
        self.sub_totla = Template.template_data[self.id]["sub_totla"]

