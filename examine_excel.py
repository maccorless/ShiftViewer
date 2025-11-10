import pandas as pd
import sys

def examine_excel(file_path):
    try:
        # Read all sheets
        xls = pd.ExcelFile(file_path)
        print(f"\nExcel file contains {len(xls.sheet_names)} sheet(s): {', '.join(xls.sheet_names)}\n")
        
        # Examine each sheet
        for sheet_name in xls.sheet_names:
            print(f"\n{'='*80}")
            print(f"SHEET: {sheet_name}")
            print(f"{'='*80}")
            
            # Read first few rows
            df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=10)
            
            # Print basic info
            print(f"\nShape: {df.shape} (rows x columns)")
            print("\nFirst 5 rows:")
            print(df.head().to_string())
            
            print("\nColumn names and data types:")
            print(df.dtypes)
            
            # Check for merged cells in first 10 rows and columns
            print("\nSample data (first 10 rows, first 10 columns):")
            print(df.iloc[:10, :10].to_string())
            
    except Exception as e:
        print(f"Error examining Excel file: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        examine_excel(sys.argv[1])
    else:
        print("Please provide the path to the Excel file as an argument.")
