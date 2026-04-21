#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_VERSION = '2022-06-28'
NOTION_BASE_URL = 'https://api.notion.com/v1'

# Database IDs (from Notion workspace)
DB_IDS = {
    'wedding': os.getenv('DB_WEDDING_ID'),
    'guests': os.getenv('DB_GUESTS_ID'),
    'sub_events': os.getenv('DB_SUB_EVENTS_ID'),
    'vendors': os.getenv('DB_VENDORS_ID'),
    'bookings': os.getenv('DB_BOOKINGS_ID'),
    'properties': os.getenv('DB_PROPERTIES_ID'),
    'tasks': os.getenv('DB_TASKS_ID'),
    'entertainment': os.getenv('DB_ENTERTAINMENT_ID'),
    'gifts': os.getenv('DB_GIFTS_ID'),
    'families': os.getenv('DB_FAMILIES_ID'),
}

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

def query_database(database_id, filters=None):
    """Query pages from a Notion database."""
    url = f'{NOTION_BASE_URL}/databases/{database_id}/query'
    data = {}
    if filters:
        data['filter'] = filters
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json()

def update_page(page_id, properties):
    """Update an existing Notion page."""
    url = f'{NOTION_BASE_URL}/pages/{page_id}'
    data = {'properties': properties}
    response = requests.patch(url, json=data, headers=HEADERS)
    return response.json()

# Route to sync guest list to Notion
@app.route('/api/sync/guests', methods=['POST'])
def sync_guests():
    """Sync guest data to Notion Guest List database."""
    data = request.json
    guests = data.get('guests', [])

    results = []
    for guest in guests:
        properties = {
            'Guest Name': {
                'title': [{'text': {'content': guest.get('full_name', 'Unknown')}}]
            },
            'Phone': {
                'phone_number': guest.get('phone_number', '')
            },
            'Email': {
                'email': guest.get('email', '')
            },
            'Relationship': {
                'rich_text': [{'text': {'content': guest.get('relationship', '')}}]
            },
            'Side': {
                'select': {'name': guest.get('side', 'Bride')}
            },
            'Dietary Restrictions': {
                'rich_text': [{'text': {'content': guest.get('dietary_restrictions', '')}}]
            },
            'Accessibility Needs': {
                'rich_text': [{'text': {'content': guest.get('accessibility_needs', '')}}]
            },
            'RSVP Status': {
                'select': {'name': guest.get('rsvp_status', 'Pending')}
            },
            'Notes': {
                'rich_text': [{'text': {'content': guest.get('notes', '')}}]
            }
        }

        result = create_page(DB_IDS['guests'], properties)
        results.append(result)

    return jsonify({'status': 'success', 'synced': len(results), 'results': results})

# Route to sync sub-events to Notion
@app.route('/api/sync/events', methods=['POST'])
def sync_events():
    """Sync sub-event data to Notion Sub-Events database."""
    data = request.json
    events = data.get('events', [])

    results = []
    for event in events:
        properties = {
            'Event Name': {
                'title': [{'text': {'content': event.get('event_name', 'Unnamed Event')}}]
            },
            'Event Type': {
                'select': {'name': event.get('event_type', 'Ceremony')}
            },
            'Date': {
                'date': {'start': event.get('event_date', '')}
            },
            'Start Time': {
                'rich_text': [{'text': {'content': event.get('start_time', '')}}]
            },
            'Location': {
                'rich_text': [{'text': {'content': event.get('location', '')}}]
            },
            'Hosting Scope': {
                'select': {'name': event.get('hosting_scope', 'Full Event')}
            },
            'Host Side': {
                'select': {'name': event.get('host_side', 'Bride')}
            },
            'Expected Guests': {
                'number': int(event.get('expected_guests', 0))
            },
            'Notes': {
                'rich_text': [{'text': {'content': event.get('notes', '')}}]
            }
        }

        result = create_page(DB_IDS['sub_events'], properties)
        results.append(result)

    return jsonify({'status': 'success', 'synced': len(results), 'results': results})

