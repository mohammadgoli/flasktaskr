from views import db
from models import Task
from datetime import date

db.create_all()
db.session.add(Task("finish this shit", date(2015, 3, 13), 10, 1))
db.session.add(Task("date :))", date(2015, 3, 13), 10, 1))

db.session.commit()
