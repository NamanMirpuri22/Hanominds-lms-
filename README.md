# 🐍 Hanominds LMS - Kid-Friendly Python Learning Platform

**A modern, interactive Learning Management System (LMS) designed specifically for kids to learn Python programming in a fun, gamified environment with instructor analytics and progress tracking.**

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [User Roles](#user-roles)
- [Database Schema](#database-schema)
- [API Routes](#api-routes)
- [Customization](#customization)
- [Screenshots & UI](#screenshots--ui)

---

## ✨ Features

### 🎓 Student Features
- **Interactive Modules**: Guided lessons with explanations, examples, activities, and code boxes
- **Quizzes**: Multi-question quizzes with instant scoring (auto-graded)
- **Assignments**: Code submission tasks to reinforce learning
- **Progress Tracking**: Visual progress bars showing module completion rates
- **Points & Badges**: Gamification with leaderboard rankings
- **Module Unlock System**: Complete a module to unlock the next one
- **Responsive UI**: Works on desktop, tablet, and mobile devices

### 👨‍🏫 Instructor Features
- **Module Management**: Create, edit, and organize course modules
- **Content Editing**: Edit lesson content, quiz questions, and assignments
- **Student Analytics**: 
  - Class-wide statistics (avg completion, avg quiz score)
  - Individual student performance metrics
  - Detailed module-by-module progress for each student
  - Leaderboard with points and badges
- **Student Management**: View all enrolled students and their progress
- **Dashboard**: Quick access to key metrics and management tools

### 👨‍💼 Admin Features
- **User Management**: Add/remove users with different roles
- **Role Assignment**: Assign students, instructors, and admin roles
- **System Overview**: Access to all user data and system statistics

---

## 📁 Project Structure

```
hanolms/
├── app.py                          # Main Flask application
├── models.py                       # SQLAlchemy database models
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── static/
│   └── css/
│       ├── style.css              # Main stylesheet (modern UI)
│       └── responsive.css         # Mobile-first responsive design
│
├── templates/
│   ├── login.html                 # Login page
│   ├── student-dashboard.html     # Student main dashboard
│   ├── course.html                # Course overview
│   ├── module.html                # Module content viewer
│   ├── quiz.html                  # Quiz interface (dynamically generated)
│   ├── instructor-dashboard.html  # Instructor main dashboard
│   ├── manage-modules.html        # Module management
│   ├── edit-module.html           # Module editor
│   ├── add-module.html            # Add new module
│   ├── instructor-analytics.html  # Student performance analytics
│   ├── view-students.html         # Student list
│   └── admin-dashboard.html       # Admin panel
│
└── instance/
    └── app.db                     # SQLite database (auto-created)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Flask 3.1.3 |
| **Database** | SQLite + SQLAlchemy 2.0 |
| **Frontend** | Jinja2 Templates, HTML5, CSS3 |
| **Styling** | Modern CSS with gradients, animations, and responsive design |
| **Authentication** | Session-based with password hashing |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone/Download Project
```bash
cd c:\Users\aalla kavya\Downloads\hanolms
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Application
```bash
python app.py
```

The app will be available at: **http://127.0.0.1:5000**

---

## 🚀 Usage Guide

### First-Time Setup

1. **Start the App**: Run `python app.py`
2. **Login**: Navigate to http://127.0.0.1:5000
3. **Seeded Accounts**:
   - **Instructor**: Email: `instructor@hanominds.com` | Password: `password123`
   - **Student**: Email: `student@hanominds.com` | Password: `password123`
   - **Admin**: Email: `admin@hanominds.com` | Password: `password123`

### Student Workflow

1. **Dashboard**: View all courses and progress
2. **Select Module**: Click on a module card to start learning
3. **Read Content**: Study lesson content, examples, and activities
4. **Take Quiz**: Complete the quiz with at least 50% to pass
5. **Submit Assignment** (if available): Submit code or text for grading
6. **Progress**: Once 50%+ score and assignment done, module completes and next unlocks
7. **Earn Rewards**: Gain points (10 per module) and badges for achievements

### Instructor Workflow

1. **Dashboard**: Access module management and student analytics
2. **Manage Modules**: 
   - Click "Manage Modules" to view all modules
   - Click "Edit" to modify lesson content, quiz, or assignment
   - Click "Add Module" to create new course content
3. **View Students**: See all enrolled students and their progress
4. **Analytics**: 
   - View class-wide statistics
   - Click "Analytics" to see detailed student performance
   - Check module-by-module completion rates
   - Monitor quiz scores and point accumulation

---

## 👥 User Roles

### Student
- **Permissions**: View courses, take quizzes, submit assignments, view own progress
- **Dashboard**: Course overview with progress bars, module links, points, badges
- **Can't Access**: Module management, analytics, admin panel, other student data

### Instructor
- **Permissions**: Create/edit modules, view all student data, analytics
- **Dashboard**: Module management, student list, analytics
- **Tools**: 
  - Edit lesson content (HTML-formatted)
  - Create/edit quiz questions with multiple choice options
  - Create assignment descriptions
  - View comprehensive student analytics

### Admin
- **Permissions**: User management, system overview
- **Dashboard**: Add/remove users, assign roles
- **Can't Access**: Module editing (instructor only)

---

## 🗄️ Database Schema

### Core Models

**User**
- id (PK)
- name, email, password_hash
- role: 'student', 'instructor', 'admin'
- status: 'active', 'inactive'

**Course**
- id (PK)
- title

**Module**
- id (PK)
- course_id (FK)
- title, order (display position)

**Lesson**
- id (PK)
- module_id (FK)
- content (HTML/markdown)

**Quiz** & **Question**
- quiz_id, question_id (PK)
- module_id (FK)
- question text, options (JSON), correct_answer

**Assignment**
- id (PK)
- module_id (FK)
- description

**Progress**
- id (PK)
- user_id (FK), module_id (FK)
- completed (boolean), quiz_score (0-100), assignment_done (boolean)

**Leaderboard**
- id (PK)
- user_id (FK)
- points, streak

**Badge** & **UserBadge**
- badge_id, badge_name, description
- user_id + badge_id tracking earned badges

---

## 🔌 API Routes

### Authentication
| Route | Method | Purpose |
|-------|--------|---------|
| `/login` | GET/POST | User login |
| `/logout` | GET | User logout |

### Student Routes
| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Student dashboard |
| `/course` | GET | Course overview |
| `/module/<id>` | GET | View module content |
| `/quiz/<id>` | GET/POST | Take quiz |
| `/assignment/<id>` | GET/POST | Submit assignment |

### Instructor Routes
| Route | Method | Purpose |
|-------|--------|---------|
| `/instructor-dashboard` | GET | Instructor main page |
| `/manage-modules` | GET | Module list |
| `/edit-module/<id>` | GET/POST | Edit module content |
| `/add-module` | GET/POST | Create new module |
| `/view-students` | GET | Student list |
| `/instructor-analytics` | GET | Student performance analytics |

### Admin Routes
| Route | Method | Purpose |
|-------|--------|---------|
| `/admin-dashboard` | GET | Admin panel |
| `/admin/add-user` | POST | Add new user |

---

## 🎨 UI/UX Features

### Modern Design
- **Gradient Backgrounds**: Eye-catching color transitions
- **Smooth Animations**: Bounce effects, fade-ins, hover states
- **Card-Based Layout**: Clean, organized information presentation
- **Icon Integration**: Emojis for visual appeal and quick identification

### Responsive Design
- **Desktop** (1024px+): Full layout with sidebars
- **Tablet** (768px-1023px): Adjusted grid and spacing
- **Mobile** (480px-767px): Single column, horizontal navigation
- **Small Mobile** (<480px): Optimized for tiny screens

### Accessibility
- Semantic HTML structure
- Proper color contrast ratios
- Keyboard navigation support
- Print-friendly stylesheets

---

## 🔧 Customization

### Add New Module Content

1. **Via UI** (Recommended):
   - Login as instructor
   - Click "Add Module"
   - Enter module title
   - Edit the module to add content, quiz, assignment

2. **Via Database**:
   ```python
   from app import db, Module, Lesson, Quiz, Assignment
   
   new_module = Module(course_id=1, title="Your Module", order=9)
   db.session.add(new_module)
   db.session.commit()
   ```

### Customize Styling

Edit `static/css/style.css` for:
- Color scheme (variables in `:root`)
- Typography (font families)
- Spacing and layout

Edit `static/css/responsive.css` for:
- Breakpoints and responsive behaviors
- Mobile-specific styling

### Create Quiz Questions

Structure in quiz questions:
```python
{
    "question": "What does 'def' mean in Python?",
    "options": '["Function definition", "Default value", "Data structure", "Module"]',
    "correct_answer": "A"
}
```

---

## 📊 Analytics Features

### Class Overview
- Total students enrolled
- Average completion rate (%)
- Average quiz score across all students
- Total modules in course

### Individual Student Performance
- Modules completed / Total modules
- Completion rate percentage (visual progress bar)
- Average quiz score (color-coded: red/good/excellent)
- Leaderboard points earned
- Badges unlocked
- Detailed module-by-module progress

---

## 🚨 Troubleshooting

### App won't start
- Ensure Python is installed: `python --version`
- Activate virtual environment
- Check port 5000 is not in use: `netstat -ano | findstr :5000`

### Database errors
- Delete `instance/app.db` to reset database
- Re-run app.py to recreate with seed data

### Module not appearing
- Check Module `course_id` matches Course id (default: 1)
- Verify Module is not deleted from database

### Quiz issues
- Ensure correct_answer is "A", "B", "C", or "D"
- Verify options JSON is valid

---

## 📝 License & Attribution

**Project**: Hanominds LMS v1.0
**Purpose**: Educational Python Learning Platform
**Created**: April 2026

---

## 🎯 Future Enhancements

- [ ] Video lesson support
- [ ] Real-time code execution environment
- [ ] Peer review system
- [ ] Discussion forums
- [ ] Certificates of completion
- [ ] Export progress reports (PDF)
- [ ] Email notifications
- [ ] Dark mode
- [ ] Multi-language support
- [ ] Mobile app (React Native/Flutter)

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review database schema to understand data flow
3. Inspect browser console (F12) for frontend errors
4. Check terminal output for backend errors

---

## 🎉 Thank You!

Enjoy teaching and learning Python with Hanominds LMS! 🐍✨
