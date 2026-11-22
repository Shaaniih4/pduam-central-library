# Testing Documentation & Verification Report
## PDUAM Central Library Management System
**Institution:** Pandit Deendayal Upadhyaya Adarsha Mahavidyalaya, Amjonga, Assam

---

## 1. Test Summary

The application has been verified through automated unit tests (`tests/test_lms.py`) and full route regression tests (`verify_routes.py`), achieving 100% pass rates across all modules.

| Test Category | Test Cases Executed | Result |
| :--- | :--- | :--- |
| **Fine Calculation Rules** | 5 boundary tests (0, 1, 7, 8, 9 days) | **PASSED** |
| **Authentication & RBAC** | 4 tests (Librarian, Member, Bad Creds, RBAC Guard) | **PASSED** |
| **Member Registration** | 2 tests (Valid registration, Duplicate Roll No. prevention) | **PASSED** |
| **Catalogue & Accessions** | 2 tests (Add book, Accession copy generation) | **PASSED** |
| **Circulation (Issue & Return)** | 3 tests (Issue, Stock decrement, Return & restoration) | **PASSED** |
| **Bulk Member Import** | 3 tests (Sample templates, CSV parsing, DB insertion) | **PASSED** |
| **Reporting Engine** | 4 tests (Data query, CSV export, Excel XLSX, ReportLab PDF) | **PASSED** |
| **Route Coverage** | 31 distinct endpoints | **ALL 31 PASSED (200 OK)** |

---

## 2. Test Case Details & Execution Log

### Test 1: Two-Tier Overdue Fine Business Rule
- **Requirement:** ₹2/day for first 7 days, ₹5/day for subsequent days.
- **Test Scenarios:**
  - 0 days overdue: Expected ₹0.00 &rarr; Received **₹0.00** [PASS]
  - 1 day overdue: Expected ₹2.00 &rarr; Received **₹2.00** [PASS]
  - 7 days overdue: Expected ₹14.00 &rarr; Received **₹14.00** [PASS]
  - 8 days overdue: Expected (7 &times; 2) + (1 &times; 5) = ₹19.00 &rarr; Received **₹19.00** [PASS]
  - 9 days overdue: Expected (7 &times; 2) + (2 &times; 5) = ₹24.00 &rarr; Received **₹24.00** [PASS]

### Test 2: Authentication & RBAC Guard
- `POST /auth/librarian/login` with `admin` / `admin123`: Authenticated and redirected to `/librarian/dashboard` [PASS].
- `POST /auth/librarian/login` with invalid credentials: Flashed error "Invalid librarian credentials" [PASS].
- Unauthenticated user attempting to access `/librarian/dashboard`: Redirected to login portal [PASS].
- Student member attempting to access `/librarian/dashboard`: Denied with flash "Librarian administrative privileges required" and redirected to `/member/dashboard` [PASS].

### Test 3: Member Registration & Duplicate Prevention
- New student registration with unique Roll Number `ROLL-TEST-001`: Successfully created in database and user login account generated [PASS].
- Second registration attempt with existing Roll Number `ROLL-TEST-001`: Rejected with error "A member with College Roll Number 'ROLL-TEST-001' is already registered." [PASS].

### Test 4: Accession Number Generation
- Adding book with 3 copies in Mathematics department:
  - Total copies set to 3, Available copies set to 3.
  - Exactly 3 records created in `book_copies` table with accession numbers formatted as `PDUAM-2026-MATH-{id}-01`, `02`, `03` [PASS].

### Test 5: Circulation Issue & Return
- Member borrows available book:
  - Active loan recorded in `loans`.
  - Available copies in `books` decremented by 1.
  - Specific physical copy in `book_copies` updated from `available` to `issued` [PASS].
- Member returns book:
  - Return date recorded, overdue fine calculated.
  - Available copies in `books` incremented by 1.
  - Physical copy updated back to `available` [PASS].

### Test 6: Bulk Member Ingestion
- Generation of sample CSV (`generate_sample_csv`) and Excel (`generate_sample_xlsx`): Valid file headers and test rows generated [PASS].
- Uploading CSV with 2 new student records: Parsed, validated, and inserted into `members` table with corresponding student login credentials [PASS].

### Test 7: Report Exports
- Export to CSV: Valid comma-separated stream with headers and records [PASS].
- Export to Excel: Valid `.xlsx` workbook generated via `openpyxl` with styled headers [PASS].
- Export to PDF: Valid landscape A4 PDF generated via `reportlab` with institutional title and table layout [PASS].

---

## 3. How to Run the Test Suite

```powershell
# Run the automated unittest suite
python -m unittest discover -s tests -p "test_*.py"

# Run the 31-endpoint route verification script
python verify_routes.py
```
