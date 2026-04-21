import json
import os
import requests
from http.server import BaseHTTPRequestHandler

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DB_GUESTS_ID = os.getenv('DB_GUESTS_ID')
NOTION_VERSION = '2022-06-28'
NOTION_BASE_URL = 'https://api.notion.com/v1'

HEADERS = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': NOTION_VERSION,
    'Content-Type': 'application/json'
}

def query_database(database_id):
    """Query pages from a Notion database."""
    url = f'{NOTION_BASE_URL}/databases/{database_id}/query'
    response = requests.post(url, json={}, headers=HEADERS)
    return response.json()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            response = query_database(DB_GUESTS_ID)
            guests = []

            for page in response.get('results', []):
                props = page['properties']
                guest = {
                    'id': page['id'],
                    'name': props['Guest Name']['title'][0]['plain_text'] if props['Guest Name']['title'] else '',
                    'phone': props['Phone'].get('phone_number', '') if 'phone_number' in props['Phone'] else '',
                    'email': props['Email'].get('email', '') if 'email' in props['Email'] else '',
                    'relationship': props['Relationship']['rich_text'][0]['plain_text'] if props['Relationship']['rich_text'] else '',
                    'side': props['Side']['select']['name'] if props['Side']['select'] else '',
                    'dietary': props['Dietary Restrictions']['rich_text'][0]['plain_text'] if props['Dietary Restrictions']['rich_text'] else '',
                    'accessibility': props['Accessibility Needs']['rich_text'][0]['plain_text'] if props['Accessibility Needs']['rich_text'] else '',
                    'rsvp_status': props['RSVP Status']['select']['name'] if props['RSVP Status']['select'] else '',
                }
                guests.append(guest)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'success',
                'guests': guests
            }).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'error',
                'message': str(e)
            }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
