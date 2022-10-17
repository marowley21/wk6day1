from app.models import User
User.query.all()
[User: bigpoppa@biggie.net | 1 ]
User.query.all()[0]
User: bigpoppa@biggie.net | 1 
User.query.all()[0].first_name
'Marcus'
User.query.get(1)
<User: bigpoppa@biggie.net | 1 >
User.query.filter_by(first_name="Marcus")
<flask_sqlalchemy.query.Query object at 0x7f7249523f10>
User.query.filter_by(first_name="Marcus").all()
[User: bigpoppa@biggie.net | 1 ]
User.query.filter_by(first_name="Marcus").first()
<User: bigpoppa@biggie.net | 1 >
User.query.filter_by(first_name="Marcus").count()
1
User.query.filter(User.name == "Marcus").all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'User' has no attribute 'name'
User.query.filter(User.first_name == "Marcus").all()
[<User: bigpoppa@biggie.net | 1 >]
User.query.filter(User.id < 7).all()
[<User: bigpoppa@biggie.net | 1 >]