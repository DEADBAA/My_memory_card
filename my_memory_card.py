import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QButtonGroup, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox


WIN_SIZE = (400, 300)
WIN_W, WIN_H = WIN_SIZE

class Question():
    def __init__(self, question, rbtn_1, rbtn_2, rbtn_3, rbtn_4, right_answer):
        self.question = question
        self.answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
        self.right_answer = right_answer
        random.shuffle(self.answers)

questions = [
    Question('Когда началась 2-ая ступень курса Python',
    '31.10', '01.11', '01.01.1970', '12.11',
    '12.11'),
    Question('Кто такой Зет?', 
    'Друг', 'Покойник', 'Враг', 'Владелец Чоппера', 
    'Покойник'),
    Question('Cамая популярная на момент 90-ых годов рок группа',
    'Nirvana', 'Blur', 'КиШ', 'Korn',
    'Nirvana'),
    Question('Как называется человек разрабатывающий рекламу',
    'Юрист-консультант', 'Маркетолог', 'Пиар-Менеджер', 'Рекламщик',
    'Маркетолог'),
    Question('В чем смысл жизни?',
    '42', 'В жизни', 'В эволюции', 'Его нет',
    '42')
]

questions_nums = list(range(len(questions)))
score = 0

def ask_question():
        rand_idx = random.randint(0, len(questions_nums) - 1)
        rand_question_idx = questions_nums.pop(rand_idx)
        rand_question = questions[rand_question_idx]
        random.shuffle(rand_question.answers)
        quest_label.setText(rand_question.question)
        rbtn_1.setText(rand_question.answers[0])
        rbtn_2.setText(rand_question.answers[1])
        rbtn_3.setText(rand_question.answers[2])
        rbtn_4.setText(rand_question.answers[3])
        right_answ_label.setText(rand_question.right_answer)
def show_question():
    group_question.show()
    group_answer.hide()
    answer.setText('Ответить')

def show_result():
    group_question.hide()
    checked_button = RadioGroup.checkedButton()
    if checked_button.text() == right_answ_label.text():
        answ_text_label.setText('Верно!')
        global score
        score += 1
        score_label.setText(f'Счёт: {str(score)}')
        score_procent_label.setText(f'Рейтинг: {str(score / len(questions)*100)} %')
    else:
        answ_text_label.setText('Ошибка!')
    
        
    user_answer_label.setText(checked_button.text())
    right_answ_label.setText('Правильный ответ: ' + right_answ_label.text())
    group_answer.show()
    answer.setText('Следующий вопрос')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def button_clicked():
    if answer.text() == 'Ответить':
        show_result()
    elif answer.text() == 'Следующий вопрос' and len(questions_nums) > 0:
        ask_question()
        show_question()
    elif answer.text() == 'Перейти к результатам':
        pass
    elif answer.text() == 'Завершить тест':
        main_window.close()

    
app = QApplication([])
main_window = QWidget()
main_window.resize(WIN_W, WIN_H)
main_window.setWindowTitle('Memo Card')


V_main_line = QVBoxLayout()
top_H_line = QHBoxLayout()
middle_H_line = QHBoxLayout()
bottom_H_line = QHBoxLayout()
result_H_line = QHBoxLayout()

answ_box_V_line = QVBoxLayout()
answ_H_line_1 = QHBoxLayout()
answ_H_line_2 = QHBoxLayout()

res_box_V_line = QVBoxLayout()

quest_label = QLabel('Question')
top_H_line.addWidget(quest_label, alignment = Qt.AlignCenter)

group_question = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1, 1)
RadioGroup.addButton(rbtn_2, 2)
RadioGroup.addButton(rbtn_3, 3)
RadioGroup.addButton(rbtn_4, 4)


answ_H_line_1.addWidget(rbtn_1, alignment = Qt.AlignCenter)
answ_H_line_1.addWidget(rbtn_2, alignment = Qt.AlignCenter)
answ_H_line_2.addWidget(rbtn_3, alignment = Qt.AlignCenter)
answ_H_line_2.addWidget(rbtn_4, alignment = Qt.AlignCenter)
answ_box_V_line.addLayout(answ_H_line_1)
answ_box_V_line.addLayout(answ_H_line_2)
group_question.setLayout(answ_box_V_line)
middle_H_line.addWidget(group_question)

group_answer = QGroupBox('Результат теста')
answ_text_label = QLabel('Правильно/Неправильно')
right_answ_label = QLabel('какой ответ правильный')
user_answer_label = QLabel('Ответ пользователя')
score_text = str(score)
score_procent_text = str(score//len(questions)*100)
score_label = QLabel('Счёт:'+score_text)
score_procent_label = QLabel('Рейтинг: ' + score_procent_text + '%')
res_box_V_line.addWidget(answ_text_label, alignment = Qt.AlignLeft)
res_box_V_line.addWidget(right_answ_label, alignment = Qt.AlignCenter)
res_box_V_line.addWidget(user_answer_label, alignment = Qt.AlignCenter)
group_answer.setLayout(res_box_V_line)
middle_H_line.addWidget(group_answer, alignment = Qt.AlignVCenter, stretch = 2)
group_answer.hide()

answer = QPushButton('Ответить')
bottom_H_line.addWidget(answer)

result_H_line.addWidget(score_label, alignment = Qt.AlignLeft)
result_H_line.addWidget(score_procent_label, alignment = Qt.AlignRight)

V_main_line.addLayout(top_H_line)
V_main_line.addStretch(1)
V_main_line.addLayout(middle_H_line, stretch = 3)
V_main_line.addStretch(1)
V_main_line.addLayout(bottom_H_line)
V_main_line.addStretch(1)
V_main_line.addLayout(result_H_line)


main_window.setLayout(V_main_line)

ask_question()

answer.clicked.connect(button_clicked)

main_window.show()
app.exec_()