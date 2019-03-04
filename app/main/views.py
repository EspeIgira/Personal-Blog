from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User,Blog,Comment,Subscribe
from ..request import get_quotes

from .forms import BlogForm,UpdateProfile,CommentForm,SubscribeForm
from .. import db,photos



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    quote=get_quotes()

    title = 'Personal blog Website Online'
    all_blogs = Blog.query.all()

    return render_template('index.html',title = title, all_blogs = all_blogs, quote= quote)


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




#Able to comment,add,delete.................

@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    form = CommentForm()
    
    blog= Blog.query.filter_by(id=id).first()
    if  form.validate_on_submit():
        description = form.description.data
        comment = Comment(description=description, blogs_id  = id, user_id=current_user.id)
        comment.save_comments()
        return redirect(url_for('main.index'))


        db.session.add(comment)
        db.session.commit()

    return render_template('comment.html',form=form, blog= blog)


@main.route('/subscribe/',methods=["GET","POST"])
def subscribe():
    
    subscribeform=SubscribeForm()

    
    if form.validate_on_submit():
       
        # name = subscribeform.name.data
        email = subscribeform.email.data
        subscribe = Subscribe(email=email)
        subscribe.save_blogs() 

        db.session.add(subscribe)
        db.session.commit()
        
        mail_message("welcome to our Blog"/welcome_user,subscribe.email,user=subscribe)

        return redirect(url_for('main.index'))

        title="subscribe"
       

    return render_template('subscribe.html',subscribeform=subscribeform)


@main.route('/blog/', methods=['GET', 'POST'])
@login_required
def newblog():
    form = BlogForm()
    
    if form.validate_on_submit():
        
        blog = form.blog.data
        
        newblog = Blog(blog=blog,user_id=current_user.id)
        newblog.save_blogs() 
    
        return redirect(url_for('main.index'))


        db.session.add(blog)
        db.session.commit()

    return render_template('newblog.html', form=form)




