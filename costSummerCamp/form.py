from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,IntegerField,BooleanField,SubmitField,SelectField
from wtforms.validators import DataRequired
from costSummerCamp.model import Cost
from costSummerCamp import db,app


class CostAdd(FlaskForm):
    name = StringField('费用名',validators=[DataRequired(message=u'费用名不可以为空'),])
    price = FloatField('该费用的价格',validators=[DataRequired(message=u'费用价格不可以为空'),])
    unit = StringField('该费用的单位',validators=[DataRequired(message=u'费用单位不可以为空'),])
    specification  = StringField('该费用的规格',validators=[DataRequired(message=u'费用规格不可以为空'),])
    classify = SelectField('该费用所属的类别',validators=[DataRequired(message=u'费用类别不可以为空'),],choices=[(1,'书法'), (2,'右脑模式'), (3,'水彩写生上色'), (4,'交通补贴')],coerce = int)
    isConsumables = BooleanField('是否是消耗品',default=False)
    isRealPrice = BooleanField('是否是真实的价格',default=False)
    submit = SubmitField('提交')

class CostDetailsAdd(FlaskForm):

    costName = SelectField('请选择费用的名字',validators=[DataRequired(message=u'费用名一定要选择喲')], coerce = int)
    number = IntegerField('请输入该费用产生的数量',validators=[DataRequired(message=u'费用数量一定要填写呦'),])
    submit = SubmitField('提交')


    def __init__(self, *args, **kwargs):
        super(CostDetailsAdd, self).__init__(*args, **kwargs)
        self.costName.choices = db.session.query(Cost.id, Cost.name).all()

