from app import create_app

app = create_app()
client = app.test_client()

routes_to_test = [
    ("/", 200),
    ("/opac", 200),
    ("/digital", 200),
    ("/login", 200),
    ("/auth/login-select", 200),
    ("/auth/librarian/login", 200),
    ("/auth/member/login", 200),
    ("/auth/register", 200),
]

all_passed = True
for url, expected_status in routes_to_test:
    res = client.get(url)
    status_match = (res.status_code == expected_status)
    print(f"Testing route {url:<25} -> Status: {res.status_code} [{'PASS' if status_match else 'FAIL'}]")
    if not status_match:
        all_passed = False

# Test Librarian flow
print("\n--- Testing Librarian Session Flow ---")
res_login = client.post("/auth/librarian/login", data={"username": "admin", "password": "admin123"}, follow_redirects=True)
print(f"Librarian Login -> Status: {res_login.status_code}")

librarian_routes = [
    ("/librarian/dashboard", 200),
    ("/librarian/books", 200),
    ("/librarian/books/add", 200),
    ("/librarian/accessions", 200),
    ("/librarian/loans", 200),
    ("/librarian/renewals", 200),
    ("/librarian/reservations", 200),
    ("/librarian/members", 200),
    ("/librarian/members/add", 200),
    ("/librarian/members/import", 200),
    ("/librarian/fines", 200),
    ("/librarian/digital/upload", 200),
    ("/librarian/reports", 200),
    ("/librarian/settings", 200),
    ("/librarian/audit-logs", 200),
    ("/notifications", 200),
]

for url, expected_status in librarian_routes:
    res = client.get(url)
    status_match = (res.status_code == expected_status)
    print(f"Testing librarian route {url:<30} -> Status: {res.status_code} [{'PASS' if status_match else 'FAIL'}]")
    if not status_match:
        all_passed = False

client.get("/auth/logout")

# Test Student Member flow
print("\n--- Testing Member Session Flow ---")
res_m_login = client.post("/auth/member/login", data={"identifier": "student", "password": "student123"}, follow_redirects=True)
print(f"Member Login -> Status: {res_m_login.status_code}")

member_routes = [
    ("/member/dashboard", 200),
    ("/member/profile", 200),
    ("/member/loans", 200),
    ("/member/fines", 200),
    ("/member/reservations", 200),
    ("/auth/change-password", 200),
    ("/notifications", 200),
]

for url, expected_status in member_routes:
    res = client.get(url)
    status_match = (res.status_code == expected_status)
    print(f"Testing member route {url:<30} -> Status: {res.status_code} [{'PASS' if status_match else 'FAIL'}]")
    if not status_match:
        all_passed = False

if all_passed:
    print("\nSUCCESS: All 31 routes tested and passed with flying colors!")
else:
    print("\nWARNING: Some routes failed.")