# Route to sync vendors to Notion
@app.route('/api/sync/vendors', methods=['POST'])
def sync_vendors():
    """Sync vendor data to Notion Vendors database."""
    data = request.json
    vendors = data.get('vendors', [])

    results = []
    for vendor in vendors:
        properties = {
            'Vendor Name': {
                'title': [{'text': {'content': vendor.get('vendor_name', 'Unknown')}}]
            },
            'Category': {
                'select': {'name': vendor.get('category', 'Catering')}
            },
            'Contact Person': {
                'rich_text': [{'text': {'content': vendor.get('contact_person', '')}}]
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

        result = create_page(DB_IDS['vendors'], properties)
        results.append(result)

    return jsonify({'status': 'success', 'synced': len(results), 'results': results})

# Route to sync bookings to Notion
@app.route('/api/sync/bookings', methods=['POST'])
def sync_bookings():
    """Sync booking data to Notion Bookings & Payments database."""
    data = request.json
    bookings = data.get('bookings', [])

    results = []
    for booking in bookings:
        properties = {
            'Booking ID': {
                'title': [{'text': {'content': booking.get('booking_id', '')}}]
            },
            'Vendor': {
                'rich_text': [{'text': {'content': booking.get('vendor_id', '')}}]
            },
            'Event': {
                'rich_text': [{'text': {'content': booking.get('sub_event_id', '')}}]
            },
            'Booking Date': {
                'date': {'start': booking.get('booking_date', '')}
            },
            'Confirmed Amount': {
                'number': float(booking.get('confirmed_amount', 0))
            },
            'Advance Paid': {
                'number': float(booking.get('advance_paid', 0))
            },
            'Balance Due': {
                'number': float(booking.get('confirmed_amount', 0)) - float(booking.get('advance_paid', 0))
            },
            'Payment Status': {
                'select': {'name': booking.get('payment_status', 'Pending')}
            },
            'Booking Status': {
                'select': {'name': booking.get('booking_status', 'Pending')}
            },
            'Notes': {
                'rich_text': [{'text': {'content': booking.get('notes', '')}}]
            }
        }

        result = create_page(DB_IDS['bookings'], properties)
        results.append(result)

    return jsonify({'status': 'success', 'synced': len(results), 'results': results})

# Route to fetch guests from Notion
@app.route('/api/fetch/guests', methods=['GET'])
def fetch_guests():
    """Fetch all guests from Notion Guest List database."""
    try:
        response = query_database(DB_IDS['guests'])
        guests = []

        for page in response.get('results', []):
            props = page['properties']
            guest = {
                'id': page['id'],
                'full_name': props['Guest Name']['title'][0]['plain_text'] if props['Guest Name']['title'] else '',
                'phone_number': props['Phone']['phone_number'] if 'phone_number' in props['Phone'] else '',
                'email': props['Email']['email'] if 'email' in props['Email'] else '',
                'relationship': props['Relationship']['rich_text'][0]['plain_text'] if props['Relationship']['rich_text'] else '',
                'side': props['Side']['select']['name'] if props['Side']['select'] else '',
                'dietary_restrictions': props['Dietary Restrictions']['rich_text'][0]['plain_text'] if props['Dietary Restrictions']['rich_text'] else '',
                'accessibility_needs': props['Accessibility Needs']['rich_text'][0]['plain_text'] if props['Accessibility Needs']['rich_text'] else '',
                'rsvp_status': props['RSVP Status']['select']['name'] if props['RSVP Status']['select'] else '',
            }
            guests.append(guest)

        return jsonify({'status': 'success', 'guests': guests})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Health check
@app.route('/api/health', methods=['GET'])
def health():
    """Check API health and Notion connectivity."""
    if not NOTION_API_KEY:
        return jsonify({'status': 'error', 'message': 'NOTION_API_KEY not configured'}), 500

    try:
        # Test Notion connection
        response = requests.get(f'{NOTION_BASE_URL}/users/me', headers=HEADERS)
        if response.status_code == 200:
            return jsonify({'status': 'healthy', 'notion': 'connected'})
        else:
            return jsonify({'status': 'error', 'notion': 'disconnected'}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
