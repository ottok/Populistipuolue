This is a project inspired by HS Open (http://blogit.hs.fi/hsnext/tama-on-kutsu-hs-open-14-3-sanomatalossa).

The visualisation is based on 2007 election machine data, originally available at http://blogit.hs.fi/hsnext/vaalikonedata-avoimeksi-kristilliset-eniten-avioliitossa and unserialized version at http://www.populistipuolue.fi/2007_vaalikone.sql).

The result is viewable at http://www.populistipuolue.fi/. As of 2011-05-12 the visualization is still in very early stages.

== SUMMARY ==

The source code and a description is available for learning purposes.

Data license: CC-AT-SA-NC (Copyright Sanoma Corporation 2011)
Code licence: AGPL (Copyright Seravo Oy 2011)

The data is in a MySQL database, which is manipulated with some Python code. As a development web server we use Django. The actual visualisation is made with JavaScript that draws SVG images from JSON data.

== INSTALLATION ==

An a Ubuntu machine, just run:
 sudo apt-get install mysql-server python-mysqldb django-project

Set user/pass: root/mysql

Download SQL data and import in local database:
 wget http://www.populistipuolue.fi/2007_vaalikone.sql
 mysql -u root -p 2007_vaalikone < 2007_vaalikone.sql

Get source
	git://github.com/ottokek/Populistipuolue.git

Run server
	cd Populistipuolue
	./manage.py runserver

Open site
	firefox localhost:8000/static/index.html

== HISTORY ==

First I fiddled around with CSV data from command line:

otto@HPG5050EO:~/Työpöytä/HS Open$ head 2007_vaalikone_users/2007_users.csv | cut -d \; -f 2,9-36
"User_id";"Answers";"CandidatesList";"PartiesList";"Created";"Modified"
"11718105386517402";"20:1:134:1:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:229:3:2:;"
"11718107047922833";"20:1:0:0:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:229:3:2:;"
"11718108872804467";"20:1:0:0:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:221:2:2:;45:26:0:0:2:;46:27:0:0:2:;"
"11718113351925319";"20:1:134:1:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:0:0:2:;"
"11718114070915404";"20:1:134:1:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:229:3:2:;"
"11718116005445614";"20:1:136:3:1:;21:2:140:3:2:;22:3:142:2:2:;23:4:148:3:2:;24:5:151:2:2:;25:6:155:3:2:;26:7:161:5:2:;27:8:164:3:2:;28:9:167:2:2:;29:10:171:3:2:;30:11:175:3:2:;31:12:178:2:2:;32:13:183:3:2:;33:14:185:2:2:;34:15:189:3:2:;35:16:191:2:2:;36:17:193:2:2:;37:18:197:2:2:;38:19:200:1:2:;39:20:204:3:2:;40:21:206:1:2:;41:22:209:1:2:;42:23:212:1:2:;43:24:219:4:2:;44:25:221:2:2:;45:26:225:3:2:;46:27:229:3:2:;"
"11718115993253185";"20:1:135:2:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:0:0:2:;"

otto@HPG5050EO:~/Työpöytä/HS Open/2007_vaalikone_users$ head 2007_users.csv | cut -d \; -f 9-36 | cut -d \; -f 1
"Answers"
"20:1:134:1:2:
"20:1:0:0:2:
"20:1:0:0:2:
"20:1:134:1:2:
"20:1:134:1:2:
"20:1:136:3:1:
"20:1:135:2:2:
"20:1:135:2:2:
"20:1:137:4:2:
otto@HPG5050EO:~/Työpöytä/HS Open/2007_vaalikone_users$ head 2007_users.csv | cut -d \; -f 9-36 | cut -d \; -f 2
"CandidatesList"
21:2:0:0:2:
21:2:0:0:2:
21:2:0:0:2:
21:2:0:0:2:
21:2:0:0:2:
21:2:140:3:2:
21:2:0:0:2:
21:2:139:2:2:
21:2:139:2:2:

20:1:0:0:2:;21:2:0:0:2:;22:3:0:0:2:;23:4:0:0:2:;24:5:0:0:2:;25:6:0:0:2:;26:7:0:0:2:;27:8:0:0:2:;28:9:0:0:2:;29:10:0:0:2:;30:11:0:0:2:;31:12:0:0:2:;32:13:0:0:2:;33:14:0:0:2:;34:15:0:0:2:;35:16:0:0:2:;36:17:0:0:2:;37:18:0:0:2:;38:19:0:0:2:;39:20:0:0:2:;40:21:0:0:2:;41:22:0:0:2:;42:23:0:0:2:;43:24:0:0:2:;44:25:0:0:2:;45:26:0:0:2:;46:27:229:3:2:;

I found out that the data structure is like this:

- kysymys-id
- kysymysnumero 1-27
- vastausvaihtoehto AnswerAlternative_id (137-229)
- AnswerAlternative_number (1-4)
- painoarvo 

My idea was to unserialize the data into something like:

2007_users_answers
- User_id
- Answer_1
- Weight_1
- Answer_2
- Weight_2
- ...

In stead of writing 1..27 by hand, I generated the command with some Python.

i=1
while i < 28:
	print """		answer_%s = %%(answer_%s)s,
		weight_%s = %%(weight_%s)s,""" % (i,i,i,i)
	i = i+1

i=1
while i < 28:
	print """answer_%s, weight_%s, """ % (i,i)
	i = i+1

Finally the table structure was:

CREATE TABLE User_Answers (
  user_id bigint(20) DEFAULT NULL,
  answer_1 int(3) DEFAULT NULL,
  weight_1 int(3) DEFAULT NULL,
  answer_2 int(3) DEFAULT NULL,
  weight_2 int(3) DEFAULT NULL, 
  answer_3 int(3) DEFAULT NULL,
  weight_3 int(3) DEFAULT NULL, 
  answer_4 int(3) DEFAULT NULL,
  weight_4 int(3) DEFAULT NULL, 
  answer_5 int(3) DEFAULT NULL,
  weight_5 int(3) DEFAULT NULL, 
  answer_6 int(3) DEFAULT NULL,
  weight_6 int(3) DEFAULT NULL, 
  answer_7 int(3) DEFAULT NULL,
  weight_7 int(3) DEFAULT NULL, 
  answer_8 int(3) DEFAULT NULL,
  weight_8 int(3) DEFAULT NULL, 
  answer_9 int(3) DEFAULT NULL,
  weight_9 int(3) DEFAULT NULL, 
  answer_10 int(3) DEFAULT NULL,
  weight_10 int(3) DEFAULT NULL, 
  answer_11 int(3) DEFAULT NULL,
  weight_11 int(3) DEFAULT NULL, 
  answer_12 int(3) DEFAULT NULL,
  weight_12 int(3) DEFAULT NULL, 
  answer_13 int(3) DEFAULT NULL,
  weight_13 int(3) DEFAULT NULL, 
  answer_14 int(3) DEFAULT NULL,
  weight_14 int(3) DEFAULT NULL, 
  answer_15 int(3) DEFAULT NULL,
  weight_15 int(3) DEFAULT NULL, 
  answer_16 int(3) DEFAULT NULL,
  weight_16 int(3) DEFAULT NULL, 
  answer_17 int(3) DEFAULT NULL,
  weight_17 int(3) DEFAULT NULL, 
  answer_18 int(3) DEFAULT NULL,
  weight_18 int(3) DEFAULT NULL, 
  answer_19 int(3) DEFAULT NULL,
  weight_19 int(3) DEFAULT NULL, 
  answer_20 int(3) DEFAULT NULL,
  weight_20 int(3) DEFAULT NULL, 
  answer_21 int(3) DEFAULT NULL,
  weight_21 int(3) DEFAULT NULL, 
  answer_22 int(3) DEFAULT NULL,
  weight_22 int(3) DEFAULT NULL, 
  answer_23 int(3) DEFAULT NULL,
  weight_23 int(3) DEFAULT NULL, 
  answer_24 int(3) DEFAULT NULL,
  weight_24 int(3) DEFAULT NULL, 
  answer_25 int(3) DEFAULT NULL,
  weight_25 int(3) DEFAULT NULL, 
  answer_26 int(3) DEFAULT NULL,
  weight_26 int(3) DEFAULT NULL, 
  answer_27 int(3) DEFAULT NULL,
  weight_27 int(3) DEFAULT NULL,  
  PRIMARY KEY (user_id)
) ENGINE=MyISAM AUTO_INCREMENT=127446 DEFAULT CHARSET=latin1;


Then I made scripts/unserialize_data.py to convert the data.

Examples of queries that can be made to this table:

SELECT COUNT(user_id) FROM User_Answers WHERE weight_1 = 3
SELECT COUNT(user_id) FROM User_Answers WHERE answer_1 = 1
SELECT COUNT(user_id) FROM User_Answers WHERE answer_1 = 1 AND answer_2 = 1

Dump new database into SQL: 
populistipuolue/static$ mysqldump -u root -p 2007_vaalikone > 2007_vaalikone.sql

From existing MySQL tables I made Django models automatically with:

./manage.py inspectdb >> povastausanalyysi/models.py

