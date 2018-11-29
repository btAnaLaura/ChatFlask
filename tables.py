from app import db

class User(db.Model): #Classe de usuário que herda da classe db.model que traz um modelo de tabela padrão.
	__tablename__ = "users" #nome da tabela no banco de dados
	
	#identificação dos campos:
	id = db.Column(db.Integer, primary_key = True) #id será uma coluna do nosso banco. Recebe como parâmetros o tipo(Integer) e que é uma chave  primária (primary_key)
	username = db.Column(db.String, unique = True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique = True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self): 
		return str(self.id)
	

	#Construtor
	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email

	#Melhorar a exibição dos registros no banco.
	def __repr__(self):
        	return "<User %r>" % self.username

class Post(db.Model):
	__tablebame__ = "posts"

	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', foreign_keys = user_id)

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id

	def __repr__ (self):
		return "<Post %r>" % self.id

class Friend(db.Model):
	__tablename__ = "friends"

	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', foreign_keys = user_id)
	friends = db.relationship('User', foreign_keys = friend_id)


