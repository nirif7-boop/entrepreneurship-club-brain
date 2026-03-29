"""
sheets_write.py
---------------
Write or append rows to a Google Spreadsheet.

Usage:
    # Append rows from a JSON file
    python tools/sheets_write.py --spreadsheet-id SHEET_ID --sheet-name "Content Calendar" \
        --data .tmp/posts.json --mode append

    # Overwrite a specific range
    python tools/sheets_write.py --spreadsheet-id SHEET_ID --sheet-name "Events" \
        --data .tmp/events.json --mode overwrite --range "A2"

    # Pipe JSON directly
    echo '[{"Title": "Post 1", "Status": "Draft"}]' | \
        python tools/sheets_write.py --spreadsheet-id SHEET_ID --sheet-name "Sheet1"

Output:
    Confirmation message with number of rows written and the updated range.

Requirements:
    pip install google-auth google-auth-oauthlib google-api-python-client python-dotenv
"""

import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
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


def rows_to_values(data: list[dict | list]) -> list[list]:
    """
    Convert a list of dicts or lists to a 2D array for the Sheets API.

    If input is list of dicts: first row = dict keys (headers), subsequent rows = values.
    If input is list of lists: passed through as-is.
    """
    if not data:
        return []

    if isinstance(data[0], dict):
        headers = list(data[0].keys())
        values = [headers]
        for row in data:
            values.append([str(row.get(h, "")) for h in headers])
        return values

    return [[str(cell) for cell in row] for row in data]


def write_sheet(
    spreadsheet_id: str,
    sheet_name: str,
    data: list,
    mode: str = "append",
    start_range: str = "A1",
) -> dict:
    """
    Write data to a Google Sheet.

    mode='append': Appends after the last row with data (ignores start_range).
    mode='overwrite': Writes starting at start_range, clearing existing content in that range.

    Returns the API response with updated range info.
    """
    service = get_sheets_service()
    values = rows_to_values(data)

    if not values:
        return {"updatedRows": 0, "updatedRange": "none"}

    range_notation = f"'{sheet_name}'!{start_range}"

    if mode == "append":
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_notation,
                valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS",
                body={"values": values},
            )
            .execute()
        )
        updates = result.get("updates", {})
        return {
            "updatedRows": updates.get("updatedRows", len(values)),
            "updatedRange": updates.get("updatedRange", range_notation),
        }

    elif mode == "overwrite":
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_notation,
                valueInputOption="USER_ENTERED",
                body={"values": values},
            )
            .execute()
        )
        return {
            "updatedRows": result.get("updatedRows", len(values)),
            "updatedRange": result.get("updatedRange", range_notation),
        }

    else:
        raise ValueError(f"Invalid mode '{mode}'. Use 'append' or 'overwrite'.")


def main():
    parser = argparse.ArgumentParser(description="Write rows to a Google Sheet")
    parser.add_argument("--spreadsheet-id", required=True, help="Google Spreadsheet ID")
    parser.add_argument("--sheet-name", required=True, help="Sheet (tab) name")
    parser.add_argument("--data", default=None,
                        help="Path to JSON file with data. If omitted, reads from stdin.")
    parser.add_argument("--mode", choices=["append", "overwrite"], default="append",
                        help="append: add after last row. overwrite: replace starting at --range.")
    parser.add_argument("--range", default="A1", dest="start_range",
                        help="Starting cell for overwrite mode (default: A1)")
    args = parser.parse_args()

    # Load data
    if args.data:
        data_path = project_root / args.data
        raw = data_path.read_text(encoding="utf-8")
    else:
        raw = sys.stdin.read()

    data = json.loads(raw)

    result = write_sheet(args.spreadsheet_id, args.sheet_name, data, args.mode, args.start_range)

    print(f"✓ Written {result['updatedRows']} rows to range: {result['updatedRange']}")


if __name__ == "__main__":
    main()
