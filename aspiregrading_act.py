#ACT GRADER
default_conversion = {'English': {(75,): 36, (74,): 35, (72,73): 34, (71,): 33, (70,): 31, (68,69): 30, (67,): 29, (65,66): 28, (64,): 27, (62, 63): 26, (60, 61): 25, (58,59): 24, (55,57): 23, (53,54): 22, (50,52): 21, (46, 49): 20, (43, 45): 19, (41, 42): 18, (39, 40): 17, (36, 38): 16, (33, 35): 15, (31, 32): 14, (28, 30): 13, (26,27): 12, (24, 25): 11, (21, 23): 10, (19, 20): 9, (16, 18): 8, (13, 15): 7, (10, 12): 6, (8,9): 5, (6,7): 4, (4,5): 3, (3,): 2, (0, 2): 1}}
default_conversion['Math'] = {(75,): 36, (74,): 35, (72,73): 34, (71,): 33, (70,): 31, (68,69): 30, (67,): 29, (65,66): 28, (64,): 27, (62, 63): 26, (60, 61): 25, (58,59): 24, (55,57): 23, (53,54): 22, (50,52): 21, (46, 49): 20, (43, 45): 19, (41, 42): 18, (39, 40): 17, (36, 38): 16, (33, 35): 15, (31, 32): 14, (28, 30): 13, (26,27): 12, (24, 25): 11, (21, 23): 10, (19, 20): 9, (16, 18): 8, (13, 15): 7, (10, 12): 6, (8,9): 5, (6,7): 4, (4,5): 3, (3,): 2, (0, 2): 1}
default_conversion['Science'] = {(75,): 36, (74,): 35, (72,73): 34, (71,): 33, (70,): 31, (68,69): 30, (67,): 29, (65,66): 28, (64,): 27, (62, 63): 26, (60, 61): 25, (58,59): 24, (55,57): 23, (53,54): 22, (50,52): 21, (46, 49): 20, (43, 45): 19, (41, 42): 18, (39, 40): 17, (36, 38): 16, (33, 35): 15, (31, 32): 14, (28, 30): 13, (26,27): 12, (24, 25): 11, (21, 23): 10, (19, 20): 9, (16, 18): 8, (13, 15): 7, (10, 12): 6, (8,9): 5, (6,7): 4, (4,5): 3, (3,): 2, (0, 2): 1}
default_conversion['Reading'] = {(75,): 36, (74,): 35, (72,73): 34, (71,): 33, (70,): 31, (68,69): 30, (67,): 29, (65,66): 28, (64,): 27, (62, 63): 26, (60, 61): 25, (58,59): 24, (55,57): 23, (53,54): 22, (50,52): 21, (46, 49): 20, (43, 45): 19, (41, 42): 18, (39, 40): 17, (36, 38): 16, (33, 35): 15, (31, 32): 14, (28, 30): 13, (26,27): 12, (24, 25): 11, (21, 23): 10, (19, 20): 9, (16, 18): 8, (13, 15): 7, (10, 12): 6, (8,9): 5, (6,7): 4, (4,5): 3, (3,): 2, (0, 2): 1}



def compiler(answerkey, answers, rawScore_conversion = default_conversion):
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
	>>> x, y = compiler(answerkey, answers, rawscoreconversion)
	>>> x
	>>> y
	"""

	math_total = 0
	english_total = 0
	reading_total = 0
	science_total = 0
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
			if wrong_answers[section]['sectiontype'] == "Science":
				science_total += rawscorefinder(wrong_answers[section], answerkey[section])
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
	final_science = 0
	for rangelst in rawScore_conversion['Science']:
		if science_total >= rangelst[0] and science_total <= rangelst[len(rangelst) - 1]:
			final_science = rawScore_conversion['Science'][rangelst] 
	for rangelst in rawScore_conversion['Math']:
		if math_total >= rangelst[0] and math_total <= rangelst[len(rangelst) - 1]:
			final_math = rawScore_conversion['Math'][rangelst]
	for rangelst in rawScore_conversion['Reading']:
		if reading_total >= rangelst[0] and reading_total <= rangelst[len(rangelst) - 1]:
			final_reading = rawScore_conversion['Reading'][rangelst]
	for rangelst in rawScore_conversion['Writing']:
		if english_total >= rangelst[0] and english_total <= rangelst[len(rangelst) - 1]:
			final_english = rawScore_conversion['Writing'][rangelst]	
	rounded = (final_math + final_reading + final_english + final_science) / 4
	if rounded % 1 >= .5:
		rounded = rounded // 1 + 1
	elif rounded % 1 < .5:
		rounded = rounded // 1
	final_scores = {'total': rounded, 'Writing': final_english, 'Math': final_math, 'Reading': final_reading, 'Science': final_science}
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

def rawscorefinder(wrong_answers, answerkey, frq = False, penalty = 0):
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
	2

	"""
	total = len(answerkey) - 1
	wrong = len(wrong_answers) - 1
	total = total - wrong - (penalty * wrong)
	return total


	

