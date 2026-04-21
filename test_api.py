#!/usr/bin/env python3
"""
API Test Script - Verify Notion Integration
Usage: python test_api.py [url]
Example: python test_api.py http://localhost:5000
         python test_api.py https://wedding-planner-xxxxx.vercel.app
"""

import json
import sys
import requests
from datetime import datetime

def test_api(base_url):
    """Test all API endpoints"""

    print(f"\n{'='*60}")
    print(f"🧪 Wedding Planner API Test Suite")
    print(f"{'='*60}")
    print(f"Testing: {base_url}\n")

    # Test 1: Health Check
    print("1️⃣  Health Check")
    print("-" * 40)
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'healthy':
                print("✅ API is healthy")
                print(f"   Notion: {result.get('notion')}")
            else:
                print("⚠️  API returned error:")
                print(f"   {result}")
        else:
            print(f"❌ API returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

    print()

    # Test 2: Sync Guests
    print("2️⃣  Sync Guests to Notion")
    print("-" * 40)
    test_guests = [
        {
            "name": "Test Guest 1",
            "phone": "555-0001",
            "email": "guest1@example.com",
            "relationship": "Friend",
            "side": "Bride",
            "dietary": "Vegetarian",
            "accessibility": "None",
            "rsvp_status": "Pending",
            "notes": "Test guest for API validation"
        }
    ]

    try:
        response = requests.post(
            f"{base_url}/api/sync_guests",
            json={"guests": test_guests},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'success':
                print(f"✅ Synced {result.get('synced')} guests")
            else:
                print(f"⚠️  Response: {result}")
        else:
            print(f"❌ Status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

    print()

    # Test 3: Sync Events
    print("3️⃣  Sync Events to Notion")
    print("-" * 40)
    test_events = [
        {
            "event_name": "Test Ceremony",
            "event_type": "Ceremony",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "startTime": "10:00 AM",
            "location": "Test Venue",
            "hosting_scope": "Full Event",
            "host_side": "Bride",
            "expected_guests": 200,
            "notes": "Test event for API validation"
        }
    ]

    try:
        response = requests.post(
            f"{base_url}/api/sync_events",
            json={"events": test_events},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'success':
                print(f"✅ Synced {result.get('synced')} events")
            else:
                print(f"⚠️  Response: {result}")
        else:
            print(f"❌ Status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

    print()

    # Test 4: Sync Vendors
    print("4️⃣  Sync Vendors to Notion")
    print("-" * 40)
    test_vendors = [
        {
            "name": "Test Catering",
            "category": "Catering",
            "contact": "John Caterer",
            "phone": "555-0100",
            "email": "catering@example.com",
            "city": "Test City",
            "estimated_cost": 50000,
            "status": "Inquiry",
            "notes": "Test vendor for API validation"
        }
    ]

    try:
        response = requests.post(
            f"{base_url}/api/sync_vendors",
            json={"vendors": test_vendors},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'success':
                print(f"✅ Synced {result.get('synced')} vendors")
            else:
                print(f"⚠️  Response: {result}")
        else:
            print(f"❌ Status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

    print()

    # Test 5: Fetch Guests (optional - only if function exists)
    print("5️⃣  Fetch Guests from Notion")
    print("-" * 40)
    try:
        response = requests.get(f"{base_url}/api/fetch_guests")
        if response.status_code == 200:
            result = response.json()
            if result.get('status') == 'success':
                guests_count = len(result.get('guests', []))
                print(f"✅ Fetched {guests_count} guests from Notion")
                if guests_count > 0:
                    print(f"   Sample: {result['guests'][0]['name']}")
            else:
                print(f"⚠️  Response: {result}")
        else:
            print(f"⚠️  Endpoint not available (status {response.status_code})")
    except Exception as e:
        print(f"⚠️  Endpoint not available: {str(e)}")

    print()
    print("=" * 60)
    print("✅ Tests Complete!")
    print("=" * 60)
    print("\nNext Steps:")
    print("1. Check your Notion workspace for new entries")
    print("2. Verify all fields populated correctly")
    print("3. If tests failed, check:")
    print("   - NOTION_API_KEY is valid")
    print("   - Database IDs are correct")
    print("   - Notion databases are shared with integration")
    print("   - API endpoint is accessible")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "http://localhost:5000"

    test_api(url)
