import json
import os
import requests
from http.server import BaseHTTPRequestHandler

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DB_VENDORS_ID = os.getenv('DB_VENDORS_ID')
NOTION_VERSION = '2022-06-28'
NOTION_BASE_URL = 'https://api.notion.com/v1'

HEADERS = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': NOTION_VERSION,
    'Content-Type': 'application/json'
}

def create_page(database_id, properties):
    """Create a new page in a Notion database."""
    url = f'{NOTION_BASE_URL}/pages'
    data = {
        'parent': {'database_id': database_id},
        'properties': properties
    }
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json()

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode('utf-8'))
        vendors = data.get('vendors', [])

        results = []
        for vendor in vendors:
            properties = {
                'Vendor Name': {
                    'title': [{'text': {'content': vendor.get('name', 'Unknown')}}]
                },
                'Category': {
                    'select': {'name': vendor.get('category', 'Catering')}
                },
                'Contact Person': {
                    'rich_text': [{'text': {'content': vendor.get('contact', '')}}]
                },
                'Phone': {
                    'phone_number': vendor.get('phone', '')
                },
                'Email': {
                    'email': vendor.get('email', '')
                },
                'City': {
                    'rich_text': [{'text': {'content': vendor.get('city', '')}}]
                },
                'Estimated Cost': {
                    'number': float(vendor.get('estimated_cost', 0))
                },
                'Status': {
                    'select': {'name': vendor.get('status', 'Inquiry')}
                },
                'Notes': {
                    'rich_text': [{'text': {'content': vendor.get('notes', '')}}]
                }
            }

            try:
                result = create_page(DB_VENDORS_ID, properties)
                results.append(result)
            except Exception as e:
                results.append({'error': str(e)})

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({
            'status': 'success',
            'synced': len([r for r in results if 'error' not in r]),
            'results': results
        }).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
