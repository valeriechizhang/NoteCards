from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Notebook, Card
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and Create database session
engine = create_engine('sqlite:///notecards.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Page handler
@app.route('/')
@app.route('/notebook')
def showNotebooks():
    notebooks = session.query(Notebook).all()
    return render_template('allbooks.html', notebooks = notebooks)

@app.route('/notebook/new', methods=['GET', 'POST'])
def newNotebook():
    if request.method == 'POST':
        name = request.form['notebook_name']
        description = request.form['notebook_description']
        newbook = Notebook(name = name, description = description)
        if name == '':
            error = 'The notebook\'s name should not be empty.'
            return render_template('newbook.html', error = error)
        session.add(newbook)
        session.commit()
        flash('New Notebook [%s] Successfully Created' % name)
        return redirect(url_for('showNotebooks'))
    else:
        return render_template('newbook.html')

@app.route('/notebook/<int:notebook_id>/edit', methods=['GET', 'POST'])
def editNotebook(notebook_id):
    notebook = session.query(Notebook).filter_by(id=notebook_id).one()
    if request.method == 'POST':
        name = request.form['notebook_name']
        description = request.form['notebook_description']
        if name == '':
            error = 'The notebook\'s name should not be empty.'
            return render_template('editbook.html', notebook=notebook, error = error)
        notebook.name = name
        notebook.description = description
        session.add(notebook)
        session.commit()
        flash("Notebook [%s] Successful Edited!" % notebook.name)
        return redirect(url_for('showNotebooks'))
    else:
        return render_template('editbook.html', notebook=notebook)

@app.route('/notebook/<int:notebook_id>/delete', methods=['GET', 'POST'])
def deleteNotebook(notebook_id):
    notebook = session.query(Notebook).filter_by(id=notebook_id).one()
    if request.method == 'POST':
        session.delete(notebook)
        session.commit()
        flash("Notebook [%s] Successful Deleted!" % notebook.name)
        return redirect(url_for('showNotebooks'))
    else:
        return render_template('deletebook.html', notebook=notebook)

@app.route('/notebook/<int:notebook_id>')
@app.route('/notebook/<int:notebook_id>/card')
def showCards(notebook_id):
    cards = session.query(Card).filter_by(notebook_id=notebook_id).all()
    return render_template("cards.html", cards=cards, notebook_id=notebook_id)

@app.route('/notebook/<int:notebook_id>/card/new', methods=['GET', 'POST'])
def newCard(notebook_id):
    if request.method == 'POST':
        term = request.form['card_term']
        tag = request.form['card_tag']
        description = request.form['card_description']
        if term == '':
            error = 'The card\'s term should not be empty.'
            return render_template('newcard.html', notebook_id=notebook_id, error = error)
        newcard = Card(term = term, tag = tag, description = description, notebook_id = notebook_id)
        session.add(newcard)
        session.commit()
        flash('New Card [%s] Successfully Created' % term)
        return redirect(url_for('showCards', notebook_id=notebook_id))
    else:
        return render_template('newcard.html', notebook_id=notebook_id)


@app.route('/notebook/<int:notebook_id>/card/<int:card_id>/edit', methods=['GET', 'POST'])
def editCard(notebook_id, card_id):
    card = session.query(Card).filter_by(id = card_id).one()
    if request.method == 'POST':
        term = request.form['card_term']
        tag = request.form['card_tag']
        description = request.form['card_description']
        if term == '':
            error = 'The card\'s term should not be empty.'
            return render_template('editcard.html', card=card, notebook_id=notebook_id, error = error)
        card.term = term
        card.tag = tag
        card.description = description
        session.add(card)
        session.commit()
        flash("Card [%s] Successful Edited!" % card.term)
        return redirect(url_for('showCards', notebook_id=notebook_id))
    else:
        return render_template('editcard.html', card=card, notebook_id=notebook_id)


@app.route('/notebook/<int:notebook_id>/card/<int:card_id>/delete', methods=['GET', 'POST'])
def deleteCard(notebook_id, card_id):
    card = session.query(Card).filter_by(id = card_id).one()
    if request.method == 'POST':
        session.delete(card)
        session.commit()
        flash("Card [%s] Successful Deleted!" % card.term)
        return redirect(url_for('showCards', notebook_id=notebook_id))
    else:
        return render_template('deletecard.html', card=card, notebook_id=notebook_id)

# JSON API endpoints
@app.route('/notebook/JSON')
def notebookJSON():
    notebooks = session.query(Notebook).all()
    return jsonify(notebooks=[n.serialize for n in notebooks])

@app.route('/notebook/<int:notebook_id>/card/JSON')
def notebookCardJSON(notebook_id):
    cards = session.query(Card).filter_by(notebook_id=notebook_id).all()
    return jsonify(cards=[c.serialize for c in cards])

@app.route('/notebook/card/<int:card_id>/JSON')
def cardJSON(card_id):
    card = session.query(Card).filter_by(id=card_id).one()
    return jsonify(card=card.serialize)

# User login functions


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)