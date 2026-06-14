import re
from pathlib import Path
import csv
import argparse


def read_contacts(filepath):

    with open(filepath, encoding="utf-8") as file:

        lines = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return lines


def parse_contacts(lines):

    contacts = []

    current_name = ""

    for line in lines:

        digits = re.sub(r"\D", "", line)

        if len(digits) >= 10:

            contact = {
                "name": current_name,
                "phone": digits
            }

            contacts.append(contact)

        else:
            current_name = line

    return contacts

def save_contacts_to_csv(contacts, filepath):

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["name", "phone"]
        )

        writer.writeheader()

        writer.writerows(contacts)

def main():
    
    parser = argparse.ArgumentParser(
        description="Convert messy contact text to CSV"
    )
    parser.add_argument(
        "--input",
        default="data/contacts.txt",
        help="Input contacts.txt file"
    )
    parser.add_argument(
        "--output",
        default="data/contacts.csv",
        help="Output CSV file"
    )
    
    args = parser.parse_args()
    
    contacts_file = Path(args.input)
    lines = read_contacts(contacts_file)
    contacts = parse_contacts(lines)
    csv_file = Path(args.output)
    save_contacts_to_csv(contacts, csv_file)
    
    print(f"✅ Parsed {len(contacts)} contacts from {args.input}")
    print(f"✅ Saved to {args.output}")

if __name__ == "__main__":
    main()