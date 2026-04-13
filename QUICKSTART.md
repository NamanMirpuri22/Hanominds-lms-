# 🚀 Quick Start Guide - Hanominds LMS

## One-Time Setup (First Time Only)

### Windows Setup
```bash
# 1. Open PowerShell/Command Prompt
cd c:\Users\aalla kavya\Downloads\hanolms

# 2. Create virtual environment
python -m venv .venv

# 3. Activate it (PowerShell)
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python app.py
```

### Mac/Linux Setup
```bash
cd ~/Downloads/hanolms

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## Daily Usage (After First Setup)

### Windows
```bash
cd c:\Users\aalla kavya\Downloads\hanolms
.venv\Scripts\Activate.ps1
python app.py
```

### Mac/Linux
```bash
cd ~/Downloads/hanolms
source .venv/bin/activate
python app.py
```

Then open: **http://127.0.0.1:5000**

---

## 🔑 Default Login Credentials

### Student
- **Email**: `student@hanominds.com`
- **Password**: `password123`

### Instructor  
- **Email**: `instructor@hanominds.com`
- **Password**: `password123`

### Admin
- **Email**: `admin@hanominds.com`
- **Password**: `password123`

---

## 📊 What's Included

✅ **Backend**
- Flask REST API
- SQLite Database with 8 pre-loaded modules
- User authentication & role-based access
- Progress tracking system
- Leaderboard & gamification

✅ **Frontend**
- Modern, responsive UI (desktop, tablet, mobile)
- Student dashboard with progress tracking
- Instructor analytics dashboard
- Module editor for creating course content
- Quiz system with auto-grading
- Assignment submission system

✅ **Features**
- 2880+ lines of Python code
- 11 HTML templates
- Responsive CSS (1600+ lines)
- 8 seeded modules with content
- 40+ quiz questions
- Complete lesson materials

---

## 🎯 Key Instructor Features

1. **Manage Modules** → Create/edit course content
2. **Analytics** → See all student performance metrics
3. **View Students** → Monitor individual progress
4. **Edit Content** → Modify lessons, quizzes, assignments

---

## 🎓 Key Student Features

1. **Dashboard** → See available modules and progress
2. **Learn** → Study lessons with interactive content
3. **Quiz** → Test knowledge and get instant feedback
4. **Assignments** → Apply learning with coding tasks
5. **Leaderboard** → Compete and earn badges

---

## ⚠️ Important Notes

- **First run** creates SQLite database automatically
- **Database location**: `instance/app.db`
- **To reset**: Delete `instance/app.db` and restart
- **Debug mode** is ON (auto-reload enabled)
- **Port**: 5000 (ensure it's available)

---

## 🔄 Common Tasks

### Add a New Student
1. Login as Admin
2. Go to Admin Dashboard
3. Fill form with name, email, password
4. Select role as "student"
5. Submit

### Create New Module
1. Login as Instructor
2. Click "Add Module"
3. Enter title
4. Click created module to edit
5. Add lesson, quiz, assignment

### View Analytics
1. Login as Instructor
2. Click "Analytics"
3. See class-wide stats and individual student progress

### Take Quiz as Student
1. Login as Student
2. Go to Dashboard
3. Click on module
4. Click "Take Quiz"
5. Answer questions and submit
6. See instant score

---

## 📱 Responsive Breakpoints

- **Desktop**: 1024px+ (full layout)
- **Tablet**: 768px-1023px (adjusted grid)
- **Mobile**: 480px-767px (single column)
- **Mini**: <480px (optimized for small screens)

---

## 🆘 Troubleshooting

**App won't start?**
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Port 5000 in use?**
```bash
# Kill process on Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Database corrupted?**
```bash
# Reset everything
rm instance/app.db
python app.py  # Will recreate with seed data
```

---

## 📂 File Reference

```
hanolms/
├── app.py                 # Main application (2880+ lines)
├── models.py              # Database models (130+ lines)
├── requirements.txt       # Dependencies
├── README.md              # Full documentation
├── QUICKSTART.md          # This file
├── instance/app.db        # SQLite database (auto-created)
├── static/css/
│   ├── style.css          # Main styling (1200+ lines)
│   └── responsive.css     # Mobile-first responsive (600+ lines)
└── templates/             # 11 HTML templates (2000+ lines)
```

---

## ✨ What Makes This Special

🎨 **Beautiful UI** - Modern gradients, smooth animations, emoji icons
📱 **Fully Responsive** - Works perfectly on any device
🎮 **Gamified** - Points, badges, leaderboards, streaks
🔐 **Secure** - Password hashing, role-based access control
📊 **Analytics** - Comprehensive student performance tracking
🚀 **Fast** - Flask optimized, instant quiz grading
🎓 **Educational** - 8 complete Python modules with content

---

## 🎉 You're Ready!

Run the app and start learning/teaching Python! 🐍✨

Questions? Check README.md for detailed documentation.
