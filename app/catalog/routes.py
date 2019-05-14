from app.catalog import main
from app.catalog.models import Book, Publication
from flask import render_template, flash, redirect,request, url_for
from flask_login import login_required
from app.catalog.forms import EditBook,CreateBook
from app import db

@main.route('/')
def display():
    listBooks = Book.query.all()

    return render_template('home.html', books = listBooks)

@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id = publisher_id).all()
    return render_template('publisher.html', publisher = publisher, publisher_books = publisher_books)


@main.route('/delete/<book_id>', methods = ['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash("Deleted Succes-ly")

        return redirect(url_for('main.display'))
    return  render_template('delete-book.html', book = book, book_id = book_id)

@main.route('/edit/<book_id>', methods = ['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBook(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash("Book is updated")
        return redirect(url_for('main.display'))


    return render_template('edit.html', form = form)

@main.route('/create/<pub_id>', methods = ['GET', 'POST'])
@login_required
def create_book(pub_id):

    form = CreateBook()

    form.pub_id.data = pub_id

    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data,format=form.format.data,

                    image=form.img.data, num_pages=form.num_pages.data,pub_id = form.pub_id.data)

        db.session.add(book)
        db.session.commit()
        flash("Book added")

        return redirect(url_for('main.display_publisher', publisher_id = pub_id))

    return render_template('create-book.html', form = form)
