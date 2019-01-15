from __init__ import db, app


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    user_id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    gender = db.Column(db.VARCHAR(10), nullable=False, server_default='0')
    age = db.Column(db.INTEGER)
    address = db.Column(db.VARCHAR(255))
    mobile = db.Column(db.BIGINT)
    # Relationships
    spectacles = db.relationship('Spectacles',  secondary='user_spec', backref=db.backref('user_info', lazy='dynamic'))


class Spectacles(db.Model):
    __tablename__ = 'spectacles'
    spec_id = db.Column(db.INTEGER, primary_key=True)
    lens_brand = db.Column(db.VARCHAR(255), nullable=False, server_default=u'')
    left_power = db.Column(db.VARCHAR(255))
    right_power = db.Column(db.VARCHAR(255))
    purchase_date = db.Column(db.Date)
    price = db.Column(db.FLOAT)
    paid = db.Column(db.FLOAT)
    user_spec_id = db.Column(db.INTEGER)


class UserSpec(db.Model):
    __tablename__ = 'user_spec'
    id = db.Column(db.INTEGER(), primary_key=True)
    user_id = db.Column(db.INTEGER(), db.ForeignKey('user_info.user_id', ondelete='CASCADE'))
    user_spec_id = db.Column(db.INTEGER(), db.ForeignKey('spectacles.user_spec_id', ondelete='CASCADE'))
