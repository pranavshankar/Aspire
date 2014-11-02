# inputs:
# 	list of student scores
# 	list of students missed questions
# 	list of answer key


# outputs: 
# 	average score of the class 
# 	standard dev of class 
# 	missed questions data:	
# 			Each question: % got right, Answer popularity by percent
# 			Essays: Average essay score, standard dev of essay scores

###FOR ACT SCORES###
from aspiregrading_act import compiler, Wrong_answers, rawscorefinder

def classCompiler(scorelist, answerlist, answerkey):
	"""
	>>> answerkey = {1: {"sectiontype": "Essay", "score": None}, 2: {"sectiontype": "Math", 1: "A", 2: "B", 3: "C", 4: "D"}}
	>>> answerkey[3] = {"sectiontype": "Science", 1: "A", 2: "C", 3: "D", 4: "A"}
	>>> answerkey[4] = {"sectiontype": "English", 1: "A", 2: "B", 3: "D", 4: "C"}
	>>> answerkey[5] = {"sectiontype": "Reading", 1: "A", 2: "B", 3: "C", 4: "D"}
	>>> rawscoreconversion = {'Math': {range(2,5): 33}, 'Writing': {range(2,5): 36}, 'Reading': {range(2,5): 36}, 'Science': {range(2,5): 36}}
	>>> answers = {1: {"sectiontype": "Essay", "score": None}, 2: {"sectiontype": "Math", 1: "A", 2: "B", 3: "C", 4: "D"}}
	>>> answers[3] = {"sectiontype": "Science", 1: "A", 2: "C", 3: "D", 4: "A"}
	>>> answers[4] = {"sectiontype": "English", 1: "A", 2: "D", 3: "D", 4: "C"}
	>>> answers[5] = {"sectiontype": "Reading", 1: "A", 2: "B", 3: "C", 4: "D"}
	>>> answers1 = {1: {"sectiontype": "Essay", "score": None}, 2: {"sectiontype": "Math", 1: "A", 2: "B", 3: "C", 4: "D"}}
	>>> answers1[3] = {"sectiontype": "Science", 1: "A", 2: "A", 3: "D", 4: "A"}
	>>> answers1[4] = {"sectiontype": "English", 1: "A", 2: "B", 3: "A", 4: "C"}
	>>> answers1[5] = {"sectiontype": "Reading", 1: "A", 2: "B", 3: "C", 4: "D"}
	>>> x, y = compiler(answerkey, answers, rawscoreconversion)
	>>> x1, y1 = compiler(answerkey, answers, rawscoreconversion)
	>>> x2, y2 = compiler(answerkey, answers1, rawscoreconversion)
	>>> scorelist = [x1, x2]
	>>> answerlist = [answers, answers1]
	>>> x, y = classCompiler(scorelist, answerlist, answerkey)
	>>> x
	>>> y
	"""
	statsdict = {}
	questionStats = {}
	essay_score_lst = []
	
	for section in answerkey:
		if answerkey[section]['sectiontype'] != 'Essay':
			questionStats[section] = {}
			question_answers = {}
			for student in answerlist:
				temp_dict = student[section]
				for question in temp_dict:
					if question != 'sectiontype':
						if question in question_answers:
							question_answers[question] += [temp_dict[question]]
						else:
							question_answers[question] = [temp_dict[question]]
			for question in question_answers:
				questionStats[section][question] = questionstats(question_answers[question], answerkey[section][question])
		else:
			for student in answerlist:
				essay_score_lst += [student[section]['score']]
	
	has_essay = True
	for essay in essay_score_lst:
		if essay == None:
			has_essay = False
	if has_essay and essay_score_lst:
		essay_average, useless = stats(essay_score_lst)
	else:
		essay_average = None

	statsdict = average_score(scorelist)
	statsdict['Essay Average'] = essay_average

	return statsdict, questionStats



def average_score(scorelist):
	writing_total = []
	reading_total = []
	math_total = []
	science_total = []
	total = []
	for student in scorelist:
		writing_total += [student['Writing']]
		reading_total += [student['Reading']]
		math_total += [student['Math']]
		science_total += [student['Science']]
		total += [student['total']]
	score_stats = {}
	score_stats['Writing'] = stats(writing_total)[0]
	score_stats['Math'] = stats(math_total)[0]
	score_stats['Reading'] = stats(reading_total)[0]
	score_stats['Science'] = stats(science_total)[0]
	score_stats['total'] = stats(total)
	return score_stats


def stats(lst):
	count = 0
	total = 0
	for item in lst:
		total += item
		count += 1
	average = total / count
	devtotal = 0
	for item in lst:
		devtotal += (item - average) ** 2
	return average, ((devtotal / count) ** (1/2))


def questionstats(answerlist, correct):
	totalright = 0
	for answer in answerlist:
		if answer == correct:
			totalright += 1
	percent_wrong = ((1 - totalright / len(answerlist)) * 100) // 1

	answer_counts = {}
	for answer in answerlist:
		if answer in answer_counts:
			answer_counts[answer] += 1
		else:
			answer_counts[answer] = 1
	for answer in answer_counts:
		answer_counts[answer] = ((answer_counts[answer] / len(answerlist)) * 100) // 1
	answer_counts['Percent incorrect'] = percent_wrong


	return answer_counts


