# 🎓 Hustle Theory - Financial Literacy for Teens

A comprehensive web application teaching financial literacy to teenagers through interactive modules, quizzes, and real-world scenarios.

## 📋 Project Overview

Hustle Theory is an educational platform designed to make financial literacy accessible and engaging for teens. The app features:

- **5 Interactive Learning Modules**
- **Quiz-based Learning System**
- **Progress Tracking with Database**
- **Badge & Achievement System**
- **Savings Goal Planner**

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python app.py
```

### 3. Open the App

- Navigate to `http://localhost:5000` (API)
- Open `auth.html` in your browser to start using the app

## 📂 Project Structure

```
hustle-theory/
├── app.py                  # Flask backend server
├── requirements.txt        # Python dependencies
├── hustle_theory.db       # SQLite database (auto-created)
├── inspect_db.py          # Database inspection tool
│
├── 📄 Main Pages
│   ├── index.html         # Dashboard (home page)
│   ├── auth.html          # Login/Register page
│   └── tracker.html       # Savings goal tracker
│
├── 📚 modules/            # Learning modules
│   ├── module1.html       # Income & Expenses
│   ├── module2.html       # Investments
│   ├── module3.html       # Insurance
│   ├── module4.html       # Taxes
│   └── module5.html       # Financial Scams & Safety
│
├── 🎨 assets/
│   ├── css/
│   │   └── style.css      # All styles
│   └── js/
│       ├── auth.js        # Authentication logic
│       ├── dashboard.js   # Dashboard functionality
│       ├── tracker.js     # Savings tracker
│       ├── module1.js     # Module 1 logic
│       ├── module2.js     # Module 2 logic
│       ├── module3.js     # Module 3 logic
│       ├── module4.js     # Module 4 logic
│       └── module5.js     # Module 5 logic
│
└── 📖 docs/               # Documentation
    ├── DATABASE_README.md
    ├── INTEGRATION_GUIDE.md
    └── MODULE_UPDATES.md
```

## 🎯 Features

### Learning Modules

1. **💰 Income & Expenses** - Learn budgeting basics and the 50-30-20 rule
2. **📈 Investments** - Understand stocks, mutual funds, and compound interest
3. **🛡️ Insurance** - Discover types of insurance and risk management
4. **🧾 Taxes** - Master income tax and GST concepts
5. **⚠️ Financial Scams** - Stay safe from phishing and fraud

### Interactive Tools

- **Investment Simulator** - Calculate compound interest returns
- **Tax Calculator** - Estimate income tax based on Indian slabs
- **Savings Goal Planner** - Plan how to save for your goals

### Gamification & Animations 🎨✨

- Progress tracking across all modules
- Badge system for achievements
- Unlockable modules based on completion
- **🦉 Smart Owl Mascot** - Appears on every page with encouraging messages
- **Smooth Animations**:
  - Bouncing mascot with hover effects
  - Rotating/spinning buttons on hover
  - Glowing pulse effect on hero buttons
  - Smooth slide-in entrance animations for page elements
  - Staggered animations for module cards
  - Interactive mascot click-to-speak feature

## 🗄️ Database

The app uses **SQLite** with the following tables:

- `users` - User accounts
- `user_progress` - Module completion tracking
- `savings_goals` - User savings goals
- `badges` - Earned achievements

To inspect the database:

```bash
python inspect_db.py
```

## 🔧 API Endpoints

### Authentication

- `POST /api/register` - Register new user
- `POST /api/login` - Login user

### Progress

- `GET /api/progress/<user_id>` - Get user progress
- `POST /api/progress` - Update module completion

### Savings

- `GET /api/savings/<user_id>` - Get savings goals
- `POST /api/savings` - Create savings goal

### Badges

- `GET /api/badges/<user_id>` - Get earned badges
- `POST /api/badges` - Award badge

## 🏆 Achievements

| Badge             | Requirement          |
| ----------------- | -------------------- |
| 🏆 Budget Boss    | Complete Module 1    |
| 💰 Smart Investor | Complete Module 2    |
| 🛡️ Risk Manager   | Complete Module 3    |
| 🧾 Tax Ninja      | Complete Module 4    |
| 🛡️ Scam Shield    | Complete Module 5    |
| 🏆 Hustle Master  | Complete all modules |

## 🛠️ Technologies Used

- **Backend**: Python, Flask, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **API**: RESTful API with JSON

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:

- **DATABASE_README.md** - API and database documentation
- **INTEGRATION_GUIDE.md** - Frontend-backend integration guide
- **MODULE_UPDATES.md** - Module structure and features

## 🎓 Educational Content

All financial concepts are tailored for Indian teenagers (ages 13-19) with:

- Real-world scenarios
- Interactive quizzes
- Age-appropriate language
- Indian currency (₹) and tax laws

## 🔐 Security Notes

**Current Implementation** (Development):

- Basic password storage (plain text)
- Local session management

**For Production** (Recommended):

- Implement password hashing (bcrypt)
- Add JWT token authentication
- Enable HTTPS
- Add input validation and sanitization

## 📝 License

College Project - 2026

## 👨‍💻 Author

Created as a college project to promote financial literacy among Indian teenagers.

## 🚀 Future Enhancements

- [ ] Password hashing and security
- [ ] JWT authentication
- [ ] Progress visualization charts
- [ ] Leaderboards
- [ ] Email notifications
- [ ] Mobile responsive design
- [ ] Deployment to cloud (Heroku/AWS)

---

**Made with ❤️ for financial literacy**
