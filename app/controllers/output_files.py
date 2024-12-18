from app.init import app
from flask import send_from_directory
import os

@app.route('/get/output_pdf/<filename>')
def download_pdf(filename):
    pdf_directory = os.path.join(os.getcwd(), 'assets/output_pdf')
    return send_from_directory(directory=pdf_directory, path=filename, as_attachment=True)

@app.route('/get/output_excel/<filename>')
def download_excel(filename):
    excel_directory = os.path.join(os.getcwd(),'assets/output_excel')
    return send_from_directory(directory=excel_directory,path=filename,as_attachment=True)