from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATABASE = 'hustle_theory.db'

def get_db():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with tables"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # User progress table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL,
            completed BOOLEAN DEFAULT 0,
            score INTEGER DEFAULT 0,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(user_id, module_id)
        )
    ''')
    
    # Savings goals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            target_price REAL NOT NULL,
            allowance REAL NOT NULL,
            allowance_type TEXT NOT NULL,
            time_value INTEGER NOT NULL,
            time_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Badges table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS badges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            badge_name TEXT NOT NULL,
            earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# ========== ROOT & INFO ROUTES ==========

@app.route('/')
def home():
    """API information page"""
    return jsonify({
        'message': 'Hustle Theory API',
        'version': '1.0',
        'status': 'running',
        'database': 'SQLite (hustle_theory.db)',
        'endpoints': {
            'auth': {
                'POST /api/register': 'Register a new user',
                'POST /api/login': 'Login user'
            },
            'progress': {
                'GET /api/progress/<user_id>': 'Get user progress',
                'POST /api/progress': 'Update module progress'
            },
            'savings': {
                'GET /api/savings/<user_id>': 'Get savings goals',
                'POST /api/savings': 'Create savings goal'
            },
            'badges': {
                'GET /api/badges/<user_id>': 'Get user badges',
                'POST /api/badges': 'Award a badge'
            }
        }
    }), 200

@app.route('/api')
def api_info():
    """API documentation"""
    return jsonify({
        'message': 'Hustle Theory API - Financial Literacy for Teens',
        'version': '1.0',
        'documentation': 'See DATABASE_README.md for full API documentation'
    }), 200

# ========== AUTH ROUTES ==========

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                      (username, password))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'message': 'User registered successfully',
            'user_id': user_id,
            'username': username
        }), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Username already exists'}), 409

@app.route('/api/login', methods=['POST'])
def login():
    """Login user"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', 
                  (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({
            'message': 'Login successful',
            'user_id': user['id'],
            'username': user['username']
        }), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# ========== PROGRESS ROUTES ==========

@app.route('/api/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    """Get user's progress across all modules"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT module_id, completed, score, completed_at 
        FROM user_progress 
        WHERE user_id = ?
        ORDER BY module_id
    ''', (user_id,))
    
    progress = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(progress), 200

@app.route('/api/progress', methods=['POST'])
def update_progress():
    """Update or create user progress for a module"""
    data = request.json
    user_id = data.get('user_id')
    module_id = data.get('module_id')
    completed = data.get('completed', False)
    score = data.get('score', 0)
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO user_progress (user_id, module_id, completed, score, completed_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id, module_id) 
        DO UPDATE SET completed = ?, score = ?, completed_at = ?
    ''', (user_id, module_id, completed, score, 
          datetime.now() if completed else None,
          completed, score, datetime.now() if completed else None))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Progress updated successfully'}), 200

# ========== SAVINGS GOALS ROUTES ==========

@app.route('/api/savings/<int:user_id>', methods=['GET'])
def get_savings_goals(user_id):
    """Get all savings goals for a user"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM savings_goals 
        WHERE user_id = ?
        ORDER BY created_at DESC
    ''', (user_id,))
    
    goals = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(goals), 200

@app.route('/api/savings', methods=['POST'])
def create_savings_goal():
    """Create a new savings goal"""
    data = request.json
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO savings_goals 
        (user_id, item_name, target_price, allowance, allowance_type, time_value, time_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data['user_id'], data['item_name'], data['target_price'], 
          data['allowance'], data['allowance_type'], data['time_value'], data['time_type']))
    
    conn.commit()
    goal_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'message': 'Savings goal created', 'goal_id': goal_id}), 201

# ========== BADGES ROUTES ==========

@app.route('/api/badges/<int:user_id>', methods=['GET'])
def get_badges(user_id):
    """Get all badges earned by a user"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT badge_name, earned_at 
        FROM badges 
        WHERE user_id = ?
        ORDER BY earned_at DESC
    ''', (user_id,))
    
    badges = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(badges), 200

@app.route('/api/badges', methods=['POST'])
def award_badge():
    """Award a badge to a user"""
    data = request.json
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO badges (user_id, badge_name)
        VALUES (?, ?)
    ''', (data['user_id'], data['badge_name']))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Badge awarded successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
