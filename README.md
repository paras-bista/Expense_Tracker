# Expense Tracker

A simple web-based **Expense Tracker** application built with Django.  
Track your income, expenses, and see your current balance in real time.

---

## Features

- Add new income and expense transactions  
- View transaction history with descriptions and amounts  
- Calculate and display total income, expenses, and balance  
- Delete transactions  
- Responsive and clean UI

---

## Project Structure

- `expensetacker/` — Main Django project folder  
- `tracker/` — Django app containing core functionality  
- `static/` — Static files like CSS and images  
- `db.sqlite3` — SQLite database file  
- `manage.py` — Django management script

---

## Installation

1. Clone the repository:  
   ```bash
   git clone <repo_url>
   cd <repo_folder>
2. Create and activate a virtual environment (optional but recommended):
   
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3.Install dependencies:

pip install -r requirements.txt

4.Run migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver
Open your browser at http://127.0.0.1:8000/ to access the app.

Usage
Use the form to add new transactions (use negative amounts for expenses).

See the updated balance, income, and expenses instantly.

Delete transactions by clicking the trash icon.

Contributing
Feel free to fork this repository and submit pull requests.
For major changes, please open an issue first to discuss what you want to change.

License
This project is open source and free to use.
