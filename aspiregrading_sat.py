#SAT GRADER

def compiler(answerkey, answers, rawScore_conversion):
	"""
	>>> answerkey = {1: {"sectiontype": "Essay", "score": None}, 2: {"sectiontype": "Math", 1: "A", 2: "B", 3: "C", 4: "D"}}
	>>> answerkey[3] = {"sectiontype": "Math FRQ", 1: "A", 2: "C", 3: 10, 4: 12, 5: 12, 6: 12, 7: 12, 8: 12, 9: 23, 10: 23, 11: 12, 12: 12}
	>>> answerkey[4] = {"sectiontype": "English", 1: "A", 2: "B", 3: "D", 4: "C"}
	>>> answerkey[5] = {"sectiontype": "Reading", 1: "A", 2: "B", 3: "C", 4: "D"}
	>>> rawscoreconversion = {'Math': {range(5,17): 800}, 'Writing': {range(2,5): {7: 800}}, 'Reading': {range(2,5): 800}}
	>>> answers = {1: {"sectiontype": "Essay", "score": 7}, 2: {"sectiontype": "Math", 1: "A", 2: "A", 3: "C", 4: "D"}}
	>>> answers[3] = {"sectiontype": "Math FRQ", 1: "A", 2: "C", 3: 10, 4: 13, 5: 12, 6: 12, 7: 12, 8: 12, 9: 23, 10: 23, 11: 12, 12: 12}
	>>> answers[4] = {"sectiontype": "English", 1: "A", 2: "B", 3: "D", 4: "C"}
	>>> answers[5] = {"sectiontype": "Reading", 1: "A", 2: "B", 3: "C", 4: "D"}
	>>> x, y = compiler(answerkey, answers, rawscoreconversion)
	>>> x
	>>> y
	"""

	math_total = 0
	english_total = 0
	reading_total = 0
	wrong_answers = {}
	essay_score = 0
	for section in answerkey:
		if answerkey[section]['sectiontype'] != 'Essay':
			wrong_answers[section] = Wrong_answers(answerkey[section], answers[section])
		else:
			essay_score = answers[section]['score']
	wrong_answers['Essay'] = essay_score
	for section in wrong_answers:
		if section != "Essay":
			if wrong_answers[section]['sectiontype'] == "Math FRQ":
				math_total += rawscorefinder(wrong_answers[section], answerkey[section], True)
			elif wrong_answers[section]['sectiontype'] == "Math":
				math_total += rawscorefinder(wrong_answers[section], answerkey[section])
			elif wrong_answers[section]['sectiontype'] == "English":
				english_total += rawscorefinder(wrong_answers[section], answerkey[section])
			elif wrong_answers[section]['sectiontype'] == "Reading":
				reading_total += rawscorefinder(wrong_answers[section], answerkey[section])
	for total in (math_total, english_total, reading_total):
		if total % 1 >= .5:
			total = total // 1 + 1
		elif total % 1 < .5:
			total = total // 1 
	final_math = 0
	final_english = 0
	final_reading = 0
	for rangelst in rawScore_conversion['Math']:
		if math_total >= rangelst[0] and math_total <= rangelst[len(rangelst) - 1]:
			final_math = rawScore_conversion['Math'][rangelst]
	for rangelst in rawScore_conversion['Reading']:
		if reading_total >= rangelst[0] and reading_total <= rangelst[len(rangelst) - 1]:
			final_reading = rawScore_conversion['Reading'][rangelst]
	for rangelst in rawScore_conversion['Writing']:
		if english_total >= rangelst[0] and english_total <= rangelst[len(rangelst) - 1]:
			final_english = rawScore_conversion['Writing'][rangelst][essay_score]
	final_scores = {'total': (final_math + final_reading + final_english), 'Writing': final_english, 'Math': final_math, 'Reading': final_reading}
	return final_scores, wrong_answers



def Wrong_answers(answerkey, answers):
	"""
	>>> answerkey = {"sectiontype": "Math"}
	>>> answerkey[1] = "A"
	>>> answerkey[2] = "B"
	>>> answerkey[3] = "C"
	>>> answerkey[4] = "D"
	>>> answers = {1: "B"}
	>>> answers[2] = "B"
	>>> answers[3] = "D"
	>>> answers[4] = "D"
	>>> Wrong_answers(answerkey, answers)
	{1: 'B', 3: 'D', 'sectiontype': 'Math'}
	"""
	question_number = 1
	wrong_answers = {}
	wrong_answers['sectiontype'] = answerkey['sectiontype']
	while question_number < len(answerkey):
		if answers[question_number] == answerkey[question_number]:
			question_number += 1
		else:
			wrong_answers[question_number] = answers[question_number]
			question_number += 1
	return wrong_answers

def rawscorefinder(wrong_answers, answerkey, frq = False, penalty = 0.25):
	"""
	>>> answerkey = {"sectiontype": "Math"}
	>>> answerkey[1] = "A"
	>>> answerkey[2] = "B"
	>>> answerkey[3] = "C"
	>>> answerkey[4] = "D"
	>>> answers = {1: "B"}
	>>> answers[2] = "B"
	>>> answers[3] = "D"
	>>> answers[4] = "D"
	>>> w = Wrong_answers(answerkey, answers)
	>>> rawscorefinder(w, answerkey)
	1.5

	"""
	total = len(answerkey) - 1
	if frq:
		frq_start = len(answerkey) - 9 - 1
		frq_wrongs = {}
		reg_wrongs = {}
		for key in wrong_answers:
			if type(key) == int and key > frq_start:
				frq_wrongs[key] = wrong_answers[key]
			elif type(key) == int:
				reg_wrongs[key] = wrong_answers[key]
		regwrong = len(reg_wrongs)
		frqwrong = len(frq_wrongs)
		total = total - regwrong - (penalty * regwrong) - frqwrong
		return total
	else:
		wrong = len(wrong_answers) - 1
		total = total - wrong - (penalty * wrong)
		return total


	

