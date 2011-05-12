# import MySQL module
import MySQLdb
# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="mysql", db="2007_vaalikone")
cursor = db.cursor()

def unserialize_answers(limitfrom, limitto):
	"""Function to facilitate database unserialization in steps in case database is so big it could not fit into memory in one piece"""
	cursor.execute("SELECT * FROM Users LIMIT %s,%s" % (limitfrom, limitto))
	rows = cursor.fetchall()
	newrows = []
	for row in rows:
		answers = row[8].split(";")
		newrow = {}
		newrow['user_id'] = row[1]
		for answer in answers:
			# check sanity of data, last line can be empty
			if answer == '': 
				break
			# build dictionary
			question = answer.split(":")[1]
			questionalternative = answer.split(":")[3]
			questionweight = answer.split(":")[4]
			newrow['answer_%s' % question] = questionalternative
			newrow['weight_%s' % question] = questionweight
		newrows.append(newrow)
	cursor.executemany("""
		INSERT INTO User_Answers SET
		user_id = %(user_id)s,
		answer_1 = %(answer_1)s,
		weight_1 = %(weight_1)s,
		answer_2 = %(answer_2)s,
		weight_2 = %(weight_2)s,
		answer_3 = %(answer_3)s,
		weight_3 = %(weight_3)s,
		answer_4 = %(answer_4)s,
		weight_4 = %(weight_4)s,
		answer_5 = %(answer_5)s,
		weight_5 = %(weight_5)s,
		answer_6 = %(answer_6)s,
		weight_6 = %(weight_6)s,
		answer_7 = %(answer_7)s,
		weight_7 = %(weight_7)s,
		answer_8 = %(answer_8)s,
		weight_8 = %(weight_8)s,
		answer_9 = %(answer_9)s,
		weight_9 = %(weight_9)s,
		answer_10 = %(answer_10)s,
		weight_10 = %(weight_10)s,
		answer_11 = %(answer_11)s,
		weight_11 = %(weight_11)s,
		answer_12 = %(answer_12)s,
		weight_12 = %(weight_12)s,
		answer_13 = %(answer_13)s,
		weight_13 = %(weight_13)s,
		answer_14 = %(answer_14)s,
		weight_14 = %(weight_14)s,
		answer_15 = %(answer_15)s,
		weight_15 = %(weight_15)s,
		answer_16 = %(answer_16)s,
		weight_16 = %(weight_16)s,
		answer_17 = %(answer_17)s,
		weight_17 = %(weight_17)s,
		answer_18 = %(answer_18)s,
		weight_18 = %(weight_18)s,
		answer_19 = %(answer_19)s,
		weight_19 = %(weight_19)s,
		answer_20 = %(answer_20)s,
		weight_20 = %(weight_20)s,
		answer_21 = %(answer_21)s,
		weight_21 = %(weight_21)s,
		answer_22 = %(answer_22)s,
		weight_22 = %(weight_22)s,
		answer_23 = %(answer_23)s,
		weight_23 = %(weight_23)s,
		answer_24 = %(answer_24)s,
		weight_24 = %(weight_24)s,
		answer_25 = %(answer_25)s,
		weight_25 = %(weight_25)s,
		answer_26 = %(answer_26)s,
		weight_26 = %(weight_26)s,
		answer_27 = %(answer_27)s,
		weight_27 = %(weight_27)s
		""", newrows)
	return

# count lines and insert all answers into new table
cursor.execute("SELECT count(*) FROM Users")
result = cursor.fetchone()
result[0]

a = 0
b = 1000
while a < result[0]:
	unserialize_answers(a, b)
	a = a+b
	b = b+1000

