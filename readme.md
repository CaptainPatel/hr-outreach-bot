# HR Outreach Bot 🤖

Automate bulk WhatsApp messaging to HR contacts or leads. Send personalized messages with resume attachments in seconds instead of hours.

## Features

✅ Bulk message sending via WhatsApp Web  
✅ Automatic resume attachment  
✅ Smart duplicate prevention (never spam same contact)  
✅ Error handling & logging  
✅ Random delays for human-like behavior  
✅ Cross-platform (Windows, Mac, Linux)  

## Quick Start

### Prerequisites
- Python 3.8+
- Chrome browser
- Your resume as `resume.pdf`
- Contact list as `data/contacts.csv`

### Installation

```bash
# 1. Clone repo
git clone https://github.com/CaptainPatel/hr-outreach-bot
cd hr-outreach-bot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Setup

1. **Add your contacts:**
   - Copy your contacts to `data/contacts.txt`
   - Run: `python src/parser.py --input your_contacts.txt`

2. **Add your resume:**
   - Place resume as `resume.pdf` in project root

3. **Customize message:**
   - Edit `templates/message.txt` with your message

4. **Run the bot:**
```bash
   python src/main.py
```

   On first run, scan WhatsApp QR code in browser.

## How It Works

1. Reads contacts from `data/contacts.csv`
2. Checks `data/send_log.csv` (skips already sent)
3. Opens WhatsApp Web for each contact
4. Sends personalized message
5. Attaches resume automatically
6. Logs result (success/failure)
7. Waits 20-40 seconds before next contact

## Project Structure

project/

├── src/

│   ├── main.py          # Main bot logic

│   ├── sender.py        # WhatsApp sending

│   ├── logger.py        # Track sent messages

│   ├── parser.py        # Parse contacts (CLI tool)

│   └── message_generator.py  # Load message template

├── data/

│   ├── contacts.csv     # Your contacts (add this)

│   └── send_log.csv     # Auto-generated log

├── templates/

│   └── message.txt      # Your message template

├── requirements.txt     # Dependencies

├── .gitignore          # Ignored files

├── resume.pdf          # Your resume (add this)

└── README.md           # This file


## First Time Setup

1. Prepare your contacts list (names + phone numbers)
2. Run parser to convert to CSV:
```bash
   python src/parser.py --input your_file.txt
```
3. Place resume.pdf in project root
4. Edit message in templates/message.txt
5. Run: `python src/main.py`


### Contact List Format

`data/contacts.txt` should have format:

Name 1
+91 1231433242
Name 2
+91 3424324234

Parser will:
- Extract name from first line
- Extract phone (10+ digits)
- Create CSV with both

Run: `python src/parser.py --input contacts.txt`

## Tracking Progress

Check `data/send_log.csv` to see:
- Which contacts were messaged
- Success/failure status
- Timestamps

## Tips

- Test with 5 contacts first: `python src/main.py`
- Messages are logged - run bot multiple times, it skips sent contacts
- WhatsApp may ask to scan QR code on first run - this is normal
- Keep 20-40 second delays to avoid spam detection

## License

MIT License - Feel free to use and modify

## Support

If contacts aren't on WhatsApp, they're automatically skipped. Check `data/send_log.csv` for details.