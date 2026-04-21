# 🚀 Quick Start - Deploy in 5 Minutes

Fastest way to get your wedding planner live on Vercel.

## ⏱️ 5-Minute Deployment

### 1️⃣ Push to GitHub (2 min)

```bash
cd "E:\Pravin\Claude New\Wedding Planner"
git init
git add .
git commit -m "Wedding planner with Notion integration"
git remote add origin https://github.com/YOUR_USERNAME/wedding-planner.git
git branch -M main
git push -u origin main
```

### 2️⃣ Deploy to Vercel (2 min)

1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Paste: `https://github.com/YOUR_USERNAME/wedding-planner.git`
4. Click "Continue"
5. Select "Other" for framework
6. Click "Deploy"

### 3️⃣ Add Environment Variables (1 min)

While Vercel deploys:

1. Go to https://www.notion.com/my-integrations
2. Create integration: "Wedding Planner"
3. Copy API token
4. In Vercel **Settings** → **Environment Variables**, add:

```
NOTION_API_KEY=noti_your_token_here
DB_GUESTS_ID=your_id_here
DB_SUB_EVENTS_ID=your_id_here
DB_VENDORS_ID=your_id_here
DB_BOOKINGS_ID=your_id_here
DB_PROPERTIES_ID=your_id_here
DB_TASKS_ID=your_id_here
DB_ENTERTAINMENT_ID=your_id_here
DB_GIFTS_ID=your_id_here
DB_WEDDING_ID=your_id_here
DB_FAMILIES_ID=your_id_here
```

5. Save and redeploy

### ✅ Done!

Your app is live at: `https://wedding-planner-xxxxx.vercel.app`

---

## 📖 How to Get Database IDs (1 min)

For each Notion database:
1. Open it in Notion
2. Copy URL from address bar
3. Extract the 32-character ID

Example:
```
https://www.notion.so/workspace/abc123def456ghi789jkl012mno345pq?v=...
                           ^                          ^
                           This is your database ID (32 chars)
```

---

## ✨ Full Guides

If you need more details:

- **Complete Vercel Setup**: [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)
- **Notion Configuration**: [NOTION_SETUP.md](./NOTION_SETUP.md)
- **Pre-Deploy Checklist**: [DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md)
- **Project Overview**: [README.md](./README.md)

---

## 🧪 Test After Deployment

### Test 1: Check Landing Page
- Visit: `https://your-domain.vercel.app`
- Should see: Beautiful landing page with tabs

### Test 2: Open App
- Click "App" or visit: `https://your-domain.vercel.app/app.html`
- Should see: Dashboard with navigation

### Test 3: Create Data
- Click "+ New Wedding"
- Fill form and submit
- Page should show your wedding

### Test 4: Test Notion Sync
- Add a guest
- Click "☁️ Sync to Notion"
- Should see green notification
- Check Notion workspace - new guest page should appear

---

## 🆘 Troubleshooting

### Deployment Failed
Check Vercel build logs (Deployments tab → View → Build Logs)

### Sync Button Not Working
1. Check environment variables are set in Vercel
2. Check API URL in app.html matches deployment
3. Verify Notion databases are shared with integration

### "Invalid Database ID"
Double-check the ID format - should be 32 alphanumeric characters

---

## 📱 Test on Your Phone

After deployment:
```
1. Get your Vercel URL: https://wedding-planner-xxxxx.vercel.app
2. Share with others: https://qr.code/your-url
3. Mobile browser auto-adapts layout
4. LocalStorage works on mobile too
```

---

## 🎉 You're Live!

Your wedding planner is now:
- ✅ Live on the internet
- ✅ Accessible from any device
- ✅ Syncing to Notion
- ✅ Auto-scaling for traffic
- ✅ Protected with HTTPS

Share the URL with your family and start planning! 💍

---

## 🔗 Useful Links

| What | Where |
|---|---|
| Your App | `https://wedding-planner-xxxxx.vercel.app` |
| Vercel Dashboard | https://vercel.com/dashboard |
| GitHub Repository | `https://github.com/YOUR_USERNAME/wedding-planner` |
| Notion Workspace | https://www.notion.so |
| API Health Check | `https://your-domain.vercel.app/api/health` |

---

## 📞 Next Steps

1. **Share the URL** with family and team
2. **Start creating weddings** and adding guests
3. **Monitor analytics** in Vercel Dashboard
4. **Read full docs** if you need advanced features

**Questions?** See [README.md](./README.md) or the detailed guides.

Happy Planning! 🎊✨
