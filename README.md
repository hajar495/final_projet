================================== Data Insight Analyzer========================================================
 #### Video Demo:  <URL HERE: https://youtu.be/us-aIBstFOU >
 GITHUB:hajar495
 edX Account: attmanihajar
 first name: Hajar
 last name: Attmani
 City : khenifra
 Country: Morocco
 date:31/01/2026

📌 Project Overview


Data Insight Analyzer is a Python-based tool that automatically analyzes CSV and Excel datasets and generates professional PDF reports with detailed statistical insights.

This project is the Final Project for CS50P (CS50’s Introduction to Programming with Python) and demonstrates:

Object-Oriented Programming (OOP)

Data analysis using pandas

Automated report generation with FPDF

Unit testing with pytest for correctness and reliability

 Program Capabilities

The program performs two main types of analysis:

1️⃣ Numerical Analysis

For all numerical columns, it computes:

Total

Mean

Minimum

Maximum

Median

2️⃣ Categorical Analysis

For all categorical columns, it computes:

Frequency of each unique value

Percentage distribution

All results are stored in a structured dictionary and exported to a well-formatted PDF report.

🛠 How the Program Works
Step 1: User Input

The user provides a dataset file in one of the following formats:

.csv

.xls / .xlsx

Run the program with:

python project.py

Step 2: Data Loading and Analysis
Class: DataAnalyzer

 def __init__(self, filename)
Initializes the analyzer with a filename and prepares empty structures for the dataset and statistics.

 def load_data(self)
Loads CSV or Excel files into a pandas DataFrame. Handles invalid formats, empty files, and encoding issues.

 def numerical_analyze(self)
Identifies numerical columns and computes total, mean, min, max, median. Results stored in self._statis["numeric"].

 def analyze_categorical(self)
Identifies categorical columns and computes frequency and percentage. Results stored in self._statis["categoric"].

statis property
Getter and setter for the statistics dictionary, ensuring a structured output for PDF generation.

Step 3: PDF Report Generation
Class: PDFGenerator

 def __init__(self, title="Data Analysis Report")
Prepares a timestamped PDF file and sets automatic page formatting.

 def generate(self, statis)
Formats the statistics dictionary into a professional PDF report with:

Sections for numerical and categorical analysis

Readable indentation and labels

Clear formatting for presentation

Example generated file:
Report_20250201_143210.pdf

🧪 Unit Testing

The project includes test_project.py using pytest to validate:

Numerical analysis – total, mean, min, max, median

Categorical analysis – frequency counts and percentage

Empty datasets – program handles empty DataFrames gracefully

Tests guarantee the program’s accuracy for a variety of inputs.

📦 Dependencies

This project uses widely-used Python libraries:

pandas – data loading, numerical & categorical analysis

FPDF – PDF generation for reports

datetime – timestamped filenames

sys – safe program termination for invalid inputs

pytest – unit testing framework

Install dependencies via requirements.txt:

pandas
fpdf
pytest


Install all packages:

pip install -r requirements.txt

📂 Project Structure
final_projet/
│
├── project.py          # Main program: data loading, analysis, PDF generation
├── test_project.py     # Unit tests using pytest
├── README.md           # Project documentation
├── requirements.txt    # Required Python libraries

🙏 Acknowledgements

I extend my deepest gratitude to Harvard University and Professor David J. Malan for their exceptional guidance, dedication, and passion throughout CS50.

Their clarity in teaching, commitment to student success, and inspiring enthusiasm made this project possible.

I also sincerely thank the communities of Pandas, FPDF, and pytest for their extensive documentation, tutorials, and support. Their resources were invaluable in understanding library functions and implementing a robust and professional solution.

Thank you all for opening doors to knowledge, for inspiring curiosity, and for making programming both challenging and rewarding.
