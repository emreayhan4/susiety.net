from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    subject = StringField('Subject', render_kw={"placeholder": 'Subject / Reply'}, validators=[DataRequired(), Length(min=1, max=35)])
    comment = TextAreaField('Comment', render_kw={"placeholder": 'Comment', "rows": '3', "cols": '31'}, validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField('Post')
