import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables
load_dotenv()
cred_path = os.getenv("KEYS")

# Initialize Firebase
if not cred_path:
    raise ValueError("Firebase credentials file path not found")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()