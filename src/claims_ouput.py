import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk

# Hide the root window
root = Tk()
root.withdraw()

# Open file dialog to select CSV file
input_csv = askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select the input CSV file")
if not input_csv:
    print("No file selected. Exiting.")
    exit()

# Open file dialog to select output Excel file for correct claims
output_excel_correct = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Save the correct claims Excel file as")
if not output_excel_correct:
    print("No file selected. Exiting.")
    exit()
output_excel_correct = output_excel_correct.replace(".xlsx", " - Accepted Claims.xlsx")

# Open file dialog to select output Excel file for rejected claims
output_excel_rejected = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Save the rejected claims Excel file as")
if not output_excel_rejected:
    print("No file selected. Exiting.")
    exit()
output_excel_rejected = output_excel_rejected.replace(".xlsx", " - Rejected Claims.xlsx")

# Load the CSV file into a DataFrame
df = pd.read_csv(input_csv)

# Assuming 'status' column exists and contains 'accepted' or 'rejected'
accepted_claims = df[df['status'] == 'accepted']
rejected_claims = df[df['status'] == 'rejected']

# Save the DataFrames to Excel files
#change
accepted_claims.to_excel(output_excel_correct, index=False)
rejected_claims.to_excel(output_excel_rejected, index=False)

print("Files saved successfully.")