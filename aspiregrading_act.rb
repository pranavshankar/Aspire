def compiler(answerkey, answers, rawScore_conversion = default_conversion)
	
	math_total = 0
	english_total = 0
	reading_total = 0
	science_total = 0
	wrong_answers = Hash[]
	essay_score = 0
	for section in answerkey.keys
		wrong_answers[section] = Wrong_answers(answerkey[section], answers[section])
	end

	for section in wrong_answers.keys
		if wrong_answers[section]['sectiontype'] == "Science"
			science_total += rawscorefinder(wrong_answers[section], answerkey[section])
		elsif wrong_answers[section]['sectiontype'] == "Math"
			math_total += rawscorefinder(wrong_answers[section], answerkey[section])
		elsif wrong_answers[section]['sectiontype'] == "English"
			english_total += rawscorefinder(wrong_answers[section], answerkey[section])
		elsif wrong_answers[section]['sectiontype'] == "Reading"
			reading_total += rawscorefinder(wrong_answers[section], answerkey[section])
		end
	end

	final_math = 0
	final_english = 0
	final_reading = 0
	final_science = 0
	
	for rangelst in rawScore_conversion['Science'].keys
		if science_total >= rangelst[0] && science_total <= rangelst[len(rangelst) - 1]
			final_science = rawScore_conversion['Science'][rangelst] 
		end
	end

	for rangelst in rawScore_conversion['Math'].keys
		if math_total >= rangelst[0] && math_total <= rangelst[ranglst.length - 1]:
			final_math = rawScore_conversion['Math'][rangelst]
		end
	end

	for rangelst in rawScore_conversion['Reading'].keys
		if reading_total >= rangelst[0] && reading_total <= rangelst[ranglst.length - 1]:
			final_reading = rawScore_conversion['Reading'][rangelst]
		end
	end

	for rangelst in rawScore_conversion['Writing'].keys
		if english_total >= rangelst[0] && english_total <= rangelst[ranglst.length - 1]:
			final_english = rawScore_conversion['Writing'][rangelst]	
		end
	end

	rounded = final_math + final_reading + final_english + final_science
	
	if rounded % 4 >= 2
		rounded = (round / 4) + 1
	else
		rounded = round / 4
	end

	final_scores = [['total', rounded], ['Writing', final_english], ['Math', final_math], ['Reading', final_reading], ['Science', final_science]]
	
	return final_scores, wrong_answers
end

def Wrong_answers(answerkey, answers)
	question_number = 1
	wrong_answers = Hash[]
	wrong_answers['sectiontype'] = answerkey['sectiontype']
	while question_number < answerkey.length do
		if answers[question_number] == answerkey[question_number]
			question_number += 1
		else
			wrong_answers[question_number] = answers[question_number]
			question_number += 1
		end
	end
	return wrong_answers
end




def rawscorefinder(wrong_answers, answerkey)
	wrong = wrong_answers.length
	total = answerkey.length
	total = total - wrong
	return total
end


