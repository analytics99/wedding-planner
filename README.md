# 💍 Family Event Coordination System - Wedding Planner

A comprehensive web-based wedding planning system with cloud synchronization to Notion. Manage families, events, vendors, guests, accommodations, entertainment, and gifts across multiple family sides.

## ✨ Features

### Core Functionality
- 📊 **Dashboard**: Overview of all wedding data and metrics
- 🎊 **Wedding Management**: Create and manage multiple weddings
- 👥 **Family Management**: Organize family units and members
- 🎭 **Sub-Events**: Mehendi, Sangeet, Ceremony, Reception, etc.
- 👨‍💼 **Vendors & Bookings**: Track vendor contacts and bookings with payment status
- 👫 **Guest Management**: Invitations, RSVPs, dietary restrictions, accessibility needs
- 🏨 **Accommodation**: Property and room assignment tracking
- 📋 **Tasks & Requirements**: Ritual checklists and task management
- 🎵 **Entertainment**: Performance tracking, costumes, rehearsal schedules
- 🎁 **Gift Tracking**: Record and acknowledge gifts received

### Technical Features
- 💾 **Local Storage**: Data persists across browser sessions
- ☁️ **Notion Sync**: One-click sync of data to Notion databases
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🎨 **Beautiful UI**: Professional, celebration-themed aesthetics
- 🔒 **Privacy-First**: Multi-sided privacy controls (Bride/Groom/Solo)
- ⚡ **Fast Performance**: Optimized for speed and reliability

---

## 📖 Quick Start

### Option 1: Local Development

1. **Open the app locally**
   ```bash
   # Option A: Direct browser
   open index.html

   # Option B: Python server (recommended)
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

2. **Create your wedding data**
   - Navigate to the app
   - Create wedding, families, guests, events, etc.
   - Data auto-saves to localStorage

3. **Optional: Sync to Notion**
   - Set up Notion API (see NOTION_SETUP.md)
   - Run backend: `python notion_api.py`
   - Click "☁️ Sync to Notion" buttons

### Option 2: Deploy to Vercel (Recommended)

For a live, cloud-hosted app:

1. Push code to GitHub
2. Deploy via Vercel Dashboard
3. Configure Notion environment variables
4. Live app is immediately available

See **[VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)** for complete instructions.

---

## 📁 Project Structure

```
wedding-planner/
├── index.html                 # Landing page with documentation
├── app.html                   # Main web application
├── api/                       # Vercel serverless functions
│   ├── sync_guests.py        # Sync guests to Notion
│   ├── sync_events.py        # Sync events to Notion
│   ├── sync_vendors.py       # Sync vendors to Notion
│   ├── sync_bookings.py      # Sync bookings to Notion
│   ├── fetch_guests.py       # Fetch guests from Notion
│   └── health.py             # API health check
├── notion_api.py             # Local Flask backend (development)
├── create_schema.py          # Excel schema generation
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
├── .env.example             # Environment variables template
├── .gitignore               # Git exclusions
├── README.md                # This file
├── NOTION_SETUP.md          # Notion integration guide
└── VERCEL_DEPLOYMENT.md     # Vercel deployment guide
```

---

## 🚀 Deployment

### Deploy to Vercel (Production)

The easiest way to deploy:

```bash
# 1. Initialize Git
git init
git add .
git commit -m "Initial commit"

# 2. Push to GitHub
git remote add origin https://github.com/USERNAME/wedding-planner.git
git push -u origin main

# 3. Deploy on Vercel
# Go to vercel.com/new and import your GitHub repository
```

**Full Guide**: See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)

### Run Locally (Development)

```bash
# Install dependencies
pip install -r requirements.txt

# Start local backend
python notion_api.py

# Open app
open app.html
# or with Python server:
python -m http.server 8000
```

---

## 🔧 Configuration

### Environment Variables

Create `.env` file (copy from `.env.example`):

```bash
# Notion API Key from https://www.notion.com/my-integrations
NOTION_API_KEY=noti_your_api_key_here

# Notion Database IDs
DB_WEDDING_ID=your_wedding_db_id
DB_GUESTS_ID=your_guests_db_id
DB_SUB_EVENTS_ID=your_events_db_id
DB_VENDORS_ID=your_vendors_db_id
DB_BOOKINGS_ID=your_bookings_db_id
DB_PROPERTIES_ID=your_properties_db_id
DB_TASKS_ID=your_tasks_db_id
DB_ENTERTAINMENT_ID=your_entertainment_db_id
DB_GIFTS_ID=your_gifts_db_id
DB_FAMILIES_ID=your_families_db_id
```

See **[NOTION_SETUP.md](./NOTION_SETUP.md)** for detailed configuration.

---

## 📊 Database Schema

### Core Entities (23 Tables)

**People & Families**
- Users (phone-first identity)
- Families (family units as sides)
- FamilyMembers (individual people)
- Relationships (family connections)

**Weddings & Events**
- Wedding (top-level container)
- Sides (bride/groom/solo family links)
- SubEvents (Mehendi, Sangeet, Ceremony, etc.)
- SideMembership (user access control)

**Vendors & Finance**
- VendorCategories (catering, photography, etc.)
- Vendors (vendor contact records)
- Bookings (vendor × event assignments)

**Guests & Accommodation**
- Guests (invited people)
- GuestInvitations (guest × event RSVPs)
- Properties (hotels, homes, facilities)
- Rooms (individual room tracking)
- RoomAssignments (guest × room assignments)

**Entertainment & Tasks**
- RequirementTemplates (ritual checklists)
- SubEventRequirements (task instances)
- Performances (dances, speeches, etc.)
- Performers (member/guest performance assignments)

**Gifts**
- Gifts (shagun, cash, jewelry tracking)

See **Family_Event_Coordination_Template_v0.2.xlsx** for full ERD.

---

## 🎨 Design & Styling

### Color Palette
- **Cream** `#faf8f3` - Primary background
- **Coral** `#d97757` - Accent highlights
- **Sage** `#7a8f7e` - Secondary text
- **Gold** `#c9a877` - Tertiary accents
- **Ivory** `#f5f2ed` - Secondary background

