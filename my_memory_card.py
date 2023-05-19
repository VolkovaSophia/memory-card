#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self, question_text, answer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

'''wrong1 = 'Энцы'
wrong2 = 'Чулымцы'
wrong3 = 'Алеуты'
answer = 'Смурфы'
question_text = 'Какой национальности не существует?'''

q1 = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')
q2 = Question('Это вопрос?', 'Да', 'Нет', 'Может быть', 'Я не знаю')
q3 = Question('Какой город является столицей Австралии?', 'Канберра', 'Сидней', 'Мельбурн', 'Аделаида')

questions = [q1, q2, q3]

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(500, 400)

question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Чулымцы')
ans3 = QRadioButton('Смурфы')
ans4 = QRadioButton('Алеуты')
answers = [ans1, ans2, ans3, ans4]

layout1 = QHBoxLayout()
layout1.addWidget(question, alignment=Qt.AlignCenter)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line1.addWidget(ans1, alignment=Qt.AlignCenter)
line1.addWidget(ans2, alignment=Qt.AlignCenter)
line2.addWidget(ans3, alignment=Qt.AlignCenter)
line2.addWidget(ans4, alignment=Qt.AlignCenter)
layout2 = QVBoxLayout()
layout2.addLayout(line1)
layout2.addLayout(line2)

result = QLabel('Верно/Неверно')
right_answer = QLabel('right answer will be here')
layout4 = QVBoxLayout()
layout4.addWidget(result, alignment=Qt.AlignLeft)
layout4.addWidget(right_answer, alignment=Qt.AlignCenter)
ans_group = QGroupBox('Результат теста')
ans_group.setLayout(layout4)

layout3 = QHBoxLayout()
layout3.addWidget(button, alignment=Qt.AlignCenter)

group = QGroupBox('Варианты ответов')
group.setLayout(layout2)

main_layout = QVBoxLayout()
main_layout.addLayout(layout1)
main_layout.addWidget(group)
main_layout.addWidget(ans_group)
main_layout.addLayout(layout3)
window.setLayout(main_layout)

button_group = QButtonGroup()
button_group.addButton(ans1)
button_group.addButton(ans2)
button_group.addButton(ans3)
button_group.addButton(ans4)

def check_false():
    button_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    button_group.setExclusive(True)


def show_result():
    group.hide()
    ans_group.show()
    button.setText('Следующий вопрос')
    check_answer()
    check_false()
    print('Статистика\n'
    'Всего вопросов:', len(questions), '\n'
    'Правильных ответов:', window.right_answers_counter, '\n'
    'Рейтинг:', (window.right_answers_counter/len(questions))*100, '%')

def show_question():
    ans_group.hide()
    group.show()
    button.setText('Ответить')
    next_question() #check this if problems occure

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    question.setText(q.question_text)
    answers[0].setText(q.answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    result.setText('Неверно')
    if answers[0].isChecked():
        result.setText('Верно')
        window.right_answers_counter += 1
    right_answer.setText(answers[0].text())

def next_question():
    ask(questions[window.count])
    window.count += 1
    if window.count > len(questions)-1:
        window.count = 0
        group.hide()
        #ans_group.hide()
        question.setText('Конец теста')
        button.setText('Пройти тест сначала')
        window.right_answers_counter = 0

window.count = -1
window.right_answers_counter = 0

shuffle(questions)
show_question()
ans_group.hide()

button.clicked.connect(start_test)

window.show()
app.exec_()