def classCompiler(scorelist, answerlist, answerkey):
	statsdict = Hash[]
	questionStats = Hash[]
	
	for section in answerkey.keys
		questionStats[section] = Hash[]
		question_answers = Hash[]
		for student in answerlist.keys
			temp_dict = student[section]
			for question in temp_dict.keys
				if question != 'sectiontype'
					if question_answers.has_key?(question)
						question_answers[question] += [temp_dict[question]]
					else:
						question_answers[question] = [temp_dict[question]]
					end
				end
			end
		end

		for question in question_answers
			questionStats[section][question] = questionstats(question_answers[question], answerkey[section][question])
		end

	statsdict = average_score(scorelist)


	return statsdict, questionStats
end



def average_score(scorelist):
	writing_total = []
	reading_total = []
	math_total = []
	science_total = []
	total = []

	for student in scorelist
		writing_total += [student['Writing']]
		reading_total += [student['Reading']]
		math_total += [student['Math']]
		science_total += [student['Science']]
		total += [student['total']]
	end

	score_stats = Hash[]
	score_stats['Writing'] = stats(writing_total)[0]
	score_stats['Math'] = stats(math_total)[0]
	score_stats['Reading'] = stats(reading_total)[0]
	score_stats['Science'] = stats(science_total)[0]
	score_stats['total'] = stats(total)
	return score_stats
end



def stats(lst)
	count = 0
	total = 0
	
	for item in lst
		total += item
		count += 1
	end

	average = total.to_f / count
	devtotal = 0

	for item in lst
		devtotal += (item - average) ** 2
	end

	return average, ((devtotal / count) ** (1/2))
end



def questionstats(answerlist, correct):
	totalright = 0

	for answer in answerlist
		if answer == correct
			totalright += 1
		end
	end

	percent_wrong = ((1 - totalright.to_f / answerlist.length) * 100) // 1

	answer_counts = Hash[]

	for answer in answerlist
		if answer_counts.keys.has_key?(answer)
			answer_counts[answer] += 1
		else
			answer_counts[answer] = 1
		end
	end

	for answer in answer_counts.keys
		answer_counts[answer] = ((answer_counts[answer].to_f / answerlist.length) * 100) // 1
	end

	answer_counts['Percent incorrect'] = percent_wrong


	return answer_counts
end
