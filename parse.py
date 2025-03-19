import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="SMS Sender CLI")
    parser.add_argument("--fr", required=True, help="Sender's phone number")
    parser.add_argument("--t", required=True, help="Recipient's phone number")
    parser.add_argument("--text", required=True, help="SMS text")
    return parser.parse_args()