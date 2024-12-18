from flask import Flask,send_from_directory
import os

app = Flask(__name__)

from app.controllers import bill_controller
@app.route('/get/output_pdf/<filename>')
def download_pdf(filename):
    pdf_directory = os.path.join(os.getcwd(), 'assets/output_pdf')
    return send_from_directory(directory=pdf_directory, path=filename, as_attachment=True)