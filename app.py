from flask import Flask, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('emails.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            body TEXT,
            received_at TEXT,
            sentiment TEXT DEFAULT 'Neutral',
            priority TEXT DEFAULT 'Not Urgent',
            response_draft TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_sample_data():
    conn = sqlite3.connect('emails.db')
    df = pd.read_csv('../sample_data/support_emails.csv')
    for _, row in df.iterrows():
        # Simple priority: if "urgent" or "critical" in subject → mark urgent
        priority = "Urgent" if any(kw in row['subject'].lower() for kw in ['urgent', 'critical', 'immediate', 'blocked']) else "Not Urgent"
        conn.execute('''
            INSERT INTO emails (sender, subject, body, received_at, priority, response_draft)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            row['sender'],
            row['subject'],
            row['body'],
            row['sent_date'],
            priority,
            "Thank you for your email. Our team will get back to you shortly."
        ))
    conn.commit()
    conn.close()

@app.route('/api/emails')
def get_emails():
    conn = sqlite3.connect('emails.db')
    conn.row_factory = sqlite3.Row
    emails = conn.execute('SELECT * FROM emails ORDER BY CASE WHEN priority="Urgent" THEN 0 ELSE 1 END').fetchall()
    conn.close()
    return jsonify([dict(email) for email in emails])

if __name__ == '__main__':
    init_db()
    if not os.path.exists('emails.db') or os.path.getsize('emails.db') == 0:
        load_sample_data()
    app.run(debug=True, port=5000)