# 🎊 START HERE - Deployment Instructions

Your wedding planner is **100% ready to deploy**. Follow these 3 steps to go live.

---

## ⚡ 3-Step Deployment (25 minutes total)

### Step 1️⃣: Push to GitHub (2 minutes)

**1. Create GitHub Repository**
- Go to: https://github.com/new
- Repository name: `wedding-planner`
- Make it Public
- Click "Create repository"
- Copy your repository URL (looks like: `https://github.com/YOUR_USERNAME/wedding-planner.git`)

**2. Push Your Code**

Open Command Prompt/PowerShell and run:

```bash
cd "E:\Pravin\Claude New\Wedding Planner"
git remote add origin https://github.com/YOUR_USERNAME/wedding-planner.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

✅ Done! Your code is now on GitHub.

---

### Step 2️⃣: Deploy to Vercel (5 minutes)

**1. Create Vercel Account**
- Go to: https://vercel.com/signup
- Sign up with GitHub (easiest)

**2. Import & Deploy**
- Go to: https://vercel.com/new
- Click "Import Git Repository"
- Paste: `https://github.com/YOUR_USERNAME/wedding-planner.git`
- Click "Continue"
- Leave settings as default (Other framework, . root)
- Click "Deploy"

⏳ Wait 1-2 minutes while Vercel deploys...

✅ You'll get a live URL like: `https://wedding-planner-xxxxx.vercel.app`

---

### Step 3️⃣: Configure Notion (18 minutes)

**1. Create Notion Integration**
- Go to: https://www.notion.com/my-integrations
- Click "+ New integration"
- Name: `Wedding Planner`
- Click "Submit"
- Go to "Secrets" tab
- Copy the "Internal Integration Token" (starts with `noti_`)

**2. Create 10 Notion Databases**

Create these databases in your Notion workspace:
1. **Wedding Planning Hub** - Fields: Wedding Name (title), City, Start Date, End Date, Status (select), Bride Family, Groom Family, Notes
2. **Guest List** - Fields: Guest Name (title), Phone, Email, Relationship, Side (select), Dietary Restrictions, Accessibility Needs, RSVP Status (select), Plus Ones, Notes
3. **Sub-Events** - Fields: Event Name (title), Event Type (select), Date, Start Time, Location, Hosting Scope (select), Host Side (select), Expected Guests, Notes
4. **Vendors** - Fields: Vendor Name (title), Category (select), Contact Person, Phone, Email, City, Estimated Cost (currency), Status (select), Notes
5. **Bookings & Payments** - Fields: Booking ID (title), Vendor, Event, Booking Date, Confirmed Amount, Advance Paid, Balance Due, Payment Status (select), Booking Status (select), Notes
6. **Properties & Accommodation** - Fields: Property Name (title), Address, City, Check-in Date, Check-out Date, Total Capacity, Rooms Available, Type (select), Cost Per Night (currency), Notes
7. **Tasks & Requirements** - Fields: Task (title), Category (select), Due Date, Assigned To, Priority (select), Status (select), Notes
8. **Entertainment & Performances** - Fields: Performance (title), Type (select), Duration (minutes), Performers, Scheduled Event, Costume Notes, Rehearsal Date, Status (select), Notes
9. **Gifts Received** - Fields: Gift ID (title), Gift Type (select), Amount/Description, From (Donor), Date Received, Side (select), Acknowledged (checkbox), Notes
10. **Families** - Fields: Family Name (title), Owner, Home City, Created At, Notes

**3. Get Database IDs**

For each database:
1. Open it in Notion
2. Copy the URL from browser address bar
3. Find the 32-character ID between `/` and `?`:
   ```
   https://www.notion.so/workspace/[DATABASE_ID_HERE]?v=...
   ```

**4. Add Environment Variables to Vercel**

1. Go to Vercel Dashboard: https://vercel.com/dashboard
2. Click your `wedding-planner` project
3. Click "Settings" → "Environment Variables"
4. Add these 11 variables (paste your IDs):

