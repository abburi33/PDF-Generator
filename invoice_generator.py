from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    filename = Path(filepath).stem
    name, date = filename.split("-")

    inv_num = f"Invoice nr. {name}"
    inv_date = f"Date {date}"

    pdf.set_font(family="Helvetica", style="B", size=16)

    pdf.cell(w=50, h=8, txt=inv_num, ln=1)
    pdf.cell(w=0, h=12, txt=inv_date, ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1", engine='openpyxl')

    # Add a header
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Helvetica", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=55, h=8, txt=columns[1], border=1)
    pdf.cell(w=45, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Add rows to the tables
    for index, row in df.iterrows():
        pdf.set_font(family="Helvetica", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=55, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=45, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    total_sum = df["total_price"].sum()

    pdf.set_font(family="Helvetica", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=55, h=8, txt="", border=1)
    pdf.cell(w=45, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Helvetica", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

    # Add company name and logo
    pdf.set_font(family="Helvetica", size=14)
    pdf.cell(w=27, h=8, txt=f"PythonHow")
    pdf.image("invoices/pythonhow.png", w=10)

    pdf.output(f"outputs/{name}.pdf")
