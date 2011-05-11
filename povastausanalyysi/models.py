# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Agegroups(models.Model):
    group_id = models.IntegerField(primary_key=True, db_column='Group_id') # Field name made lowercase.
    start_age = models.IntegerField(null=True, db_column='Start_age', blank=True) # Field name made lowercase.
    end_age = models.IntegerField(null=True, db_column='End_age', blank=True) # Field name made lowercase.
    statistic_id = models.IntegerField(null=True, db_column='Statistic_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AgeGroups'

class Answeralternatives(models.Model):
    answeralternative_id = models.IntegerField(primary_key=True, db_column='AnswerAlternative_id') # Field name made lowercase.
    answeralternative_number = models.IntegerField(null=True, db_column='AnswerAlternative_number', blank=True) # Field name made lowercase.
    question_id = models.IntegerField(null=True, db_column='Question_id', blank=True) # Field name made lowercase.
    answer_text = models.TextField(db_column='Answer_text', blank=True) # Field name made lowercase.
    components = models.CharField(max_length=150, db_column='Components', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AnswerAlternatives'
        ordering = ['answeralternative_number']
        
class Answers(models.Model):
    user_answer_id = models.IntegerField(primary_key=True, db_column='User_answer_id') # Field name made lowercase.
    question_id = models.IntegerField(null=True, db_column='Question_id', blank=True) # Field name made lowercase.
    user_id = models.BigIntegerField(null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    answer_alternative_id = models.IntegerField(null=True, db_column='Answer_alternative_id', blank=True) # Field name made lowercase.
    weight = models.IntegerField(null=True, db_column='Weight', blank=True) # Field name made lowercase.
    explanation = models.TextField(db_column='Explanation', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Answers'

class Candidateresults(models.Model):
    result_id = models.IntegerField(primary_key=True, db_column='Result_id') # Field name made lowercase.
    election_type = models.CharField(max_length=30, db_column='Election_type', blank=True) # Field name made lowercase.
    area_number = models.IntegerField(null=True, db_column='Area_number', blank=True) # Field name made lowercase.
    municipal_number = models.IntegerField(null=True, db_column='Municipal_number', blank=True) # Field name made lowercase.
    municipal_area_number = models.IntegerField(null=True, db_column='Municipal_area_number', blank=True) # Field name made lowercase.
    info_type = models.CharField(max_length=30, db_column='Info_type', blank=True) # Field name made lowercase.
    party_name = models.CharField(max_length=150, db_column='Party_name', blank=True) # Field name made lowercase.
    candidate_number = models.IntegerField(null=True, db_column='Candidate_number', blank=True) # Field name made lowercase.
    candidate_name = models.CharField(max_length=600, db_column='Candidate_name', blank=True) # Field name made lowercase.
    age_electionday = models.IntegerField(null=True, db_column='Age_electionDay', blank=True) # Field name made lowercase.
    euro_member = models.IntegerField(null=True, db_column='Euro_member', blank=True) # Field name made lowercase.
    parlament_member = models.IntegerField(null=True, db_column='Parlament_member', blank=True) # Field name made lowercase.
    municipal_member = models.IntegerField(null=True, db_column='Municipal_member', blank=True) # Field name made lowercase.
    votes_this = models.IntegerField(null=True, db_column='Votes_this', blank=True) # Field name made lowercase.
    votes_this_percent = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Votes_this_percent', blank=True) # Field name made lowercase.
    elected = models.IntegerField(null=True, db_column='Elected', blank=True) # Field name made lowercase.
    comparing = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    results_update_time = models.CharField(max_length=15, db_column='Results_update_time', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CandidateResults'

class Candidatesuitabilities(models.Model):
    suitabilityid = models.IntegerField(primary_key=True, db_column='SuitabilityId') # Field name made lowercase.
    user_id = models.BigIntegerField(null=True, blank=True)
    candidate_id = models.IntegerField(null=True, db_column='Candidate_Id', blank=True) # Field name made lowercase.
    points = models.IntegerField(null=True, db_column='Points', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CandidateSuitabilities'

class Candidates(models.Model):
    candidate_id = models.IntegerField(primary_key=True, db_column='Candidate_id') # Field name made lowercase.
    area_id = models.IntegerField(null=True, db_column='Area_id', blank=True) # Field name made lowercase.
    party_id = models.IntegerField(null=True, db_column='Party_id', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, db_column='Published', blank=True) # Field name made lowercase.
    user_name = models.CharField(max_length=300, db_column='User_name', blank=True) # Field name made lowercase.
    password = models.CharField(max_length=300, db_column='Password', blank=True) # Field name made lowercase.
    first_name = models.CharField(max_length=300, db_column='First_name', blank=True) # Field name made lowercase.
    last_name = models.CharField(max_length=300, db_column='Last_name', blank=True) # Field name made lowercase.
    born = models.DateTimeField(null=True, db_column='Born', blank=True) # Field name made lowercase.
    candidate_number = models.IntegerField(null=True, db_column='Candidate_number', blank=True) # Field name made lowercase.
    sex = models.CharField(max_length=3, db_column='Sex', blank=True) # Field name made lowercase.
    profession = models.CharField(max_length=300, db_column='Profession', blank=True) # Field name made lowercase.
    profession_title = models.CharField(max_length=300, db_column='Profession_title', blank=True) # Field name made lowercase.
    education = models.IntegerField(null=True, db_column='Education', blank=True) # Field name made lowercase.
    working_sector = models.IntegerField(null=True, db_column='Working_sector', blank=True) # Field name made lowercase.
    marital_status = models.IntegerField(null=True, db_column='Marital_status', blank=True) # Field name made lowercase.
    children = models.IntegerField(null=True, db_column='Children', blank=True) # Field name made lowercase.
    photo = models.TextField(db_column='Photo', blank=True) # Field name made lowercase.
    uncommitted = models.IntegerField(null=True, db_column='Uncommitted', blank=True) # Field name made lowercase.
    parlament_member = models.IntegerField(null=True, db_column='Parlament_member', blank=True) # Field name made lowercase.
    euro_member = models.IntegerField(null=True, db_column='Euro_member', blank=True) # Field name made lowercase.
    municipal_member = models.IntegerField(null=True, db_column='Municipal_member', blank=True) # Field name made lowercase.
    homepage = models.CharField(max_length=300, db_column='Homepage', blank=True) # Field name made lowercase.
    video_link = models.CharField(max_length=600, db_column='Video_link', blank=True) # Field name made lowercase.
    free_field = models.TextField(blank=True)
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Candidates'

class Educationtypes(models.Model):
    type_id = models.IntegerField(primary_key=True, db_column='Type_id') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EducationTypes'

class Electionmachine(models.Model):
    machineid = models.IntegerField(primary_key=True, db_column='MachineId') # Field name made lowercase.
    election_type = models.CharField(max_length=12, db_column='Election_type', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    opened = models.IntegerField(null=True, db_column='Opened', blank=True) # Field name made lowercase.
    importinstanceworking = models.IntegerField(null=True, db_column='importInstanceWorking', blank=True) # Field name made lowercase.
    senderinstanceworking = models.IntegerField(null=True, db_column='SenderInstanceWorking', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ElectionMachine'

class Eventtypes(models.Model):
    event_id = models.IntegerField(primary_key=True, db_column='Event_id') # Field name made lowercase.
    event_type = models.CharField(max_length=300, db_column='Event_type', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EventTypes'

class Lettertexts(models.Model):
    row_id = models.IntegerField(primary_key=True, db_column='Row_id') # Field name made lowercase.
    type_id = models.IntegerField(null=True, blank=True)
    type_name = models.CharField(max_length=300, db_column='Type_name', blank=True) # Field name made lowercase.
    type_name_partitive = models.CharField(max_length=300, blank=True)
    letter_text = models.TextField(db_column='Letter_text', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LetterTexts'

class Log(models.Model):
    log_id = models.IntegerField(primary_key=True, db_column='Log_id') # Field name made lowercase.
    category = models.CharField(max_length=300, db_column='Category', blank=True) # Field name made lowercase.
    event_id = models.IntegerField(null=True, db_column='Event_id', blank=True) # Field name made lowercase.
    message = models.TextField(db_column='Message', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Log'

class Maritalstatuses(models.Model):
    status_id = models.IntegerField(primary_key=True, db_column='Status_id') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MaritalStatuses'

class Parliamentages(models.Model):
    age = models.IntegerField(null=True, blank=True)
    gr = models.IntegerField()
    class Meta:
        db_table = u'ParliamentAges'

class Parties(models.Model):
    party_id = models.IntegerField(primary_key=True, db_column='Party_id') # Field name made lowercase.
    shortening = models.CharField(max_length=60, db_column='Shortening', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    common_name = models.CharField(max_length=300, db_column='Common_name', blank=True) # Field name made lowercase.
    homepage = models.CharField(max_length=300, db_column='Homepage', blank=True) # Field name made lowercase.
    parlamient_party = models.IntegerField(null=True, db_column='Parlamient_party', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Parties'

class Partyresults(models.Model):
    result_id = models.IntegerField(primary_key=True, db_column='Result_id') # Field name made lowercase.
    election_type = models.CharField(max_length=30, db_column='Election_type', blank=True) # Field name made lowercase.
    area_number = models.IntegerField(null=True, db_column='Area_number', blank=True) # Field name made lowercase.
    municipal_number = models.IntegerField(null=True, db_column='Municipal_number', blank=True) # Field name made lowercase.
    municipal_area_number = models.IntegerField(null=True, db_column='Municipal_area_number', blank=True) # Field name made lowercase.
    party_number = models.IntegerField(null=True, db_column='Party_number', blank=True) # Field name made lowercase.
    list_party_number = models.IntegerField(null=True, db_column='List_party_number', blank=True) # Field name made lowercase.
    short_name = models.CharField(max_length=600, db_column='Short_name', blank=True) # Field name made lowercase.
    long_name = models.CharField(max_length=600, db_column='Long_name', blank=True) # Field name made lowercase.
    info_type = models.CharField(max_length=30, db_column='Info_type', blank=True) # Field name made lowercase.
    votes_count_this = models.IntegerField(null=True, db_column='Votes_count_this', blank=True) # Field name made lowercase.
    votes_percent_this = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Votes_percent_this', blank=True) # Field name made lowercase.
    places_this = models.IntegerField(null=True, db_column='Places_this', blank=True) # Field name made lowercase.
    votes_count_previous = models.IntegerField(null=True, db_column='Votes_count_previous', blank=True) # Field name made lowercase.
    votes_percent_previous = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Votes_percent_previous', blank=True) # Field name made lowercase.
    places_previous = models.IntegerField(null=True, db_column='Places_previous', blank=True) # Field name made lowercase.
    votes_count_previous2 = models.IntegerField(null=True, db_column='Votes_count_previous2', blank=True) # Field name made lowercase.
    votes_percent_previous2 = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Votes_percent_previous2', blank=True) # Field name made lowercase.
    results_update_time = models.CharField(max_length=15, db_column='Results_update_time', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PartyResults'

class Questioncategories(models.Model):
    category_id = models.IntegerField(primary_key=True, db_column='Category_id') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'QuestionCategories'

class Questiontypes(models.Model):
    type_id = models.IntegerField(primary_key=True, db_column='Type_id') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'QuestionTypes'

class Questions(models.Model):
    question_id = models.IntegerField(primary_key=True, db_column='Question_id') # Field name made lowercase.
    question_number = models.IntegerField(null=True, db_column='Question_number', blank=True) # Field name made lowercase.
    type_code = models.IntegerField(null=True, db_column='Type_code', blank=True) # Field name made lowercase.
    category_code = models.IntegerField(null=True, db_column='Category_code', blank=True) # Field name made lowercase.
    question = models.TextField(db_column='Question', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Questions'
        ordering = ['question_number']

class Selectionareaquestions(models.Model):
    row_id = models.IntegerField(primary_key=True, db_column='Row_id') # Field name made lowercase.
    question_id = models.IntegerField(null=True, db_column='Question_id', blank=True) # Field name made lowercase.
    area_id = models.IntegerField(null=True, db_column='Area_id', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SelectionAreaQuestions'

class Selectionarearesults(models.Model):
    result_id = models.IntegerField(primary_key=True, db_column='Result_id') # Field name made lowercase.
    election_type = models.CharField(max_length=30, db_column='Election_type', blank=True) # Field name made lowercase.
    area_number = models.IntegerField(null=True, db_column='Area_number', blank=True) # Field name made lowercase.
    municipal_number = models.IntegerField(null=True, db_column='Municipal_number', blank=True) # Field name made lowercase.
    municipal_area_number = models.IntegerField(null=True, db_column='Municipal_area_number', blank=True) # Field name made lowercase.
    shortening = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=600, db_column='Name', blank=True) # Field name made lowercase.
    info_type = models.CharField(max_length=30, db_column='Info_type', blank=True) # Field name made lowercase.
    voters_count_this = models.IntegerField(null=True, db_column='Voters_count_this', blank=True) # Field name made lowercase.
    voters_count_this_men = models.IntegerField(null=True, blank=True)
    voters_count_this_women = models.IntegerField(null=True, blank=True)
    voting_percent_this = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Voting_percent_this', blank=True) # Field name made lowercase.
    voted_count_this = models.IntegerField(null=True, db_column='Voted_count_this', blank=True) # Field name made lowercase.
    votes_computed_percent_this = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Votes_computed_percent_this', blank=True) # Field name made lowercase.
    candidates_count_this = models.IntegerField(null=True, db_column='Candidates_count_this', blank=True) # Field name made lowercase.
    voters_count_previous_same = models.IntegerField(null=True, db_column='Voters_count_previous_same', blank=True) # Field name made lowercase.
    voting_percent_previous_same = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Voting_percent_previous_same', blank=True) # Field name made lowercase.
    voters_count_previous = models.IntegerField(null=True, db_column='Voters_count_previous', blank=True) # Field name made lowercase.
    voting_percent_previous = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Voting_percent_previous', blank=True) # Field name made lowercase.
    results_type = models.CharField(max_length=6, db_column='Results_type', blank=True) # Field name made lowercase.
    results_update_time = models.CharField(max_length=15, db_column='Results_update_time', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SelectionAreaResults'

class Selectionareas(models.Model):
    area_id = models.IntegerField(primary_key=True, db_column='Area_id') # Field name made lowercase.
    area_number = models.IntegerField(null=True, db_column='Area_number', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    name2 = models.CharField(max_length=300, db_column='Name2', blank=True) # Field name made lowercase.
    homepage = models.CharField(max_length=300, db_column='Homepage', blank=True) # Field name made lowercase.
    picture = models.CharField(max_length=300, db_column='Picture', blank=True) # Field name made lowercase.
    link = models.CharField(max_length=300, db_column='Link', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, db_column='Published', blank=True) # Field name made lowercase.
    selectionunion = models.CharField(max_length=300, db_column='SelectionUnion', blank=True) # Field name made lowercase.
    defaultselectionarea = models.IntegerField(null=True, db_column='DefaultSelectionArea', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SelectionAreas'

class UserAnswers(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    answer_1 = models.IntegerField(null=True, blank=True)
    weight_1 = models.IntegerField(null=True, blank=True)
    answer_2 = models.IntegerField(null=True, blank=True)
    weight_2 = models.IntegerField(null=True, blank=True)
    answer_3 = models.IntegerField(null=True, blank=True)
    weight_3 = models.IntegerField(null=True, blank=True)
    answer_4 = models.IntegerField(null=True, blank=True)
    weight_4 = models.IntegerField(null=True, blank=True)
    answer_5 = models.IntegerField(null=True, blank=True)
    weight_5 = models.IntegerField(null=True, blank=True)
    answer_6 = models.IntegerField(null=True, blank=True)
    weight_6 = models.IntegerField(null=True, blank=True)
    answer_7 = models.IntegerField(null=True, blank=True)
    weight_7 = models.IntegerField(null=True, blank=True)
    answer_8 = models.IntegerField(null=True, blank=True)
    weight_8 = models.IntegerField(null=True, blank=True)
    answer_9 = models.IntegerField(null=True, blank=True)
    weight_9 = models.IntegerField(null=True, blank=True)
    answer_10 = models.IntegerField(null=True, blank=True)
    weight_10 = models.IntegerField(null=True, blank=True)
    answer_11 = models.IntegerField(null=True, blank=True)
    weight_11 = models.IntegerField(null=True, blank=True)
    answer_12 = models.IntegerField(null=True, blank=True)
    weight_12 = models.IntegerField(null=True, blank=True)
    answer_13 = models.IntegerField(null=True, blank=True)
    weight_13 = models.IntegerField(null=True, blank=True)
    answer_14 = models.IntegerField(null=True, blank=True)
    weight_14 = models.IntegerField(null=True, blank=True)
    answer_15 = models.IntegerField(null=True, blank=True)
    weight_15 = models.IntegerField(null=True, blank=True)
    answer_16 = models.IntegerField(null=True, blank=True)
    weight_16 = models.IntegerField(null=True, blank=True)
    answer_17 = models.IntegerField(null=True, blank=True)
    weight_17 = models.IntegerField(null=True, blank=True)
    answer_18 = models.IntegerField(null=True, blank=True)
    weight_18 = models.IntegerField(null=True, blank=True)
    answer_19 = models.IntegerField(null=True, blank=True)
    weight_19 = models.IntegerField(null=True, blank=True)
    answer_20 = models.IntegerField(null=True, blank=True)
    weight_20 = models.IntegerField(null=True, blank=True)
    answer_21 = models.IntegerField(null=True, blank=True)
    weight_21 = models.IntegerField(null=True, blank=True)
    answer_22 = models.IntegerField(null=True, blank=True)
    weight_22 = models.IntegerField(null=True, blank=True)
    answer_23 = models.IntegerField(null=True, blank=True)
    weight_23 = models.IntegerField(null=True, blank=True)
    answer_24 = models.IntegerField(null=True, blank=True)
    weight_24 = models.IntegerField(null=True, blank=True)
    answer_25 = models.IntegerField(null=True, blank=True)
    weight_25 = models.IntegerField(null=True, blank=True)
    answer_26 = models.IntegerField(null=True, blank=True)
    weight_26 = models.IntegerField(null=True, blank=True)
    answer_27 = models.IntegerField(null=True, blank=True)
    weight_27 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'User_Answers'

class Users(models.Model):
    inner_id = models.BigIntegerField(primary_key=True, db_column='Inner_id') # Field name made lowercase.
    user_id = models.BigIntegerField(null=True, db_column='User_id', blank=True) # Field name made lowercase.
    age_group = models.IntegerField(null=True, db_column='Age_group', blank=True) # Field name made lowercase.
    sex = models.CharField(max_length=3, db_column='Sex', blank=True) # Field name made lowercase.
    area_id = models.IntegerField(null=True, db_column='Area_id', blank=True) # Field name made lowercase.
    election_year = models.IntegerField(null=True, db_column='Election_year', blank=True) # Field name made lowercase.
    winnercandidate = models.IntegerField(null=True, db_column='winnerCandidate', blank=True) # Field name made lowercase.
    winnerparty = models.CharField(max_length=150, db_column='winnerParty', blank=True) # Field name made lowercase.
    answers = models.TextField(db_column='Answers', blank=True) # Field name made lowercase.
    candidateslist = models.TextField(db_column='CandidatesList', blank=True) # Field name made lowercase.
    partieslist = models.TextField(db_column='PartiesList', blank=True) # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    modified = models.DateTimeField(null=True, db_column='Modified', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Users'

class Workingsectortypes(models.Model):
    type_id = models.IntegerField(primary_key=True, db_column='Type_id') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'WorkingSectorTypes'