| Key | Value |
|---|---|
| `NOTION_API_KEY` | `noti_your_token_here` |
| `DB_WEDDING_ID` | (paste your ID) |
| `DB_GUESTS_ID` | (paste your ID) |
| `DB_SUB_EVENTS_ID` | (paste your ID) |
| `DB_VENDORS_ID` | (paste your ID) |
| `DB_BOOKINGS_ID` | (paste your ID) |
| `DB_PROPERTIES_ID` | (paste your ID) |
| `DB_TASKS_ID` | (paste your ID) |
| `DB_ENTERTAINMENT_ID` | (paste your ID) |
| `DB_GIFTS_ID` | (paste your ID) |
| `DB_FAMILIES_ID` | (paste your ID) |

**5. Share Databases with Integration**

For each Notion database:
1. Click "Share" button
2. Add members → Search "Wedding Planner"
3. Give it "Edit" access
4. Click "Invite"

**6. Redeploy Vercel**

1. In Vercel Dashboard, click "Deployments"
2. Find your latest deployment
3. Click the "..." menu
4. Click "Promote to Production"

✅ Done! Your app is live with Notion sync!

---

## ✨ Test Your App (5 minutes)

### Test 1: Landing Page
```
Visit: https://your-url.vercel.app
Should see: Wedding planner landing page
```

### Test 2: Web App
```
Visit: https://your-url.vercel.app/app.html
Should see: Dashboard with navigation sidebar
```

### Test 3: Create Data
1. Click "+ New Wedding"
2. Fill in: Wedding Name, City, Dates, Status
3. Click "Create"
4. Click "+ Add Family" and add a family
5. Click "+ New Event" and add an event
6. Click "+ Add Guest" and add a guest

### Test 4: Notion Sync
1. Create a guest in the app
2. Click "☁️ Sync to Notion" button
3. See green notification: "Synced X guests to Notion"
4. Check your Notion workspace
5. New guest should appear in Guest List database

---

## 📱 Share with Family

Once live, share your URL:
```
https://your-wedding-planner-xxxxx.vercel.app
```

Family can:
- View the landing page
- Open the app
- Create events and guests
- See data sync to Notion in real-time

---

## 🆘 Troubleshooting

### "Git command not found"
- Install Git: https://git-scm.com/download/win
- Restart Command Prompt
- Try again

### "Repository already exists"
- You might have pushed already
- Check GitHub.com - look for `wedding-planner` repo
- If it exists, deployment is on track

### "Vercel deployment failed"
- Check Vercel Dashboard → Deployments
- Click on failed deployment → View Logs
- Common issues:
  - Missing `requirements.txt` ✅ (we have it)
  - Invalid Python syntax ✅ (we tested it)
  - Missing environment variables (you'll add these)

### "Sync to Notion fails"
- Check environment variables are added to Vercel
- Verify Notion databases are shared with integration (Edit access)
- Check API key starts with `noti_`
- Verify database IDs are correct format (32 chars, alphanumeric)

---

## 📖 Full Guides (If You Need More Details)

- **DEPLOYMENT_STATUS.md** - Current progress & next steps
- **QUICK_START.md** - Alternative 5-minute guide
- **VERCEL_DEPLOYMENT.md** - Detailed Vercel setup (30 min read)
- **NOTION_SETUP.md** - Detailed Notion configuration
- **README.md** - Complete project documentation
- **DEPLOYMENT_CHECKLIST.md** - Full pre-deploy checklist

---

## ✅ Quick Reference

| What | Where |
|------|-------|
| Create GitHub repo | https://github.com/new |
| Deploy to Vercel | https://vercel.com/new |
| Notion integration | https://www.notion.com/my-integrations |
| Vercel dashboard | https://vercel.com/dashboard |
| Your GitHub repos | https://github.com/YOUR_USERNAME |

---

## 🎯 Summary

**Before:** Wedding planner files on your computer  
**After 25 minutes:** Live app with Notion sync at `https://your-domain.vercel.app`

**All the hard work is done.** You just need to:
1. Push to GitHub (2 min)
2. Deploy to Vercel (5 min)
3. Configure Notion (18 min)

That's it! 🚀

---

**Ready?** Start with **Step 1** above 👆

Good luck! 💍✨
