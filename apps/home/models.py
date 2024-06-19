from apps import db


class Assets(db.Model):

    __tablename__ = 'Assets'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    type = db.Column(db.String(64))
    group = db.Column(db.String(64))
    value = db.Column(db.Integer)
    remark = db.Column(db.String(64))
    create_time = db.Column(db.DateTime)


    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, property, value)

