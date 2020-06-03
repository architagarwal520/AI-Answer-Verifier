
from flask import Flask, render_template, request,redirect,url_for,session
from  models.nav_test import calc
import requests
from models import app
from models import db
from models import auth
import secrets

def get_QnA(module_id):	#finding question and answer and keyword based on id
	qna=[]
	all_users = db.child("Paper").get()
	for user in all_users.each():
		if user.key()==module_id:
			x=user.val()
			for key,value in x.items():
				if key.startswith("Q"):
					qna.append(value)
				if key.startswith("A"):
					qna.append(value)
				if key.startswith("K"):
					qna.append(value)
	return qna

def get_questions():  #getting all questions in a list
	questions=[]
	all_users = db.child("Paper").get()
	for user in all_users.each():
		question=user.val()
		for key,value in question.items():
			if key.startswith("Q"):
				questions.append(value)
	return questions

def get_answers():	#getting all answers in a list
	answers=[]
	all_users = db.child("Paper").get()
	for user in all_users.each():
		answer=user.val()
		for key,value in answer.items():
			if key.startswith("A"):
				answers.append(value)
	return answers


def get_keywords():	#getting all answers in a list
	keywords=[]
	all_users = db.child("Paper").get()
	for user in all_users.each():
		keyword=user.val()
		for key,value in keyword.items():
			if key.startswith("K"):
				keywords.append(value)
	return keywords
  

@app.route('/',methods=['POST','GET']) 
@app.route('/home',methods=['POST','GET']) 
def home():
	return render_template('home.html')


@app.route('/exam', methods=['POST', 'GET']) 
def exam(): 
	token=session.get('token',None)
	print("token:",token)
	if(token):
		question=[]
		answers=[]
		sol_by_student=[]
		result_calc=[]
		i=0
		question=get_questions()
		if request.method=='POST':
			answers=get_answers()
			keywords=get_keywords()
			for key,val in request.form.items():	#getting all the answers submitted by student
				sol_given=request.form[key]
				print(sol_given)
				str(sol_given)
				sol_by_student.append(sol_given)
			while(i<len(sol_by_student)):	#calculating result
				x=answers[i]
				y=sol_by_student[i]
				z=keywords[i]
				result_found=calc(x,y,z)
				result_calc.append(result_found)
				i=i+1
			return render_template('result.html',res=result_calc)
		return render_template('exam.html',title='Exam',question=question)
	else:
		return redirect(url_for('login'))



@app.route('/admin', methods=['POST', 'GET']) 
def admin():
	token=session.get('token',None)
	if(token=='wBrCxmN5qzZkoUI48eh2y9g3Hi83'):
		question=[]
		question=get_questions()
		keys=[]
		all_users = db.child("Paper").get()
		for user in all_users.each():
			key_of=user.key()
			keys.append(key_of)
		return render_template('admin.html',title='admin',question=question,keys=keys)
	elif(not token):
		return redirect(url_for('login'))
	else:
		return redirect(url_for('exam'))


@app.route('/admin/<module_id>', methods=['GET','POST']) 
def module(module_id):
	li=get_QnA(module_id)
	question=li[2]
	answer=li[0]
	keywords=li[1]
				
	return render_template('module.html',title='Module',question=question,answer=answer,key=module_id,keywords=keywords)


@app.route('/admin/<module_id>/update', methods=['GET','POST']) 
def module_update(module_id):
	li=get_QnA(module_id)
	question=li[2]
	answer=li[0]
	keywords=li[1]
	if request.method=='POST':
		q=request.form['ques']
		a=request.form['ans']
		k=request.form['keywords']
		db.child("Paper").child(module_id).update({"Q":q,"A":a,"K":k})
		return redirect(url_for('admin'))

	return render_template('new_module.html',question=question,answer=answer,keywords=keywords)
	

@app.route('/admin/<module_id>/delete', methods=['POST']) 
def delete_module(module_id):
	if request.method=="POST":
		db.child("Paper").child(module_id).remove()
		return redirect(url_for('admin'))
	

@app.route('/add', methods=['POST','GET']) 
def module_add():
	if request.method=='POST':
		q=request.form['ques']
		a=request.form['ans']
		k=request.form['keywords']
		data={"Q":q,"A":a,"K":k}
		db.child("Paper").push(data)
		return redirect(url_for('admin'))
	return render_template('new_module.html')


@app.route('/register',methods=['POST','GET']) 
def register():
	try:
		if request.method=='POST':
			email=request.form['e']
			password=request.form['p']
			user=auth.create_user_with_email_and_password(email, password)
			return redirect(url_for('login'))
	except:
		return "please try again"
	return render_template('register.html')


@app.route('/login',methods=['POST','GET']) 
def login():
	if request.method=='POST':
		email=request.form['e']
		password=request.form['p']
		user=auth.sign_in_with_email_and_password(email,password)
		token=user['localId']
		session['token']=token
		if(token=='wBrCxmN5qzZkoUI48eh2y9g3Hi83'):
			return redirect(url_for('admin'))
		else:
			return redirect(url_for('exam'))
	return render_template('login.html')

@app.route('/logout',methods=['POST','GET']) 
def logout():
	print("sessions:",session)
	for key in dict(session):
		session.pop(key)
	print("sessions after logout:",session)
	return redirect(url_for('home'))