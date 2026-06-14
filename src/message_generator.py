from dotenv import load_dotenv
import os

load_dotenv()

def load_template():
    template_path = os.getenv('MESSAGE_TEMPLATE', 'templates/message.txt')
    with open(template_path, encoding="utf-8") as file:
        return file.read()

def generate_message(contact_name):
    """Generate message with env variables"""
    template = load_template()
    sender_name = os.getenv('SENDER_NAME', 'Friend')
    use_contact_name = os.getenv('USE_CONTACT_NAME', 'True') == 'True'
    
    # Decide what name to use
    if use_contact_name and contact_name:
        name = contact_name
    else:
        name = "Sir/Ma'am"
    
    return template.format(name=name, SENDER_NAME=sender_name)