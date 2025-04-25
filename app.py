from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('sops.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sops
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  content TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_sop():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        conn = sqlite3.connect('sops.db')
        c = conn.cursor()
        c.execute('INSERT INTO sops (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        conn = sqlite3.connect('sops.db')
        c = conn.cursor()
        c.execute('SELECT * FROM sops WHERE title LIKE ?', ('%' + search_term + '%',))
        results = c.fetchall()
        conn.close()
        return render_template('search.html', results=results)
    return render_template('search.html')

@app.route('/sop/<int:sop_id>')
def view_sop(sop_id):
    conn = sqlite3.connect('sops.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sops WHERE id = ?', (sop_id,))
    sop = c.fetchone()
    conn.close()
    return render_template('view_sop.html', sop=sop)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 