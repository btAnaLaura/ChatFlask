#default terá as funções de rota
from flask import render_template, flash, redirect, url_for #Recebe um arquivo html e renderializa ele.
from app import app, db, lm #importando a variável app, que esta dentro do __init__ pricipal (/app/__init__.py)
from app.models.forms import LoginForm
from app.models.tables import User #importando as tabelas de usuarios
#decorator
from flask_login import login_user, logout_user


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/index") #A rota da função index é "/index".
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			flash("Logged in!")
			return redirect(url_for("index"))
		else:
			flash("Invalid login!")
	return render_template('login.html', form = form)

#@app.route("/teste/<info>")
#@app.route("/teste", defaults={"info": None})
#def teste(info):

@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out.")
	return redirect(url_for("index"))

	'''
	#Fazendo o CREATE
	i = User("alisson", "1234", "Alisson Romano", "alissonl09@outlook.com")
	db.session.add(i) #Sessao temporaria que esta ativa em um usuario e que esta ativa no banco
	db.session.commit() #commit - Salva as informacoes
	'''

	'''
	Fazendo o SELECT
	r = User.query.filter_by(username="alisson").all()
	print(r.username, r.name)
	return "Ok"
	'''

	'''
	Fazendo o UPDATE
	r = User.query.filter_by(username="alisson").first()
	r.name = "Alisson Rodrigues Romano"
	db.session.add(r)
	db.session.commit()
	return "Ok
	'''	

	'''
	Fazendo o DELETE
	r = User.query.filter_by(username="alisson").first()
	r.name = "Alisson Rodrigues Romano"
	db.session.delete(r)
	db.session.commit()
	return "Ok"
	'''
	
