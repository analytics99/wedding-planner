# Wedding Planner - Vercel Deployment Guide

Complete guide to deploy your family event coordination system to Vercel with Notion integration.

## Architecture Overview

Your deployment consists of:
- **Frontend**: `index.html`, `app.html` (static files served globally)
- **Backend**: Serverless Python functions in `/api` directory
- **Data Storage**: Notion databases (configured via environment variables)

All components are automatically scaled and deployed to Vercel's global CDN.

---

## Prerequisites

1. **GitHub Account**: [github.com](https://github.com) (free)
2. **Vercel Account**: [vercel.com](https://vercel.com) (free)
3. **Notion API Key**: From https://www.notion.com/my-integrations
4. **Database IDs**: From your Notion workspace (see NOTION_SETUP.md)

---

## Step 1: Prepare Your Project

### 1.1 Initialize Git Repository

In your project folder, open terminal and run:

```bash
git init
git add .
git commit -m "Initial commit: Wedding planner with Notion integration"
```

### 1.2 Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Create repository named `wedding-planner`
3. Do **NOT** initialize with README (we'll push existing code)
4. Copy the commands shown after repository creation

### 1.3 Push Code to GitHub

Run these commands in your project folder:

```bash
git remote add origin https://github.com/YOUR_USERNAME/wedding-planner.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## Step 2: Deploy to Vercel

### 2.1 Import Project to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import Project"**
3. Select **"Import Git Repository"**
4. Paste your GitHub repository URL:
   ```
   https://github.com/YOUR_USERNAME/wedding-planner.git
   ```
5. Click **"Continue"**

### 2.2 Configure Project Settings

**Project Name**: `wedding-planner` (or preferred name)

**Framework Preset**: Select **"Other"** (not Next.js)

**Root Directory**: `.` (dot - project root)

Click **"Continue"**

### 2.3 Add Environment Variables

On the environment variables screen, add all Notion credentials:

| Key | Value |
|---|---|
| `NOTION_API_KEY` | Your Notion API token (noti_...) |
| `DB_WEDDING_ID` | Wedding Planning Hub database ID |
| `DB_GUESTS_ID` | Guest List database ID |
| `DB_SUB_EVENTS_ID` | Sub-Events database ID |
| `DB_VENDORS_ID` | Vendors database ID |
| `DB_BOOKINGS_ID` | Bookings & Payments database ID |
| `DB_PROPERTIES_ID` | Properties & Accommodation database ID |
| `DB_TASKS_ID` | Tasks & Requirements database ID |
| `DB_ENTERTAINMENT_ID` | Entertainment & Performances database ID |
| `DB_GIFTS_ID` | Gifts Received database ID |
| `DB_FAMILIES_ID` | Families database ID |

**How to get Database IDs:**
- Open each Notion database
- Copy URL: `https://www.notion.so/[DATABASE_ID]?v=...`
- Extract the `[DATABASE_ID]` part (32 characters)

See **NOTION_SETUP.md** for detailed instructions on finding these IDs.

### 2.4 Deploy

Click **"Deploy"** button.

Vercel will:
1. Build your Python functions
2. Optimize your static files
3. Deploy to global CDN
4. Provide you a live URL

Wait for deployment to complete (usually 1-2 minutes).

---

## Step 3: Verify Deployment

### 3.1 Check Live Site

After deployment completes:
1. Vercel shows your site URL: `https://wedding-planner-xxxxx.vercel.app`
2. Click the link to visit your deployed app
3. Landing page (`index.html`) should load
4. All styling should match local version

### 3.2 Test App Functionality

1. Click **"App"** in landing page (or navigate to `/app.html`)
2. Create sample wedding, guests, events
3. Click **"☁️ Sync to Notion"** button
4. Should see green notification: "Synced X guests to Notion"
5. Check Notion workspace - new pages should appear in databases

### 3.3 Check API Health

In browser console, run:
```javascript
fetch('/api/health').then(r => r.json()).then(console.log)
```

Should return: `{ status: 'healthy', notion: 'connected' }`

---

## Step 4: Post-Deployment Configuration

### 4.1 Notion Database Sharing

For each database, share it with your "Wedding Planner" integration:

1. Open database in Notion
2. Click **Share** → **Add members**
3. Search for "Wedding Planner" integration
4. Set permission to **Edit**
5. Click **Invite**

Repeat for all 10 databases.

### 4.2 Custom Domain (Optional)

To use custom domain like `wedding.example.com`:

1. In Vercel Dashboard, go to **Settings** → **Domains**
2. Click **Add Domain**
3. Enter your domain
4. Follow DNS configuration steps
5. Wait for verification (5-30 minutes)

### 4.3 Build & Deploy Settings (Optional)

For advanced users in **Settings** → **Git**:
- **Production Branch**: `main`
- **Build Command**: `pip install -r requirements.txt` (auto-configured)
- **Output Directory**: (leave blank)

---

## Troubleshooting

### Deployment Failed

**Error**: "Build failed"

**Solution**:
1. Check **Build & Logs** tab in Vercel Dashboard
2. Common causes:
   - Missing `requirements.txt`
   - Invalid Python syntax in `/api` files
   - Missing environment variables

### Sync Buttons Don't Work

**Error**: "Failed to sync..." notification

**Solution**:
1. Check browser console (F12 → Console)
2. Verify environment variables in Vercel Settings
3. Test API: Visit `/api/health` endpoint
4. Check that Notion databases are shared with integration

### "401 Unauthorized" Error

**Cause**: Invalid or missing `NOTION_API_KEY`

**Solution**:
1. Verify API key starts with `noti_`
2. Copy directly from https://www.notion.com/my-integrations
3. Update in Vercel **Settings** → **Environment Variables**
4. Redeploy after updating

### "404 Database Not Found"

**Cause**: Wrong database ID format or database not shared

**Solution**:
1. Verify database ID is 32 alphanumeric characters
2. Check database is shared with "Wedding Planner" integration (Edit access)
3. Verify ID copied correctly from URL
4. Test by viewing database in Notion - should be editable

### CORS Errors

**Error**: "Access-Control-Allow-Origin" error in console

**Solution**:
- Already handled by serverless functions
- If still occurring, check:
  1. Browser is accessing `https://` (not `http://`)
  2. Notion API key is valid
  3. Deployment completed successfully

---

## Continuous Deployment

### Auto-Deploy on Code Changes

Vercel automatically deploys when you push to GitHub:

```bash
# Make local changes to app.html
git add app.html
git commit -m "Update app styling"
git push origin main
```

Vercel detects changes and auto-deploys in ~1 minute.

### Rollback to Previous Deployment

In Vercel Dashboard:
1. Go to **Deployments** tab
2. Find previous working deployment
3. Click **...** menu
4. Select **Promote to Production**

---

## Monitoring & Analytics

### View Deployment Logs

In Vercel Dashboard:
1. Click **Deployments**
2. Select latest deployment
3. View **Build Logs** and **Runtime Logs**

### Monitor API Usage

Python functions automatically track:
- Request count
- Response times
- Error rates
- CPU time

View in Dashboard under **Analytics**.

### Edge Function Metrics

All API calls go through Vercel's global edge network:
- Sub-100ms response times from any location
- Automatic scaling
- No cold starts after initial request

---

## Update & Maintenance

### Update Dependencies

When updating Python packages:

```bash
# Local development
pip install --upgrade <package-name>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

Vercel auto-redeploys with new dependencies.

### Update Notion Databases

To add new fields to Notion databases:

1. Update database in Notion
2. Update corresponding `/api` file
3. Commit and push changes
4. Deployment updates automatically

---

## Performance Optimization

Your Vercel deployment includes:

✅ **Global CDN**: Static files served from edge locations worldwide  
✅ **Automatic Scaling**: Handles traffic spikes automatically  
✅ **Zero Downtime**: Deployments don't interrupt service  
✅ **Caching**: HTML cached for 1 hour by default  
✅ **Compression**: Automatic gzip/brotli compression  

---

## Support & Resources

### Vercel Documentation
- Deployment Guide: https://vercel.com/docs
- Python Functions: https://vercel.com/docs/functions/python
- Environment Variables: https://vercel.com/docs/projects/environment-variables

### Notion API Documentation
- Notion Developers: https://developers.notion.com
- API Reference: https://developers.notion.com/reference/intro
- Auth Guide: https://developers.notion.com/docs/getting-started/auth

### Your Project
- GitHub: `https://github.com/YOUR_USERNAME/wedding-planner`
- Live App: `https://wedding-planner-xxxxx.vercel.app`
- Local Setup: See `NOTION_SETUP.md`

---

## Next Steps

1. ✅ Deploy to Vercel (this guide)
2. ✅ Configure Notion integration
3. 🔄 Invite team members to app
4. 🔄 Set up custom domain (optional)
5. 🔄 Monitor analytics in Vercel Dashboard

Congratulations! Your wedding planner is live and syncing with Notion.
