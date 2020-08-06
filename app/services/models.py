from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(256), index=True, unique=True)
    is_send = db.Column(db.Boolean())

    def __repr__(self):
        return '<Job {} {}>'.format(self.title, self.description)