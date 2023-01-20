from flask import render_template, url_for, redirect, Blueprint
from susiety import db
from susiety.models import Post, Reply
from susiety.posts.forms import PostForm
from susiety.posts.utils import random_name

posts = Blueprint('posts', __name__)


@posts.route("/wall", methods=['GET', 'POST'])
def wall():
    form = PostForm()
    posts = Post.query.all()
    if form.validate_on_submit():
        name = random_name()
        post = Post(subject=form.subject.data, comment=form.comment.data, author=name)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.wall'))
    return render_template('wall.html', title='Wall', form=form, posts=posts)


@posts.route("/wall/<int:post_id>", methods=['GET', 'POST'])
def reply_wall(post_id):
    form = PostForm()
    posts = Post.query.all()
    replies = Reply.query.filter_by(subject=post_id)
    if form.validate_on_submit():
        name = random_name()
        if form.subject.data.isdigit():
            if int(form.subject.data) > len(posts):
                return redirect(url_for('posts.reply_wall', post_id=post_id))
            else:
                reply = Reply(subject=form.subject.data, comment=form.comment.data, author=name)
                db.session.add(reply)
                db.session.commit()
        else:
            post = Post(subject=form.subject.data, comment=form.comment.data, author=name)
            db.session.add(post)
            db.session.commit()
        return redirect(url_for('posts.reply_wall', post_id=post_id))
    return render_template('reply_wall.html', title='Wall', form=form, posts=posts, replies=replies)
