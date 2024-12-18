from flask import request
from app.init import app
from app.models.bill_data_model import BillData 
from app.models.template_model import Template
from openpyxl import Workbook,load_workbook
import shutil
import datetime

@app.post('/generate_bill/')
def generate_bill():
    data = request.get_json()
    bill_data = BillData(data)
    # template = Template(bill_data.template)

    file_name  = f"{str(int(datetime.datetime.now().timestamp()))}_{bill_data.customer_name}"

    shutil.copyfile(f"assets/templates_excel/template1.xlsx", f"assets/output_excel/{file_name}.xlsx")
    # workbook = load_workbook(f"outputs/{file_name}.xlsx")
    # sheet = workbook.active



    return ({"data":bill_data.company_name})