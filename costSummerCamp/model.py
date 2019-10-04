from costSummerCamp import db
from datetime import datetime

class Cost (db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    name = db.Column(db.String,unique=True)
    price = db.Column(db.Float)
    unit = db.Column(db.String)
    specification = db.Column(db.String)
    classify = db.Column(db.String)
    isConsumables = db.Column(db.Boolean)
    isRealPrice = db.Column(db.Boolean)
    costdetails = db.relationship('CostDetails')

class CostDetails(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    costName = db.Column(db.String)
    number = db.Column(db.Integer)
    # timestamp = db.column(db.DateTime,default=datetime.now())
    cost_id = db.Column(db.Integer,db.ForeignKey('cost.id'))