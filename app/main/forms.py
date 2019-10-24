from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField,TextAreaField, SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField('Pick Category here',choices=[('inspiration','Inspiration'),
                                                        ('pick-up','Pick Up Lines'),
                                                        ('interview','Interview Pitch'),
                                                        ('product','Product Pitch'),
                                                        ('promotion','Promotion Pitch')], validators=[Required()])
    title = StringField('Pitch Title',validators=[Required()])
    name = StringField('Authors Name', validators=[Required()])
    pitch = TextAreaField('Write your Pitch here', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    author = TextAreaField('Author')
    body = TextAreaField('Write your comment', validators=[Required()])
    vote = RadioField('Vote here',choices=[('upvote','upvote'),
                                            ('downvote','downvote')],validators=[Required()])
    submit = SubmitField('Submit')