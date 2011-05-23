# -*- coding: utf-8 -*-

from models import *
from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
import simplejson
#from django.utils.encoding import *
from decimal import *

'''
 this would be nice, but where to put in in template context?	
@register.filter
def multiply(value, arg):
	return int(value) * int(arg)
'''
	
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
			answeralternativecountpros = int(round(answeralternativecount/float(answercount)*100))
			# get possible next answeralternatives
			relations = []
			if question.question_number < 27:
				cursor.execute("SELECT DISTINCT(answer_%s) as answers FROM User_Answers WHERE answer_%s!=0 order by answers ASC" % (question.question_number+1,question.question_number+1))
				relationalternatives = cursor.fetchall()
				for relationalternative in relationalternatives:
					cursor.execute("SELECT COUNT(user_id) FROM User_Answers WHERE answer_%s=%s AND answer_%s=%s" % (question.question_number,answeralternative.answeralternative_number,question.question_number+1,relationalternative[0]))
					relationcount = cursor.fetchone()[0]
					relations.append(int(round(relationcount/float(answeralternativecount)*100)))
			subdata.append((
				answeralternative.answeralternative_number, 
				answeralternative.answer_text, 
				answeralternativecount,
				answeralternativecountpros,
				{"suhde_seuraaviin": relations}
			))
		data.append({
			"nro":question.question_number, 
			"kysymys":question.question, 
			"vastauksia":answercount,
			"painoarvo":{
				"pieni": [important_no, int(round(important_no/float(answercount)*100))], 
				"normaali": [important_na, int(round(important_na/float(answercount)*100))],
				"iso": [important_yes, int(round(important_yes/float(answercount)*100))]
			},
			"vastausvaihtoehdot":subdata
		})
	return data

def index(request):
	return render_to_response("index.html")

def tutkimus(request):
	return render_to_response("tutkimus.html", {'kysymykset':getdata()})

def kannatus(request):
	cursor.execute("""
		SELECT count(user_id) FROM User_Answers WHERE 
		answer_13 = 1 AND
		answer_21 != 3 AND
		answer_22 != 2 AND
		answer_4 != 1 AND
		answer_5 != 1 AND
		answer_6 != 4 AND
		answer_7 != 1 AND
		answer_9 != 1 AND
		(answer_11 = 2 OR answer_11 = 3)
	""")
	kannattajia = cursor.fetchone()[0]
	cursor.execute("SELECT count(user_id) FROM User_Answers")
	vastaajia = cursor.fetchone()[0]
	kannatus = int(round(kannattajia/float(vastaajia)*100))
	return render_to_response("kannatus.html", {'kannattajia':kannattajia, 'vastaajia':vastaajia, 'kannatus':kannatus, 'kysymykset':getdata()})

def index_json(request):
	return HttpResponse(simplejson.dumps(getdata(), sort_keys=True, indent=4 * ' '), mimetype='application/javascript')

