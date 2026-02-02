Author

Jabir Hussain
MCA (AI&IOT) | NIT PATNA
#  Admission Management System (Django)

A role-based Admission Management System built using Django, designed to handle student admissions, payments, and admin approvals in a real-world workflow.

This project is being developed step-by-step with industry best practices, focusing on clean architecture, scalability, and interview readiness.

---

##  Features

###  Student
- User registration & login
- Fill admission form
- Pay admission fees
- Track admission status
- Access student dashboard after approval

###  Admin
- View all admission applications
- Approve / reject students
- Verify payments
- Send approval emails
- Manage system via Django Admin

---

##  Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (development), PostgreSQL (production-ready)
- **Authentication:** Django Auth (User model)
- **Forms:** Django Forms
- **Payments:** Test-mode payment gateway (planned)
- **Email:** SMTP (planned)
- **PDF:** Admission receipt generation (planned)
- **Version Control:** Git & GitHub

---

##  Project Structure

```text
admission_portal/
│
├── accounts/     # Authentication & user roles
├── admission/    # Admission form & workflow
├── payments/     # Payment handling
├── dashboard/    # Student & admin dashboards
│
├── admission_portal/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── .gitignore


** How  to run project Locallly **

git clone https://github.com/YOUR_USERNAME/admission-management-system.git
cd admission-management-system


python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



How to Run the Project Locally


 ___________________DAY_3______________________________
 ## Day 3 Progress
- User registration & login
- Role-based Profile model
- Auto profile creation using Django signals
- Bootstrap integrated for UI
