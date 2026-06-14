import pandas as pd
import random
import time
from pathlib import Path
from logger import log_result, is_already_sent
from sender import create_driver, send_message, send_resume
from message_generator import load_template
from dotenv import load_dotenv
import os
from message_generator import generate_message

driver = create_driver()
df = pd.read_csv("data/contacts.csv")


load_dotenv()  # Load .env file

# Then use:
min_delay = int(os.getenv('MIN_DELAY', 20))
max_delay = int(os.getenv('MAX_DELAY', 40))
resume_path = os.getenv('RESUME_PATH', './resume.pdf')


# Load message template once
message = load_template()

print(f"\n{'='*60}")
print(f"Starting HR Outreach Bot - {len(df)} contacts")
print(f"{'='*60}\n")

success_count = 0
failed_count = 0

try:
    for idx, contact in enumerate(df.itertuples(index=False), 1):
        name = contact.name
        phone = str(contact.phone)

        # Generate message with contact's name
        message = generate_message(name)
        
        print(f"[{idx}/{len(df)}] {name} | {phone}")
        
        # Check if already sent
        if is_already_sent(phone):
            print(f"  ⏭️  Skipped (already sent)\n")
            continue
        
        try:
            # Send message and resume
            print(f"  📤 Sending...")
            send_message(driver, phone, message)
            send_resume(driver, resume_path)
            log_result(name, phone, "SUCCESS")
            print(f"  ✅ Success!\n")
            success_count += 1
            
            # Random delay between contacts
            if idx < len(df):
                delay = random.randint(20, 40)
                print(f"  ⏳ Waiting {delay}s...\n")
                time.sleep(delay)
        
        except Exception as e:
            error_msg = str(e)[:50]
            print(f"  ❌ Failed: {error_msg}\n")
            log_result(name, phone, f"FAILED: {error_msg}")
            failed_count += 1

except KeyboardInterrupt:
    print("\n\n⚠️  Bot interrupted by user")

finally:
    print(f"\n{'='*60}")
    print(f"✅ Success: {success_count} | ❌ Failed: {failed_count}")
    print(f"{'='*60}\n")
    driver.quit()