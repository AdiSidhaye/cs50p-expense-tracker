# 💸 Expense Tracker (CS50P Final Project)

Video URL - https://youtu.be/tGHQLoY2JKs
This is a simple expense tracker application built in Python as a final project for Harvard's CS50P course. The application allows users to:

- Add new expenses  
- Create and manage categories  
- View expense distribution (via plots)

---

## 💻 Technologies Used

- Python 3.13  
- `Tkinter` (GUI)  
- `pandas` (for CSV handling)  
- `matplotlib` (for visualization)  
- `pytest` (for testing)

---

## ✨ Features

- GUI for adding expenses  
- Validation of inputs with error handling  
- Category management (add/check)  
- Plotting pie chart of expenses by category  
- File storage in CSV format  
- Unit tests to validate functions

---

## 📁 Project Structure

- `project.py` – Main application logic  
- `test_project.py` – Unit tests for the app  
- `data/` – Stores `expenses.csv` and `categories.csv`  
- `README.md` – Project description  
- `.gitignore` – Ignored files/folders for Git

---

## 🖼️ Screenshot
<img width="554" alt="image" src="https://github.com/user-attachments/assets/21233e15-e074-47e9-af64-5c31687594ea" />


---

✅ Future Improvements

-Add data filtering by date
-Add more plotting options that allow custom date data plotting
-Export summary reports, with custom dates
-Improve UI using customTkinter or web framework

---

🎓 Developed for

Harvard’s CS50P: Introduction to Programming with Python

---

---

## 🏃‍♂️ How to Run

### 1. Clone the repo:
```bash
git clone <your-repo-url>
cd CS50_expense_tracker
2. Install dependencies (if needed):
pip install pandas matplotlib
3. Run the app:
python project.py
4. Run tests:
pytest test_project.py

