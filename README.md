# PDUAM Central Library Management System
**Institution:** Pandit Deendayal Upadhyaya Adarsha Mahavidyalaya (PDUAM), Amjonga, Goalpara, Assam, India.  
**Affiliation:** Gauhati University  
**Technology Stack:** Python 3.10+, Flask 3.1, SQLite, Bootstrap 5.3, Chart.js, OpenPyXL, ReportLab, Werkzeug.

---

## 1. Overview & Architecture

The **PDUAM Central Library Management System** is an enterprise-grade digital library management platform engineered for Pandit Deendayal Upadhyaya Adarsha Mahavidyalaya, Amjonga. The system provides separate portals for **Librarians** and **Student Members**, a public **OPAC (Online Public Access Catalogue)**, individual physical copy **Accession Number Tracking**, circulation (borrowing, returning, renewals, reservations), automated two-tier overdue fines, bulk member importing via Excel/CSV, a digital thesis/e-resource repository, and comprehensive reporting with instant CSV, Excel (.xlsx), and PDF exports.

### Key Highlights
- **Institutional Branding:** Features the official college logo, academic navy & light blue palette, institutional headers, and print-ready receipts.
- **Strict Role-Based Access Control (RBAC):** Server-enforced permissions for Public Visitors, Student Members, and Librarians.
- **Physical Copy Accession Tracking:** Every copy is assigned a unique accession number (e.g., `PDUAM-2026-CS-001-01`), tracking barcode, physical condition (Good, Fair, Damaged, Lost), and shelf/rack location.
- **Automated Fine Calculations:** Configurable two-tier overdue fine policy (default: ₹2/day for first 7 days, ₹5/day thereafter).
- **Bulk Data Ingestion:** Import student rosters from `.csv` and `.xlsx` with column validation, duplicate detection, and sample templates.
- **Reporting Engine:** 15 distinct report types with date and department filtering, downloadable as styled Excel spreadsheets (via `openpyxl`) and landscape PDF documents (via `reportlab`).

---

## 2. Default Demo Accounts

| Portal | Username / Roll No | Password | Role | Permissions |
| :--- | :--- | :--- | :--- | :--- |
| **Librarian Admin** | `admin` | `admin123` | `librarian` | Full system control, catalogue, circulation desk, members, fines, reports, settings |
| **Student Member** | `student` *(or `ROLL-CS-001`)* | `student123` | `member` | Personal dashboard, borrow history, renewals, book reservations, fine records, digital library |

---

## 3. Windows 11 & VS Code Quick Start Guide

### Step 1: Open Project in VS Code
Open your terminal in VS Code (`Ctrl + ~`) and navigate to the project directory:
```powershell
cd C:\Users\shaanii\.gemini\antigravity\scratch\PDUAM_Central_Library\pduam_central_library
```

### Step 2: Create and Activate Virtual Environment (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If running scripts is restricted on your system, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first).*

### Step 3: Install Required Dependencies
```powershell
pip install -r requirements.txt
```

### Step 4: Environment Variables (Optional)
A `.env.example` file is provided. Create a `.env` file if you wish to override default configuration:
```powershell
Copy-Item .env.example .env
```

### Step 5: Start the Flask Application
Run the main application script:
```powershell
python app.py
```
The console will display:
```
PDUAM Central Library database initialized successfully at: ...\instance\library.db
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 6: Access the Application
Open your web browser and navigate to:
- **OPAC Public Catalogue:** [http://127.0.0.1:5000](http://127.0.0.1:5000) or [http://127.0.0.1:5000/opac](http://127.0.0.1:5000/opac)
- **Portal Selection:** [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
- **Librarian Login:** [http://127.0.0.1:5000/auth/librarian/login](http://127.0.0.1:5000/auth/librarian/login)
- **Student Member Login:** [http://127.0.0.1:5000/auth/member/login](http://127.0.0.1:5000/auth/member/login)
- **Member Registration:** [http://127.0.0.1:5000/auth/register](http://127.0.0.1:5000/auth/register)
- **Digital Library:** [http://127.0.0.1:5000/digital](http://127.0.0.1:5000/digital)

---

## 4. Running the Automated Test Suite

To execute the unit and integration tests covering business rules, authentication, circulation, bulk import, and reports:
```powershell
python -m unittest discover -s tests -p "test_*.py"
```
Or run the route verification script:
```powershell
python verify_routes.py
```

---

## 5. System Features & Modules

### A. OPAC (Online Public Access Catalogue)
- Accessible without login to general students and public visitors.
- Real-time search across Titles, Authors, ISBN, Subjects, and Descriptions.
- Multi-criteria filtering by Academic Department, Category, and Availability Status.
- Book detail page with individual physical copies, condition, shelf location, and direct reservation button.

### B. Circulation Desk
- **Book Issue:** Validates member account status, enforces 3-book active quota limit, and links unique accession copies.
- **Book Return:** Automatically computes late return penalties using the configurable fine rates and restores copy availability.
- **Renewals:** Students can request loan renewals from their dashboard; librarians can approve or reject them based on reservation waitlists.
- **Reservations:** Priority queue management when titles are out of stock.

### C. Fine Management & Official Receipts
- Fine calculation: ₹2 per day for the first 7 days, ₹5 per day thereafter (e.g., 8 days overdue = ₹19).
- Settlement recording with payment mode reference (`CASH`, `UPI`, `BANK`).
- Institutional waiver workflow with required administrative justification.
- Official printable payment receipt with institutional header, college logo, and librarian stamp line.

### D. Member Administration & Bulk Import
- Add, edit, activate, or deactivate student membership accounts.
- Comprehensive member profiles showing active loans, return history, fines, and reservations.
- Bulk student roster import supporting `.csv` and `.xlsx` formats with pre-built downloadable sample templates.

### E. Digital Library & Theses Repository
- Academic archive supporting Doctor of Philosophy/Master theses, dissertations, project reports, and previous 5 years examination question papers.
- Role-gated downloads (Public vs Enrolled Members vs Internal Staff).
- Secure file storage and real-time download counter tracking.

### F. Reports & Institutional Auditing
- 15 comprehensive report registers including Accession Register, Overdue Register, Fine Revenue, and Circulation Statistics.
- Instant export to:
  - **CSV:** Comma-separated value stream for spreadsheet software.
  - **Excel (.xlsx):** Formatted openpyxl workbook with institutional title banner and column auto-sizing.
  - **PDF:** Formatted ReportLab document in landscape A4 with college title and styled data tables.
  - **Print View:** Dedicated print stylesheet removing navbars and sidebars.

---

## 6. Database Migration to MySQL (Future Deployment)

The system currently uses an SQLite database (`instance/library.db`) with full referential integrity and foreign key support (`PRAGMA foreign_keys = ON`).

To migrate to MySQL in a production environment:
1. Install `mysql-connector-python` or `PyMySQL`:
   ```powershell
   pip install pymysql cryptography
   ```
2. The database schema in `app/database.py` uses standard ANSI SQL data types (`INTEGER`, `TEXT`, `REAL`, `TIMESTAMP`) that map directly to MySQL (`INT AUTO_INCREMENT`, `VARCHAR`, `TEXT`, `DECIMAL(10,2)`, `DATETIME`).
3. Set the `DATABASE_PATH` or configure SQLAlchemy URI in `config.py`:
   ```python
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "mysql+pymysql://user:password@localhost/pduam_library")
   ```

---

## 7. Institutional Credits

**Pandit Deendayal Upadhyaya Adarsha Mahavidyalaya (PDUAM)**  
Amjonga, Goalpara, Assam - 783124  
*Central Library Management Platform v2.0*
