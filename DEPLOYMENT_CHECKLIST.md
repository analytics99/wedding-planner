# 🚀 Vercel Deployment Checklist

Quick checklist to deploy your wedding planner to Vercel.

## Pre-Deployment (Local)

- [ ] All files committed to local git repository
- [ ] `.env.example` created with all environment variables
- [ ] `requirements.txt` contains all Python dependencies
- [ ] `vercel.json` configured correctly
- [ ] `/api` directory has all serverless functions
- [ ] `app.html` points to correct API endpoints
- [ ] Test app locally: `python -m http.server 8000`
- [ ] Verify landing page loads: http://localhost:8000

## GitHub Setup

- [ ] GitHub account created
- [ ] New repository created: `wedding-planner`
- [ ] Local repo initialized: `git init`
- [ ] Remote added: `git remote add origin ...`
- [ ] Code pushed: `git push -u origin main`
- [ ] Repository visible on GitHub.com

## Notion Preparation

- [ ] Notion account with workspace
- [ ] Integration created: https://www.notion.com/my-integrations
  - [ ] Name: "Wedding Planner"
  - [ ] Token copied and saved securely
- [ ] 10 Notion databases created
  - [ ] Wedding Planning Hub
  - [ ] Guest List
  - [ ] Sub-Events
  - [ ] Vendors
  - [ ] Bookings & Payments
  - [ ] Properties & Accommodation
  - [ ] Tasks & Requirements
  - [ ] Entertainment & Performances
  - [ ] Gifts Received
  - [ ] Families
- [ ] Database IDs extracted (32 character codes)
  - [ ] `DB_WEDDING_ID`
  - [ ] `DB_GUESTS_ID`
  - [ ] `DB_SUB_EVENTS_ID`
  - [ ] `DB_VENDORS_ID`
  - [ ] `DB_BOOKINGS_ID`
  - [ ] `DB_PROPERTIES_ID`
  - [ ] `DB_TASKS_ID`
  - [ ] `DB_ENTERTAINMENT_ID`
  - [ ] `DB_GIFTS_ID`
  - [ ] `DB_FAMILIES_ID`
- [ ] All databases shared with "Wedding Planner" integration (Edit access)

## Vercel Deployment

- [ ] Vercel account created: https://vercel.com/signup
- [ ] GitHub account connected to Vercel
- [ ] Project imported: `https://github.com/USERNAME/wedding-planner`
- [ ] Environment variables configured in Vercel Settings:
  - [ ] `NOTION_API_KEY` = `noti_...`
  - [ ] `DB_WEDDING_ID` = database ID
  - [ ] `DB_GUESTS_ID` = database ID
  - [ ] `DB_SUB_EVENTS_ID` = database ID
  - [ ] `DB_VENDORS_ID` = database ID
  - [ ] `DB_BOOKINGS_ID` = database ID
  - [ ] `DB_PROPERTIES_ID` = database ID
  - [ ] `DB_TASKS_ID` = database ID
  - [ ] `DB_ENTERTAINMENT_ID` = database ID
  - [ ] `DB_GIFTS_ID` = database ID
  - [ ] `DB_FAMILIES_ID` = database ID
- [ ] Project deployed successfully
- [ ] Build logs show no errors
- [ ] Live URL generated: `https://wedding-planner-xxxxx.vercel.app`

## Post-Deployment Testing

### Frontend
- [ ] Landing page loads: `/`
- [ ] App page loads: `/app.html`
- [ ] Sidebar navigation works
- [ ] Create wedding form opens
- [ ] Create guest form opens
- [ ] Create event form opens
- [ ] LocalStorage saves data (refresh page, data persists)

### Backend API
- [ ] Health check: `https://YOUR_DOMAIN/api/health`
  - Should show: `{ "status": "healthy", "notion": "connected" }`
- [ ] API is accessible (no CORS errors)

### Notion Integration
- [ ] Test data created in app (wedding, guests, events)
- [ ] Click "☁️ Sync to Notion" for guests
  - Should show: "Synced X guests to Notion"
- [ ] Click "☁️ Sync to Notion" for events
  - Should show: "Synced X events to Notion"
- [ ] Click "☁️ Sync to Notion" for vendors
  - Should show: "Synced X vendors to Notion"
- [ ] Check Notion workspace
  - [ ] New pages in Guest List database
  - [ ] New pages in Sub-Events database
  - [ ] New pages in Vendors database
  - [ ] All fields populated correctly

## Optional: Custom Domain

- [ ] Custom domain registered (godaddy.com, namecheap.com, etc.)
- [ ] Domain configured in Vercel Settings → Domains
- [ ] DNS records updated per Vercel instructions
- [ ] SSL certificate issued (auto by Vercel)
- [ ] App accessible at custom domain

## Documentation

- [ ] README.md created
- [ ] NOTION_SETUP.md created
- [ ] VERCEL_DEPLOYMENT.md created
- [ ] DEPLOYMENT_CHECKLIST.md created
- [ ] .env.example created
- [ ] All documentation is clear and accurate

## Go Live

- [ ] Deployment verified working
- [ ] Notion sync tested
- [ ] Share app URL with family/team
- [ ] Monitor Vercel analytics
- [ ] Monitor Notion for sync issues
- [ ] Create backup of Notion data (optional)

## Maintenance

- [ ] Set reminder to monitor app usage
- [ ] Plan for feature additions
- [ ] Document any custom changes
- [ ] Keep dependencies updated
- [ ] Monitor Vercel logs for errors
- [ ] Archive deployment after wedding (optional)

---

## Quick Reference

### Deploy Again After Changes

```bash
# Make changes locally
git add .
git commit -m "Your message"
git push origin main
# Vercel auto-deploys in ~1 minute
```

### Rollback to Previous Version

1. Vercel Dashboard → Deployments
2. Find previous working deployment
3. Click ... menu → Promote to Production

### Check Logs

1. Vercel Dashboard → Deployments → Select latest
2. View Build Logs (build issues)
3. View Runtime Logs (API errors)

### Update Environment Variables

1. Vercel Dashboard → Settings → Environment Variables
2. Edit and save changes
3. Redeploy by pushing empty commit:
   ```bash
   git commit --allow-empty -m "Redeploy"
   git push origin main
   ```

---

## Support Links

- Vercel Dashboard: https://vercel.com/dashboard
- GitHub Repository: https://github.com/YOUR_USERNAME/wedding-planner
- Live App: https://your-domain.vercel.app
- Notion Integration: https://www.notion.com/my-integrations

---

**Status**: ⏱️ Ready to Deploy

Once all items are checked, your wedding planner is live and ready to use! 🎉
