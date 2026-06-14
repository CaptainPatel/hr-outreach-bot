import csv
from datetime import datetime
from pathlib import Path
import pandas as pd

# After your existing imports

def log_result(name, phone, status):

    with open(
        "data/send_log.csv",
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            phone,
            status,
            datetime.now()
        ])

def is_already_sent(phone):
    
    # PART A: Check if file exists
    log_path = Path("data/send_log.csv")
    
    if not log_path.exists():
        # File doesn't exist → no contacts sent yet → return False
        return False
    
    # PART B: Read the CSV file
    try:
        df = pd.read_csv(log_path)
    except:
        # File exists but is empty or corrupted → assume not sent
        return False
    
    # PART C: Check if phone is in the phone column
    # Convert phone to string for comparison
    phone_str = str(phone)
    
    # Check if this phone number exists in the dataframe
    is_in_log = phone_str in df["phone"].astype(str).values
    
    # PART D: Return the result
    return is_in_log