### Typography
- **Headings**: Playfair Display (serif)
- **Body**: Poppins (sans-serif)
- **Responsive**: Adjusts for all screen sizes

### Responsive Breakpoints
- **Desktop**: 1280px+
- **Tablet**: 768px - 1024px
- **Mobile**: < 768px

---

## 🔌 Notion Integration

### Sync Data to Notion

One-click sync from app to Notion:

```javascript
// Sync guests to Notion
syncGuestsToNotion()

// Sync events to Notion
syncEventsToNotion()

// Sync vendors to Notion
syncVendorsToNotion()
```

### Fetch Data from Notion

```javascript
// Fetch guests from Notion
fetch('/api/fetch_guests').then(r => r.json())
```

### Create Databases

The system creates 10 Notion databases:
1. Wedding Planning Hub
2. Guest List
3. Sub-Events
4. Vendors
5. Bookings & Payments
6. Properties & Accommodation
7. Tasks & Requirements
8. Entertainment & Performances
9. Gifts Received
10. Families

See **[NOTION_SETUP.md](./NOTION_SETUP.md)** for setup.

---

## 📱 Browser Support

✅ Chrome/Brave (latest)  
✅ Firefox (latest)  
✅ Safari (latest)  
✅ Edge (latest)  
⚠️ IE 11 (not supported)

---

## 🔐 Privacy & Security

### Data Storage
- **Local**: localStorage (encrypted by browser)
- **Cloud**: Notion (encrypted at rest and in transit)
- **API**: HTTPS only, no logging of sensitive data

### Multi-Sided Access
- Each wedding has bride/groom/solo sides
- Users can belong to multiple sides
- Gifts are private (own side only)
- Permissions enforced server-side

### Environment Variables
- Never commit `.env` file
- Sensitive keys stored in Vercel dashboard
- API tokens not exposed to frontend

---

## 🛠️ Development

### Local Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/wedding-planner.git
cd wedding-planner

# Install dependencies
pip install -r requirements.txt

# Start local server
python -m http.server 8000

# In another terminal, start backend
python notion_api.py

# Visit http://localhost:8000
```

### Making Changes

1. Edit files locally
2. Test in browser (reload to see changes)
3. Commit and push to GitHub
4. Vercel auto-deploys

### Testing Notion Sync

```bash
# Check API health
curl http://localhost:5000/api/health

# Test guest sync
curl -X POST http://localhost:5000/api/sync/guests \
  -H "Content-Type: application/json" \
  -d '{"guests": [{"name": "John", "phone": "555-1234"}]}'
```

---

## 📖 Documentation

- **[NOTION_SETUP.md](./NOTION_SETUP.md)** - Notion integration & configuration
- **[VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)** - Deploy to Vercel
- **[index.html](./index.html)** - Landing page with system documentation
- **[app.html](./app.html)** - Main application code

---

## 🐛 Troubleshooting

### App Data Disappeared
- Check browser localStorage isn't cleared
- Verify localStorage is enabled
- Try creating data again (should persist)

### Sync Buttons Don't Work
- Ensure Notion API is running: `python notion_api.py`
- Check browser console for errors (F12)
- Verify `.env` file has correct credentials

### Notion Connection Failed
- Verify API key starts with `noti_`
- Check database IDs are correct format (32 chars)
- Ensure databases are shared with integration
- Test API: `curl http://localhost:5000/api/health`

### Deployment Issues
- Check Vercel build logs
- Verify environment variables are set
- Confirm all files are committed to GitHub
- Redeploy: Vercel Dashboard → Redeploy button

For more help, see respective documentation files.

---

## 📞 Support

- **Issues**: Create GitHub issue in repository
- **Questions**: Check documentation files
- **Vercel Support**: https://vercel.com/help
- **Notion Support**: https://support.notion.so

---

## 📄 License

Open source project. Feel free to fork, modify, and use for your events.

---

## 🎉 Getting Started

1. **First Time?** Start with [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)
2. **Need Notion?** Follow [NOTION_SETUP.md](./NOTION_SETUP.md)
3. **Want Local Dev?** Run `python -m http.server 8000`
4. **Ready to Deploy?** Push to GitHub and deploy on Vercel

Your wedding planning system is ready to go! 💍✨
