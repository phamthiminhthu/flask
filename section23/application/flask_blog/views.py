from flask import render_template, request, redirect, url_for, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー各が異なります。')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります。')
        else:
            session['logged_in'] = True
            flash('ログインしました。')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました。')
    return redirect(url_for('show_entries'))



