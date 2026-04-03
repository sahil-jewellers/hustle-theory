# Hustle Theory - Backend Setup Guide

## Database Overview

This project now uses **SQLite** with a **Flask** backend to store user data persistently.

### Database Tables

1. **users** - User authentication
   - id, username, password, created_at

2. **user_progress** - Track module completion
   - user_id, module_id, completed, score, completed_at

3. **savings_goals** - Store financial planning goals
   - user_id, item_name, target_price, allowance, allowance_type, time_value, time_type

4. **badges** - User achievements
   - user_id, badge_name, earned_at

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Database Auto-Initialization

The SQLite database (`hustle_theory.db`) will be created automatically when you first run the app.

## API Endpoints

### Authentication

- **POST** `/api/register` - Register new user

  ```json
  {
    "username": "john_doe",
    "password": "securepass123"
  }
  ```

- **POST** `/api/login` - Login user
  ```json
  {
    "username": "john_doe",
    "password": "securepass123"
  }
  ```

### Progress Tracking

- **GET** `/api/progress/<user_id>` - Get user's module progress
- **POST** `/api/progress` - Update module progress
  ```json
  {
    "user_id": 1,
    "module_id": 1,
    "completed": true,
    "score": 85
  }
  ```

### Savings Goals

- **GET** `/api/savings/<user_id>` - Get all savings goals
- **POST** `/api/savings` - Create new savings goal
  ```json
  {
    "user_id": 1,
    "item_name": "Headphones",
    "target_price": 3000,
    "allowance": 100,
    "allowance_type": "weekly",
    "time_value": 30,
    "time_type": "weeks"
  }
  ```

### Badges

- **GET** `/api/badges/<user_id>` - Get user's badges
- **POST** `/api/badges` - Award a badge
  ```json
  {
    "user_id": 1,
    "badge_name": "First Module Complete"
  }
  ```

## Frontend Integration

Update your JavaScript files to make API calls to the backend:

```javascript
// Example: Register user
fetch("http://localhost:5000/api/register", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    username: "john_doe",
    password: "password123",
  }),
})
  .then((res) => res.json())
  .then((data) => console.log(data));
```

## Development Tips

- The database file `hustle_theory.db` is created in the project root
- Use tools like [DB Browser for SQLite](https://sqlitebrowser.org/) to inspect the database
- CORS is enabled for local development
- In production, add proper password hashing (bcrypt) and authentication tokens (JWT)

## Next Steps

1. Update frontend JavaScript to connect to the API
2. Add password hashing for security
3. Implement JWT token-based authentication
4. Add input validation and error handling
5. Create a production deployment configuration
