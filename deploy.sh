#!/bin/bash
# Wedding Planner - Vercel Deployment Script
# This script automates the deployment process

set -e  # Exit on error

echo "=========================================="
echo "🚀 Wedding Planner - Vercel Deployment"
echo "=========================================="
echo ""

# Step 1: Initialize Git if needed
echo "Step 1️⃣ : Checking Git Status..."
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    git config user.email "wedding-planner@example.com"
    git config user.name "Wedding Planner Bot"
else
    echo "✅ Git repository already initialized"
fi

echo ""

# Step 2: Add and commit files
echo "Step 2️⃣ : Staging Files..."
git add .
echo "✅ Files staged for commit"

echo ""
echo "Step 3️⃣ : Creating Commit..."
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit"
else
    git commit -m "🎊 Wedding Planner - Full deployment with Notion integration

Features:
- Complete family event coordination system
- Notion cloud storage integration
- Multi-sided privacy (Bride/Groom/Solo)
- Serverless Python backend
- Responsive web application
- LocalStorage persistence

Includes:
- 6 serverless API functions
- Comprehensive documentation
- Deployment guides and checklists
- API testing utilities"
    echo "✅ Changes committed"
fi

echo ""
echo "=========================================="
echo "📋 Git Status:"
git status
echo "=========================================="
echo ""

# Step 3: Show GitHub instructions
echo "Step 4️⃣ : GitHub Setup Instructions"
echo "----------------------------------------"
echo "To complete deployment, you need to:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   👉 https://github.com/new"
echo ""
echo "2. Name it: wedding-planner"
echo ""
echo "3. Run these commands to push your code:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/wedding-planner.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. Then deploy on Vercel:"
echo "   👉 https://vercel.com/new"
echo ""
echo "   - Click 'Import Git Repository'"
echo "   - Paste: https://github.com/YOUR_USERNAME/wedding-planner.git"
echo "   - Select 'Other' for framework"
echo "   - Click Deploy"
echo ""
echo "5. Add Environment Variables in Vercel Settings:"
echo ""
echo "   NOTION_API_KEY=noti_your_token_here"
echo "   DB_WEDDING_ID=your_id"
echo "   DB_GUESTS_ID=your_id"
echo "   DB_SUB_EVENTS_ID=your_id"
echo "   DB_VENDORS_ID=your_id"
echo "   DB_BOOKINGS_ID=your_id"
echo "   DB_PROPERTIES_ID=your_id"
echo "   DB_TASKS_ID=your_id"
echo "   DB_ENTERTAINMENT_ID=your_id"
echo "   DB_GIFTS_ID=your_id"
echo "   DB_FAMILIES_ID=your_id"
echo ""
echo "=========================================="
echo "✅ Git preparation complete!"
echo "=========================================="
echo ""
echo "📖 Next: Follow the instructions above to complete deployment"
