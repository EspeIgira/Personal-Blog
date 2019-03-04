from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User,Blogs,Comments,Subscribe
from ..request import get_blogs

from .forms import UserForm,UpdateProfile,AddBlog
from .. import db,photos



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form = UserForm()

    


    title = 'Personal blog Website Online'
    
    # all_comments = Comments.get_comments()

    return render_template('index.html',title = title, form=form)

#Link user file and index file.............   

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/comment/')
def comment():

    return render_template("new_user.html")


@main.route('/subscribe/')
def subscribe():

    return render_template("new_user.html")

@main.route('/delete/')
def delete():

    return render_template("new_user.html")

@main.route('/update/')
def update():

    return render_template("new_user.html")

#Able to comment,add,vote.................
@main.route('/newcomment/',methods = ['GET','POST'])
# @login_required
def newcomment():

    form = AddBlog()
  
    if form.validate_on_submit():
       
        comments= form.comments.data

        # Updated review instance
        newcomment = Comments(comments = comments ,user_id=current_user.id)

        # save review method
        newcomment.save_comments()
        return redirect(url_for('.index'))

   
    return render_template('new_user.html',form=form)

# @main.route('/comment/')
# def comment():

#     return render_template("comment.html")

# @main.route('/vote/')
# def vote():

#     return render_template("new_user.html")







