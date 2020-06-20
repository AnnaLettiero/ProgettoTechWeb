from Progetto.models import Users, Books, Reviews, db
from Progetto import app, bcrypt
from flask import render_template, url_for, flash, redirect
from Progetto.forms import RegistrationForm, LoginForm, ReviewForm
from flask_login import login_user, current_user, logout_user, login_required

reviewsdemo = [
    {
        'author': 'Sara22',
        'title': 'Il prigionero del cielo',
        'content': 'Recensione Il prigionero del cielo',
        'reviewdate': '10 Aprile 2019',
        'bookauthor': 'Carlos Ruiz Zafon',
    },
    {
        'author': 'DAmbra67',
        'title': 'Mille splendidi soli',
        'content': 'Recensione Mille splendidi soli',
        'reviewdate': '8 Febbraio 2019',
        'bookauthor': 'Khaled Hosseini',
    }
]

booksdemo = [
    {
        'idbook': 1,
        'title': 'Il prigionero del cielo',
        'author': 'Carlos Ruiz Zafon',
        'publisher': 'Feltrinelli',
        'releasedate': '10 Aprile 2019',
        
    },
    {
        'idbook': 2,
        'title': 'Mille splendidi soli',
        'author': 'Khaled Hosseini',
        'publisher': 'Feltrinelli',
        'releasedate': '10 Aprile 2019',
    }
]

@app.route("/recensioni")
@login_required
def recensioni():
    reviews = Reviews.query.order_by(Reviews.codbook.desc())
    return render_template('recensioni.html', reviews=reviews)  

#@app.route("/about")
#def about():
#    return render_template('about.html', title='About')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='home')


@app.route("/register", methods=['GET' , 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    print(form.username.data)
    if form.validate_on_submit():
        print("SUBMIT")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username = form.username.data, email = form.email.data, password = hashed_password, usertype='normale')
        print(form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET' , 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Errore. Perfavore controlla email e password', 'danger')
    #Altrimenti se acceduto col GET renderizza pagina di accesso
    return render_template('login.html', title='Login', form=form)


#@app.route("/newsletter")
#def newsletter():
#    return render_template('newsletter.html', title='Newsletter')


#@app.route("/search")
#def search():
#   return render_template('search.html', title='Cerca')

@app.route("/book")
def book():
    books = Books.query.order_by(Books.idbook.desc())
    return render_template('book.html', title='libri', books=books)  

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/bookview/<int:book_id>", methods=['GET' , 'POST'])
@login_required
def bookview(book_id):
    book = Books.query.filter_by(idbook=book_id).first()
    form = ReviewForm()
    if form.validate_on_submit():
        review = Reviews(type=form.title.data,content=form.content.data,coduser=current_user.id,codbook=book_id)
        db.session.add(review)
        db.session.commit()
        flash('Il tuo post è stato creato!', 'success')
        reviews = Reviews.query.filter_by(codbook=book_id)
        return render_template('bookview.html', title=book.title, book=book, reviews=reviews, form=form)
    reviews = Reviews.query.filter_by(codbook=book_id)
    return render_template('bookview.html', title=book.title, book=book, reviews=reviews, form=form)

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')