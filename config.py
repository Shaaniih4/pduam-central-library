import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    BASE_DIR = BASE_DIR
    SECRET_KEY = os.environ.get("SECRET_KEY", "pduam-central-library-secure-key-2026-production")
    DATABASE_PATH = os.environ.get(
        "DATABASE_PATH",
        os.path.join(BASE_DIR, "instance", "library.db")
    )
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app", "uploads")
    COVERS_UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, "covers")
    DIGITAL_UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, "digital_resources")
    MAX_CONTENT_LENGTH = 64 * 1024 * 1024  # 64 MB
    ALLOWED_EXTENSIONS = {"pdf", "epub", "doc", "docx", "txt", "xlsx", "csv", "png", "jpg", "jpeg"}
    
    # Institutional Metadata
    INSTITUTION_NAME = "Pandit Deendayal Upadhyaya Adarsha Mahavidyalaya, Amjonga"
    LIBRARY_NAME = "PDUAM Central Library"
    INSTITUTION_LOCATION = "Amjonga, Goalpara, Assam, India - 783124"
    LOGO_FILENAME = "logo.png"

    # Business Rule Defaults
    DEFAULT_LOAN_DAYS = 14
    MAX_ACTIVE_BOOKS_PER_MEMBER = 3
    FINE_FIRST_DAYS = 7
    FINE_RATE_TIER1 = 2   # ₹2/day for first 7 days
    FINE_RATE_TIER2 = 5   # ₹5/day for subsequent days
    MAX_RENEWALS = 2
    RESERVATION_EXPIRY_DAYS = 3
