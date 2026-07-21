from flask import Blueprint, render_template, url_for, redirect, request
from pybo.models import Question
from datetime import datetime
from pybo import db
from pybo.forms import QuestionForm, AnswerForm


bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()     # 상세 조회 라우터 내부에서 빈 답변 폼 생성
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

# 질문 등록 라우트 함수 추가
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question._list'))
    return render_template('question/question_form.html', form=form)