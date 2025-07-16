from flask import Flask
from extensions import db
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    test_user = User(
        name='Teste',
        email='teste@example.com',
        password='123456'
    )
    db.session.add(test_user)
    db.session.commit()
    print(f"Utilizador criado: {test_user.name} ✅")

