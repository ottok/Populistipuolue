# -*- coding: utf-8 -*-

from models import *
from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
import simplejson
#from django.utils.encoding import *
from decimal import *

# import MySQL module
import MySQLdb
# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="mysql", db="2007_vaalikone")
cursor = db.cursor()

def getdata():
	questions = Questions.objects.all()
	data = []

	for question in questions:
		cursor.execute("SELECT count(user_id) FROM User_Answers WHERE answer_%s != 0" % question.question_number)
		answercount = cursor.fetchone()[0]
		cursor.execute("SELECT count(user_id) FROM User_Answers WHERE weight_%s=1" % question.question_number)
		important_no = cursor.fetchone()[0]
		cursor.execute("SELECT count(user_id) FROM User_Answers WHERE weight_%s=2" % question.question_number)
		important_na = cursor.fetchone()[0]
		cursor.execute("SELECT count(user_id) FROM User_Answers WHERE weight_%s=3" % question.question_number)
		important_yes = cursor.fetchone()[0]
		subdata = []
		answeralternatives = Answeralternatives.objects.filter(question_id=question.question_id)
		for answeralternative in answeralternatives:
			cursor.execute("SELECT count(user_id) FROM User_Answers WHERE answer_%s=%s" % (question.question_number,answeralternative.answeralternative_number))
			answeralternativecount = cursor.fetchone()[0]
			answeralternativecountpros = answeralternativecount/float(answercount)
			subdata.append((
				answeralternative.answeralternative_number, 
				answeralternative.answer_text, 
				answeralternativecount,
				answeralternativecountpros
			))
		data.append({
			"nro":question.question_number, 
			"kysymys":question.question, 
			"vastauksia":answercount,
			"painoarvo":{
				"pieni": [important_no, important_no/float(answercount)], 
				"normaali": [important_na, important_na/float(answercount)],
				"iso": [important_yes, important_yes/float(answercount)]
			},
			"vastausvaihtoehdot":subdata
		})
	return data

def index(request):
	return render_to_response("index.html")
#	return render_to_response("index.html", {'questions':getdata()}) # template made with old data model, should be updated to ned getdata() contents

def json(request):
	return HttpResponse(simplejson.dumps(getdata(), sort_keys=True, indent=4 * ' '), mimetype='application/javascript')


