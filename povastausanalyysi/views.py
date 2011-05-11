# -*- coding: utf-8 -*-

from models import *
from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
import json
#from django.utils.encoding import *

# import MySQL module
import MySQLdb
# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="mysql", db="2007_vaalikone")
cursor = db.cursor()

def index(request):
	questions = Questions.objects.all()
	data = []

	for question in questions:
		cursor.execute("SELECT count(*) FROM User_Answers WHERE weight_%s=1" % question.question_number)
		important_no = cursor.fetchone()[0]
		cursor.execute("SELECT count(*) FROM User_Answers WHERE weight_%s=2" % question.question_number)
		important_na = cursor.fetchone()[0]
		cursor.execute("SELECT count(*) FROM User_Answers WHERE weight_%s=3" % question.question_number)
		important_yes = cursor.fetchone()[0]
		subdata = []
		answeralternatives = Answeralternatives.objects.filter(question_id=question.question_id)
		for answeralternative in answeralternatives:
			cursor.execute("SELECT count(*) FROM User_Answers WHERE answer_%s=%s" % (question.question_number,answeralternative.answeralternative_number))
			subdata.append((answeralternative.answeralternative_number, answeralternative.answer_text, cursor.fetchone()[0]))
		data.append((question.question_number, question.question, important_no, important_na, important_yes, subdata))
	
	return render_to_response("index.html", {'questions':data})

