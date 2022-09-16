from datetime import datetime

from flask import Blueprint, flash, url_for, render_template, request

from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserCreateForm
from app.models import UserModel

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/test')
def test():
    return {"response" : "ok"}

@bp.route('/', methods=('GET', 'POST'))
def register():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = UserModel.query.filter_by(user_id=form.user_id.data).first()
        if not user:
            user = UserModel(
                        user_id=form.user_id.data,
                        password=generate_password_hash(form.password.data),
                        email=form.email.data,
                        create_date=datetime.now(),
                        Allergy_list=""
                        )
            db.session.add(user)
            db.session.commit()

            return redirect('https://www.kogoon.me')
            
        else:
            flash('이미 존재하는 사용자입니다.')

    return render_template('register.html', form=form)