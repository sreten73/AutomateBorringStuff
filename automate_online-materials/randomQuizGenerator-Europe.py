import random

# The quiz data. Keys are states and values are their capitals.
europe_capitals = {
    "Albania": "Tirana", "Andorra": "Andorra la Vella", "Austria": "Vienna", "Belarus": "Minsk",
    "Belgium": "Brussels", "Bosnia and Herzegovina": "Sarajevo", "Bulgaria": "Sofia", "Croatia": "Zagreb",
    "Cyprus": "Nicosia", "Czech Republic": "Prague", "Denmark": "Copenhagen", "Estonia": "Tallinn",
    "Finland": "Helsinki", "France": "Paris", "Germany": "Berlin", "Greece": "Athens",
    "Hungary": "Budapest", "Iceland": "Reykjavik", "Ireland": "Dublin", "Italy": "Rome",
    "Latvia": "Riga", "Liechtenstein": "Vaduz", "Lithuania": "Vilnius", "Luxembourg": "Luxembourg City",
    "Malta": "Valletta", "Moldova": "Chisinau", "Monaco": "Monaco", "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam", "North Macedonia": "Skopje", "Norway": "Oslo", "Poland": "Warsaw",
    "Portugal": "Lisbon", "Romania": "Bucharest", "Russia": "Moscow", "San Marino": "San Marino",
    "Serbia": "Belgrade", "Slovakia": "Bratislava", "Slovenia": "Ljubljana", "Spain": "Madrid",
    "Sweden": "Stockholm", "Switzerland": "Bern", "Ukraine": "Kyiv", "United Kingdom": "London", "Vatican City": "Vatican City"
}


for quizNum in range(5):
    # Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{(quizNum+1)}.txt','w')
    answerKeyFile = open(f'capitalsquiz_answers{(quizNum + 1)}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20)+f'Europe State Capitals Quiz (Form {(quizNum+1)})')
    quizFile.write('\n\n')

    # Shufle the order of the states.
    states = list(europe_capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(45):
        # Get right and wrong answers.
        correctAnswer = europe_capitals[states[questionNum]]
        wrongAnswers = list(europe_capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{(questionNum+1)}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()



