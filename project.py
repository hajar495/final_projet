import pandas as pd
from fpdf import FPDF
import datetime
import sys

class PDFGenerator:
    # Class to generate PDF report
    def __init__(self, title="Data Analysis Report"):
        self.title = title
        self.filename = f"Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=10)

    def generate(self, statis):
        # Create the PDF using the statistics dictionary
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", "B", 16)
        self.pdf.cell(0, 10, self.title, ln=True, align="C")
        self.pdf.ln(5)
        self.pdf.set_font("Helvetica", "", 12)

        # Numerical columns
        if statis.get("numeric"):
            self.pdf.set_font("Helvetica", "B", 14)
            self.pdf.cell(0, 8, "=== Numerical Columns ===", ln=True)
            self.pdf.set_font("Helvetica", "", 12)
            for column, values in statis["numeric"].items():
                self.pdf.cell(0, 8, f"Column: {column}", ln=True)
                for key, val in values.items():
                    self.pdf.cell(0, 6, f"  {key.capitalize()}: {val:.2f}", ln=True)
                self.pdf.ln(3)

        # Categorical columns
        if statis.get("categoric"):
            self.pdf.set_font("Helvetica", "B", 14)
            self.pdf.cell(0, 8, "=== Categorical Columns ===", ln=True)
            self.pdf.set_font("Helvetica", "", 12)
            for column, values in statis["categoric"].items():
                self.pdf.cell(0, 8, f"Column: {column}", ln=True)
                for key, v in values.items():
                    self.pdf.cell(0, 6, f"  {key.capitalize()}:", ln=True)
                    for x, y in v.items():
                        self.pdf.cell(0, 6, f"    {x}: {str(y)}", ln=True)
                self.pdf.ln(3)

        self.pdf.output(self.filename)
        print(f"PDF report has been generated successfully: {self.filename}")


class DataAnalyzer:
    
    # Class to analyze CSV or Excel files
    def __init__(self, filename):
        self._filename = filename
        self._df = None
        self._statis = {"numeric": {}, "categoric": {}}

    @property
    def statis(self):
        return self._statis

    @statis.setter
    def statis(self, value):
        if not isinstance(value, dict):
            raise ValueError("Statistics must be a dictionary")
        self._statis = value

    def load_data(self):
        try:
            if self._filename.endswith(".csv"):
                self._df = pd.read_csv(self._filename, engine="python", encoding="utf-8")
            elif self._filename.endswith((".xls", ".xlsx")):
                self._df = pd.read_excel(self._filename)
            else:
                raise ValueError("Invalid file format")

            if self._df.empty:
                raise ValueError("Empty file!!")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def numerical_analyze(self):
        numeric_columns = self._df.select_dtypes(include="number").columns
        for column in numeric_columns:
            series = self._df[column].dropna()
            self._statis["numeric"][column] = {
                "total": series.sum(),
                "mean": series.mean(),
                "min": series.min(),
                "max": series.max(),
                "median": series.median()
            }

    def analyze_categorical(self):
        categorical_columns = self._df.select_dtypes(include=["object","string"]).columns
        for column in categorical_columns:
            freq = self._df[column].value_counts()
            percentage = self._df[column].value_counts(normalize=True) * 100
            self._statis["categoric"][column] = {
                "frequency": freq.to_dict(),
                "percentage": percentage.round(1).to_dict()
            }


def main():
    print("====== Welcome to Data Insight Analyzer - Your Smart CSV & Excel Analysis Tool ======")
    filename = input("Enter the CSV or Excel file you want to analyze: ").strip()

    analyzer = DataAnalyzer(filename)
    analyzer.load_data()
    analyzer.numerical_analyze()
    analyzer.analyze_categorical()

    pdf_gen = PDFGenerator()
    pdf_gen.generate(analyzer.statis)


if __name__ == "__main__":
    main()
