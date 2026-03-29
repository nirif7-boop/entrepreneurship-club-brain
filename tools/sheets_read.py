"""
sheets_read.py
--------------
Read rows or a range from a Google Spreadsheet.

Usage:
    python tools/sheets_read.py --spreadsheet-id SHEET_ID --sheet-name "Sheet1"
    python tools/sheets_read.py --spreadsheet-id SHEET_ID --sheet-name "Events" --range "A1:D50"
    python tools/sheets_read.py --spreadsheet-id SHEET_ID --sheet-name "Members" --output .tmp/members.json

Output:
    JSON array of objects (one per row, using the first row as column headers).
    Printed to stdout or saved to a file.

Requirements:
    pip install google-auth google-auth-oauthlib google-api-python-client python-dotenv
"""

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load .env from project root
project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
CREDENTIALS_FILE = project_root / "credentials.json"
TOKEN_FILE = project_root / "token.json"


def get_sheets_service():
    """Authenticate and return a Google Sheets service object."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                print(
                    f"ERROR: credentials.json not found at {CREDENTIALS_FILE}\n"
                    "Download it from Google Cloud Console → APIs & Services → Credentials.",
                    file=sys.stderr,
                )
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")

    return build("sheets", "v4", credentials=creds)


def read_sheet(spreadsheet_id: str, sheet_name: str, cell_range: str = None) -> list[dict]:
    """
    Read data from a Google Sheet.

    Returns a list of dicts where keys are taken from the first row (headers).
    Rows with fewer columns than headers get empty strings for missing values.
    """
    service = get_sheets_service()

    range_notation = f"'{sheet_name}'"
    if cell_range:
        range_notation = f"'{sheet_name}'!{cell_range}"

    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_notation)
        .execute()
    )

    values = result.get("values", [])

    if not values:
        return []

    headers = values[0]
    rows = []
    for row in values[1:]:
        # Pad short rows with empty strings
        padded = row + [""] * (len(headers) - len(row))
        rows.append(dict(zip(headers, padded)))

    return rows


def main():
    parser = argparse.ArgumentParser(description="Read rows from a Google Sheet")
    parser.add_argument("--spreadsheet-id", required=True, help="Google Spreadsheet ID")
    parser.add_argument("--sheet-name", required=True, help="Sheet (tab) name")
    parser.add_argument("--range", default=None, dest="cell_range",
                        help="Optional cell range, e.g. A1:D50")
    parser.add_argument("--output", default=None,
                        help="Save JSON output to file (e.g. .tmp/data.json)")
    args = parser.parse_args()

    rows = read_sheet(args.spreadsheet_id, args.sheet_name, args.cell_range)
    output = json.dumps(rows, ensure_ascii=False, indent=2)

    if args.output:
        out_path = project_root / args.output
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Saved {len(rows)} rows to {out_path}")
    else:
        print(output)


if __name__ == "__main__":
    main()
