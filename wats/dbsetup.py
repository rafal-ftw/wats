from basic import db, User, app

with app.app_context():
    db.create_all()

    tom = User('tom', 'tom@example.com')
    frank = User('frank', 'frank@example.com')


    db.session.add_all([tom, frank])
    db.session.commit()

