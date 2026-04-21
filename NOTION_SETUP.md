# Notion Integration Setup Guide

This guide walks through setting up Notion cloud storage integration with your Wedding Planner application.

## Overview

The Notion integration consists of:
- **Backend API** (`notion_api.py`): Flask server handling Notion API authentication and data syncing
- **Web App** (`app.html`): Frontend with sync buttons for each data section
- **Configuration** (`.env`): Environment file storing your Notion credentials

Data flows one-way (web app → Notion) with these supported entities:
- Guests & RSVPs
- Sub-Events
- Vendors
- Bookings & Payments

---

## Step 1: Create a Notion Integration

### 1.1 Go to Notion Integrations
1. Visit https://www.notion.com/my-integrations
2. Click **"+ New integration"**
3. Name it "Wedding Planner"
4. Select your workspace
5. Click **"Submit"**

### 1.2 Copy Your API Key
1. In the integration page, go to the **"Secrets"** tab
2. Copy the **"Internal Integration Token"** (starts with `noti_`)
3. Save it safely — you'll need it next

---

## Step 2: Get Database IDs from Notion

You need to extract the database IDs from your existing Notion databases. These are long alphanumeric strings in the database URLs.

### Finding Database IDs

For each database you created:
1. Open the database in Notion
2. Copy the URL from your browser:
   ```
   https://www.notion.so/workspace/[DATABASE_ID]?v=...
   ```
3. Extract the `[DATABASE_ID]` part (usually 32 characters)

### Database ID Reference

Find these databases and copy their IDs:

| Database Name | Environment Variable | Notes |
|---|---|---|
| Wedding Planning Hub | `DB_WEDDING_ID` | Top-level wedding info |
| Guest List | `DB_GUESTS_ID` | All guest records |
| Sub-Events | `DB_SUB_EVENTS_ID` | Mehendi, Sangeet, etc. |
| Vendors | `DB_VENDORS_ID` | Vendor contact info |
| Bookings & Payments | `DB_BOOKINGS_ID` | Vendor bookings & payments |
| Properties & Accommodation | `DB_PROPERTIES_ID` | Hotels, homes, facilities |
| Tasks & Requirements | `DB_TASKS_ID` | Ritual checklists |
| Entertainment & Performances | `DB_ENTERTAINMENT_ID` | Dances, speeches, etc. |
| Gifts Received | `DB_GIFTS_ID` | Gift tracking (private) |
| Families | `DB_FAMILIES_ID` | Family unit records |

---

## Step 3: Configure Environment File

### 3.1 Create `.env` File

In your project folder (`Wedding Planner/`), create a file named `.env`:

```bash
# Notion API Configuration
NOTION_API_KEY=noti_[YOUR_API_TOKEN_HERE]

# Database IDs
DB_WEDDING_ID=[paste_wedding_db_id]
DB_GUESTS_ID=[paste_guests_db_id]
DB_SUB_EVENTS_ID=[paste_events_db_id]
DB_VENDORS_ID=[paste_vendors_db_id]
DB_BOOKINGS_ID=[paste_bookings_db_id]
DB_PROPERTIES_ID=[paste_properties_db_id]
DB_TASKS_ID=[paste_tasks_db_id]
DB_ENTERTAINMENT_ID=[paste_entertainment_db_id]
DB_GIFTS_ID=[paste_gifts_db_id]
DB_FAMILIES_ID=[paste_families_db_id]

# Server Configuration
FLASK_ENV=development
FLASK_PORT=5000
```

### 3.2 Share Databases with Integration

For each Notion database:
1. Click **Share** in the database
2. Click **Add members** and search for your "Wedding Planner" integration
3. Give it **"Edit"** access
4. Click **Invite**

This allows the integration to create and modify records.

---

## Step 4: Install Python Dependencies

### 4.1 Install Required Packages

In your project folder, open a terminal and run:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- flask-cors (cross-origin support)
- python-dotenv (environment configuration)
- requests (HTTP client)

---

## Step 5: Run the Backend Server

### 5.1 Start the Notion API Server

In your project folder, run:

```bash
python notion_api.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

**Keep this terminal open** while using the app. The sync buttons will communicate with this server.

---

## Step 6: Use the Web App

### 6.1 Open the App

Open `app.html` in your browser (or use a local server).

### 6.2 Add Data Locally

Create some data in the app:
- Add guests (Guests section)
- Create sub-events (Sub-Events section)
- Add vendors (Vendors & Bookings section)

### 6.3 Sync to Notion

For each section with data:
1. Click the **☁️ Sync to Notion** button
2. A notification will appear:
   - Green: Sync successful
   - Red: Error (check terminal for details)

### 6.4 Verify in Notion

Go to your Notion workspace and check:
- New pages appear in each database
- Data matches what you entered in the app
- All fields populated correctly

---

## Troubleshooting

### Backend Won't Start
**Error**: "ModuleNotFoundError: No module named 'flask'"

**Solution**: Run `pip install -r requirements.txt`

### Sync Button Does Nothing
**Error**: No notification appears

**Solution**: 
1. Check that `notion_api.py` is running in terminal
2. Ensure it shows "Running on http://127.0.0.1:5000"
3. Check browser console for errors (F12 → Console tab)

### "Error: 401 Unauthorized"
**Cause**: Invalid or missing `NOTION_API_KEY`

**Solution**:
1. Verify API key starts with `noti_`
2. Check it's the "Internal Integration Token" (not OAuth)
3. Recreate `.env` file and paste key again

### "Error: 404 Database Not Found"
**Cause**: Incorrect database ID

**Solution**:
1. Double-check database ID format (32 chars, alphanumeric)
2. Verify database is shared with integration (see Step 3.2)
3. Copy ID directly from URL instead of typing

### "CORS Error" in Browser Console
**Cause**: Backend not running

**Solution**: Ensure `python notion_api.py` is running and shows "Running on http://127.0.0.1:5000"

### Data Not Appearing in Notion
**Cause**: Database fields don't match expected schema

**Solution**:
1. Check field names match exactly (case-sensitive)
2. Verify field types (title, select, date, etc.)
3. Check terminal output for error details

---

## Advanced: Fetching Data from Notion

The backend also supports fetching guests from Notion back into the app:

```javascript
// In browser console or JavaScript:
fetch('http://localhost:5000/api/fetch/guests')
    .then(r => r.json())
    .then(data => console.log(data.guests));
```

This feature can be extended to create full bidirectional sync.

---

## Next Steps

### Manual CSV Import (Optional)
If you have guest lists in CSV:
1. Export from Excel/Google Sheets as CSV
2. Parse in Python script
3. Sync to Notion using bulk API

### Automated Sync (Advanced)
Set up scheduled syncing using:
- Celery for task scheduling
- GitHub Actions for serverless sync
- Zapier/Make.com for no-code integration

### Real-Time Collaboration
Add Notion OAuth to allow multiple users to:
1. Log in with their Notion accounts
2. Share data across the team
3. Track changes in real-time

---

## API Endpoints Reference

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/sync/guests` | POST | Sync guests to Notion |
| `/api/sync/events` | POST | Sync sub-events to Notion |
| `/api/sync/vendors` | POST | Sync vendors to Notion |
| `/api/sync/bookings` | POST | Sync bookings to Notion |
| `/api/fetch/guests` | GET | Fetch guests from Notion |
| `/api/health` | GET | Check API health |

---

## Support

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Review terminal output from `notion_api.py` for error details
3. Check browser console (F12 → Console) for frontend errors
4. Verify Notion database is properly shared with integration
