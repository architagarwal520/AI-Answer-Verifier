
from flask import Flask, render_template, request,redirect,url_for
from  models.nav_test import calc
import requests
from models import app
from models import db
from models import auth

def get_QnA(module_id):	#finding question and answer based on id
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

  

@app.route('/',methods=['POST','GET']) 
@app.route('/exam', methods=['POST', 'GET']) 
def exam(): 
	question=[]
	answers=[]
	sol_by_student=[]
	result_calc=[]
	i=0
	question=get_questions()
	if request.method=='POST':
		answers=get_answers()
		for key,val in request.form.items():	#getting all the answers submitted by student
			sol_given=request.form[key]
			print(sol_given)
			str(sol_given)
			sol_by_student.append(sol_given)
		while(i<len(sol_by_student)):	#caalculating result
			x=answers[i]
			y=sol_by_student[i]
			result_found=calc(x,y)
			result_calc.append(result_found)
			i=i+1
		return render_template('result.html',res=result_calc)

	return render_template('exam.html',title='Exam',question=question)


@app.route('/admin', methods=['POST', 'GET']) 
def admin():
	question=[]
	question=get_questions()
	keys=[]
	all_users = db.child("Paper").get()
	for user in all_users.each():
		key_of=user.key()
		keys.append(key_of)
	return render_template('admin.html',title='admin',question=question,keys=keys)

@app.route('/admin/<module_id>', methods=['GET','POST']) 
def module(module_id):
	li=get_QnA(module_id)
	question=li[1]
	answer=li[0]
				
	return render_template('module.html',title='Module',question=question,answer=answer,key=module_id)


@app.route('/admin/<module_id>/update', methods=['GET','POST']) 
def module_update(module_id):
	li=get_QnA(module_id)
	question=li[1]
	answer=li[0]
	if request.method=='POST':
		q=request.form['ques']
		a=request.form['ans']
		db.child("Paper").child(module_id).update({"Q":q,"A":a})
		return redirect(url_for('admin'))

	return render_template('new_module.html',question=question,answer=answer)
	

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
		data={"Q":q,"A":a}
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
			return render_template('login.html')
	except expression as identifier:
		return "please again"
	
	return render_template('register.html')

