from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'








# from . import db
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash,check_password_hash
# from . import login_manager



# class User(db.Model,UserMixin):
# 	__tablename__='users'
# 	id=db.Column(db.Integer,primary_key=True)
# 	username=db.Column(db.String(255))
# 	password=db.Column(db.String(255))
# 	posts = db.relationship('Post', backref='user', lazy='dynamic')
# 	comments = db.relationship('Comment', backref='user', lazy='dynamic')
# 	likes = db.relationship('Upvote', backref='user', lazy='dynamic')
# 	dislikes = db.relationship('Downvote', backref='user', lazy='dynamic')
# 	favorites=db.relationship('Favourite', backref='user', lazy='dynamic')

# 	def verifypass(self,trial):
# 		return check_password_hash(self.password,trial)
# 	@property
# 	def passwd(self):
# 		raise AttributeError('You cannot read this!')
# 	@passwd.setter
# 	def passwd(self,passwd):
# 		self.password = generate_password_hash(passwd)
# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def favs(self):
# 		for fav in self.favorites.all():
# 			yield fav.post
# 	def __repr__(self):
# 		return '<User %r>' % self.username

# class Favourite(db.Model):
# 	__tablename__='favourites'
# 	id=db.Column(db.Integer,primary_key=True)
# 	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
# 	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def selfdestruct(self):
# 		db.session.delete(self)
# 		db.session.commit()

# class Post(db.Model):
# 	__tablename__='posts'
# 	id=db.Column(db.Integer,primary_key=True)
# 	text=db.Column(db.Text())
# 	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
# 	category=db.Column(db.String(255))
# 	likes=db.relationship('Upvote', backref='post', lazy='dynamic')
# 	dislikes=db.relationship('Downvote', backref='post', lazy='dynamic')
# 	comments=db.relationship('Comment', backref='post', lazy='dynamic')
# 	userfavs=db.relationship('Favourite', backref='post', lazy='dynamic')

# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def selfdestruct(self):
# 		for child in self.likes.all()+self.dislikes.all()+self.comments.all():
# 			child.selfdestruct()
# 		db.session.delete(self)
# 		db.session.commit()

# class Comment(db.Model):
# 	__tablename__='comments'
# 	id=db.Column(db.Integer,primary_key=True)
# 	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
# 	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
# 	text=db.Column(db.Text())
# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def selfdestruct(self):
# 		db.session.delete(self)
# 		db.session.commit()

# class Upvote(db.Model):
# 	__tablename__='upvotes'
# 	id=db.Column(db.Integer,primary_key=True)
# 	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
# 	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def selfdestruct(self):
# 		db.session.delete(self)
# 		db.session.commit()

# class Downvote(db.Model):
# 	__tablename__='downvotes'
# 	id=db.Column(db.Integer,primary_key=True)
# 	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
# 	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
# 	def save(self):
# 		db.session.add(self)
# 		db.session.commit()
# 	def selfdestruct(self):
# 		db.session.delete(self)
# 		db.session.commit()


