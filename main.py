#! python3
# main.py - Створює екзаменаційні білети з питаннями та відповідями, які розташовуються в випадковому порядку, разом із ключами відповідей

import random

# Данні білета. Ключі - назва штатів, а значення - столиці.
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Генерація 35 файлів білетів
for quizNum in range(35):
    # Створення файлів білетів та ключей відповідей.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w', encoding='utf-8')
    answersKeys = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w', encoding='utf-8')

    # Запис заголовка білету.
    quizFile.write("Ім'я: \n\nДата: \n\nКурс: \n\n")
    quizFile.write(' ' * 15 + f'Перевірка знань столиць США (Білет №{quizNum + 1})\n\n')
    quizFile.write('\n\n')

    # Перемішування порядку послідовності столиць штатів
    states = list(capitals.keys())
    random.shuffle(states)

    # Організація циклу по всім 50 штатам із створенням питання для кожного з них
    for questionNum in range(50):

        # Отримання правильних і неправильних відповідей 
        correctAnswers = capitals[states[questionNum]] 
        wrongAnswers = list(capitals.values())

        del wrongAnswers[wrongAnswers.index(correctAnswers)]

        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]

        random.shuffle(answerOptions)

        # Запис варіантів питань та відповідей у файл білету
        quizFile.write(f'{questionNum + 1}. Яка столиця штату {states[questionNum]}?\n')

        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

        # Запис ключа відповіді в файл
        correctLetter = 'ABCD'[answerOptions.index(correctAnswers)]

        answersKeys.write(f'{questionNum + 1}. {correctLetter}\n')
        
    quizFile.close()
    answersKeys.close
