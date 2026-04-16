from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from models import db, User, Course, Module, Lesson, Quiz, Question, Assignment, Progress, Submission, Badge, UserBadge, Leaderboard
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    # Seed some data if empty
    if not Course.query.first():
        course = Course(title='Python Adventure: Learn Coding Like a Game!')
        db.session.add(course)
        db.session.commit()

        # Module 1: Introduction to Coding
        module1 = Module(course_id=course.id, title='Introduction to Coding', order=1)
        db.session.add(module1)
        db.session.commit()

        lesson1_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic 1: What is Coding?</h2>

            <div class="explanation-box">
                <h3>🧠 Simple Explanation</h3>
                <p class="big-text">Coding is like <strong>giving instructions to a robot</strong> 🤖</p>
                <p>If you say: "Clap hands" → Robot claps 👏</p>
                <p>Computer also listens like that!</p>
            </div>

            <div class="example-box">
                <h3>🌍 Real-Life Example</h3>
                <p>Giving instructions to your friend:</p>
                <p>"Bring water → Open bottle → Drink"</p>
            </div>

            <div class="fun-box">
                <h3>😂 Funny Example</h3>
                <p>If you say: "Eat 100 chocolates" 🍫</p>
                <p>Computer will say: "Okay boss 😎" (no health worries!)</p>
            </div>

            <div class="code-box">
                <h3>💻 Try This Code</h3>
                <pre><code>print("Hello, I am your robot friend!")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Your Turn!</h3>
                <p>Make the computer say your name + favorite food</p>
                <p><strong>Hint:</strong> Use print() and + to join words</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic 2: What is Python?</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Python is a <strong>friendly language</strong> to talk to computers 🐍</p>
            </div>

            <div class="example-box">
                <h3>🌍 Real-Life</h3>
                <p>Like English for humans, Python for computers</p>
            </div>

            <div class="fun-box">
                <h3>😂 Funny</h3>
                <p>Python is not snake here 😆 it won't bite!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>print("Python is fun!")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Print: "I love coding"</p>
            </div>
        </div>
        '''

        lesson1 = Lesson(module_id=module1.id, content=lesson1_content)
        quiz1 = Quiz(module_id=module1.id)
        db.session.add(lesson1)
        db.session.add(quiz1)
        db.session.commit()

        # Quiz questions for Module 1
        quiz1_questions = [
            Question(quiz_id=quiz1.id, question='Coding means:', options=json.dumps(['A) Drawing pictures', 'B) Giving instructions to computer', 'C) Playing games']), correct_answer='B'),
            Question(quiz_id=quiz1.id, question='Computer understands:', options=json.dumps(['A) Magic spells', 'B) Step-by-step instructions', 'C) Only English']), correct_answer='B'),
            Question(quiz_id=quiz1.id, question='What will this code print? print("Hi")', options=json.dumps(['A) Hello', 'B) Hi', 'C) Bye']), correct_answer='B'),
            Question(quiz_id=quiz1.id, question='True or False: Computer can think by itself', options=json.dumps(['A) True', 'B) False']), correct_answer='B'),
            Question(quiz_id=quiz1.id, question='What is coding used for?', options=json.dumps(['A) Only making games', 'B) Solving problems and creating things', 'C) Only drawing']), correct_answer='B'),
        ]
        db.session.add_all(quiz1_questions)

        # Module 2: Python Basics
        module2 = Module(course_id=course.id, title='Python Basics', order=2)
        db.session.add(module2)
        db.session.commit()

        lesson2_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: Variables</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Variable = <strong>box to store things</strong> 📦</p>
            </div>

            <div class="example-box">
                <h3>🌍 Real-Life</h3>
                <p>Your school bag holds books 🎒</p>
            </div>

            <div class="fun-box">
                <h3>😂 Funny</h3>
                <p>Don't put elephant in small box 🐘📦😂</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>name = "Kavya"
age = 10
print(name)
print(age)</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Store your name & age in variables and print them!</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: Data Types</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>Types of data:</p>
                <ul>
                    <li><strong>Number</strong> 🔢 (like 10, 25)</li>
                    <li><strong>Text</strong> 📝 (like "hello", "Kavya")</li>
                    <li><strong>Decimal</strong> 🍫 (like 3.5, 2.75)</li>
                </ul>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>x = 10          # Number
y = "Hello"     # Text
z = 3.5         # Decimal

print(x)
print(y)
print(z)</code></pre>
            </div>
        </div>
        '''

        lesson2 = Lesson(module_id=module2.id, content=lesson2_content)
        quiz2 = Quiz(module_id=module2.id)
        db.session.add(lesson2)
        db.session.add(quiz2)
        db.session.commit()

        # Quiz questions for Module 2
        quiz2_questions = [
            Question(quiz_id=quiz2.id, question='What is a variable?', options=json.dumps(['A) A type of snake', 'B) A box to store data', 'C) A math problem']), correct_answer='B'),
            Question(quiz_id=quiz2.id, question='Which is a text data type?', options=json.dumps(['A) 123', 'B) "hello"', 'C) 45.6']), correct_answer='B'),
            Question(quiz_id=quiz2.id, question='What does this code do? name = "Alex"', options=json.dumps(['A) Prints Alex', 'B) Stores "Alex" in name', 'C) Deletes Alex']), correct_answer='B'),
            Question(quiz_id=quiz2.id, question='Which is a number data type?', options=json.dumps(['A) "ten"', 'B) 10', 'C) ten']), correct_answer='B'),
            Question(quiz_id=quiz2.id, question='What will print(name) show if name = "Sam"?', options=json.dumps(['A) name', 'B) Sam', 'C) Nothing']), correct_answer='B'),
        ]
        db.session.add_all(quiz2_questions)

        # Module 3: User Input
        module3 = Module(course_id=course.id, title='User Input', order=3)
        db.session.add(module3)
        db.session.commit()

        lesson3_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: Getting Input from Users</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Computer asks → You answer 🗣️</p>
                <p>The computer can ask questions and wait for your answers!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>name = input("Enter your name: ")
print("Hello", name)
print("Nice to meet you! 😊")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Ask for user's favorite color and say "Nice choice!"</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: Numbers and Calculations</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>Computer can do math faster than you! ⚡</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("That's fast! 🚀")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Create a program that asks for two numbers and shows their multiplication!</p>
            </div>
        </div>
        '''

        lesson3 = Lesson(module_id=module3.id, content=lesson3_content)
        quiz3 = Quiz(module_id=module3.id)
        db.session.add(lesson3)
        db.session.add(quiz3)
        db.session.commit()

        # Quiz questions for Module 3
        quiz3_questions = [
            Question(quiz_id=quiz3.id, question='What does input() do?', options=json.dumps(['A) Shows output', 'B) Gets user input', 'C) Prints text']), correct_answer='B'),
            Question(quiz_id=quiz3.id, question='Why use int() with input for numbers?', options=json.dumps(['A) To make it bigger', 'B) To convert text to number', 'C) To make it smaller']), correct_answer='B'),
            Question(quiz_id=quiz3.id, question='What will this show? input("Age: ")', options=json.dumps(['A) Age: ', 'B) Waits for user to type age', 'C) Shows user age']), correct_answer='B'),
            Question(quiz_id=quiz3.id, question='What does a + b do if a=5, b=3?', options=json.dumps(['A) 53', 'B) 8', 'C) 15']), correct_answer='B'),
            Question(quiz_id=quiz3.id, question='True or False: input() always returns text', options=json.dumps(['A) True', 'B) False']), correct_answer='A'),
        ]
        db.session.add_all(quiz3_questions)

        # Module 4: Decision Making
        module4 = Module(course_id=course.id, title='Decision Making', order=4)
        db.session.add(module4)
        db.session.commit()

        lesson4_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: If-Else Statements</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Like making decisions in real life!</p>
                <p>"If raining → take umbrella ☔"</p>
                <p>"If sunny → wear sunglasses 🕶️"</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote! 🗳️")
    print("You are an adult! 👨‍💼")
else:
    print("Too young to vote 😊")
    print("Keep learning! 📚")

print("Thanks for telling your age!")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Ask for temperature and say if it's hot (>30°C) or cold (≤30°C)!</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: Comparisons</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>Comparison symbols:</p>
                <ul>
                    <li><strong>==</strong> → equal to (5 == 5 → True)</li>
                    <li><strong>></strong> → greater than (10 > 5 → True)</li>
                    <li><strong><</strong> → less than (3 < 8 → True)</li>
                    <li><strong>>=</strong> → greater or equal (5 >= 5 → True)</li>
                    <li><strong><=</strong> → less or equal (3 <= 5 → True)</li>
                    <li><strong>!=</strong> → not equal (5 != 3 → True)</li>
                </ul>
            </div>

            <div class="code-box">
                <h3>💻 Example</h3>
                <pre><code>score = 85

if score >= 90:
    print("Excellent! 🌟")
elif score >= 75:
    print("Good job! 👍")
else:
    print("Keep trying! 💪")</code></pre>
            </div>
        </div>
        '''

        lesson4 = Lesson(module_id=module4.id, content=lesson4_content)
        quiz4 = Quiz(module_id=module4.id)
        db.session.add(lesson4)
        db.session.add(quiz4)
        db.session.commit()

        # Quiz questions for Module 4
        quiz4_questions = [
            Question(quiz_id=quiz4.id, question='What does "if" check?', options=json.dumps(['A) Time', 'B) Conditions', 'C) Colors']), correct_answer='B'),
            Question(quiz_id=quiz4.id, question='What does else do?', options=json.dumps(['A) Stops program', 'B) Runs if condition is false', 'C) Repeats code']), correct_answer='B'),
            Question(quiz_id=quiz4.id, question='What does >= mean?', options=json.dumps(['A) Equal', 'B) Greater or equal', 'C) Less than']), correct_answer='B'),
            Question(quiz_id=quiz4.id, question='In if age > 10: what happens if age = 8?', options=json.dumps(['A) Code runs', 'B) Code skips to else', 'C) Error occurs']), correct_answer='B'),
            Question(quiz_id=quiz4.id, question='What is elif used for?', options=json.dumps(['A) End program', 'B) Check another condition', 'C) Print text']), correct_answer='B'),
        ]
        db.session.add_all(quiz4_questions)

        # Module 5: Loops
        module5 = Module(course_id=course.id, title='Loops', order=5)
        db.session.add(module5)
        db.session.commit()

        lesson5_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: For Loops</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Repeat actions again and again 🔁</p>
                <p>Like saying "Hello" to 5 friends without typing it 5 times!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>print("Counting to 5:")
for i in range(5):
    print(i + 1)

print("Done! ✅")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Print "I love coding!" 3 times using a loop</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: While Loops</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>Keep doing something WHILE a condition is true</p>
                <p>Like: "Keep eating cookies while cookies exist" 🍪</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>count = 1
while count <= 5:
    print("Count:", count)
    count = count + 1

print("Finished counting! 🎉")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Ask user to guess a number (1-10) until they get it right!</p>
            </div>
        </div>
        '''

        lesson5 = Lesson(module_id=module5.id, content=lesson5_content)
        quiz5 = Quiz(module_id=module5.id)
        db.session.add(lesson5)
        db.session.add(quiz5)
        db.session.commit()

        # Quiz questions for Module 5
        quiz5_questions = [
            Question(quiz_id=quiz5.id, question='What does a loop do?', options=json.dumps(['A) Stops program', 'B) Repeats code', 'C) Shows pictures']), correct_answer='B'),
            Question(quiz_id=quiz5.id, question='What is range(5)?', options=json.dumps(['A) Numbers 0-4', 'B) Numbers 1-5', 'C) Number 5']), correct_answer='A'),
            Question(quiz_id=quiz5.id, question='While loop runs:', options=json.dumps(['A) Fixed times', 'B) While condition is true', 'C) Never']), correct_answer='B'),
            Question(quiz_id=quiz5.id, question='In for i in range(3): what is i first?', options=json.dumps(['A) 1', 'B) 0', 'C) 3']), correct_answer='B'),
            Question(quiz_id=quiz5.id, question='How to stop infinite while loop?', options=json.dumps(['A) Use break', 'B) Change condition', 'C) Both A and B']), correct_answer='C'),
        ]
        db.session.add_all(quiz5_questions)

        # Module 6: Lists
        module6 = Module(course_id=course.id, title='Lists', order=6)
        db.session.add(module6)
        db.session.commit()

        lesson6_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: Lists</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">List = group of items in one box 🛒</p>
                <p>Like a shopping list or your toy collection!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>fruits = ["apple", "banana", "mango"]
print(fruits[0])  # First item
print(fruits[1])  # Second item
print(fruits[2])  # Third item

print("All fruits:", fruits)</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Create a list of your 3 favorite foods and print the second one!</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: List Operations</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>You can add, remove, and change items in lists!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>colors = ["red", "blue", "green"]

# Add item
colors.append("yellow")
print("After adding:", colors)

# Change item
colors[1] = "purple"
print("After changing:", colors)

# Remove item
colors.remove("red")
print("After removing:", colors)</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Create a list of games, add one more game, then remove the first game!</p>
            </div>
        </div>
        '''

        lesson6 = Lesson(module_id=module6.id, content=lesson6_content)
        quiz6 = Quiz(module_id=module6.id)
        db.session.add(lesson6)
        db.session.add(quiz6)
        db.session.commit()

        # Quiz questions for Module 6
        quiz6_questions = [
            Question(quiz_id=quiz6.id, question='What is a list?', options=json.dumps(['A) Single item', 'B) Group of items', 'C) A number']), correct_answer='B'),
            Question(quiz_id=quiz6.id, question='How to access first item in list?', options=json.dumps(['A) list[1]', 'B) list[0]', 'C) list[first]']), correct_answer='B'),
            Question(quiz_id=quiz6.id, question='What does append() do?', options=json.dumps(['A) Remove item', 'B) Add item to end', 'C) Change item']), correct_answer='B'),
            Question(quiz_id=quiz6.id, question='How to change second item?', options=json.dumps(['A) list[2] = new', 'B) list[1] = new', 'C) list[0] = new']), correct_answer='B'),
            Question(quiz_id=quiz6.id, question='What does remove() do?', options=json.dumps(['A) Add item', 'B) Delete item', 'C) Show item']), correct_answer='B'),
        ]
        db.session.add_all(quiz6_questions)

        # Module 7: Functions
        module7 = Module(course_id=course.id, title='Functions', order=7)
        db.session.add(module7)
        db.session.commit()

        lesson7_content = '''
        <div class="lesson-content">
            <h2>🟢 Topic: Functions</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p class="big-text">Function = <strong>machine that does work</strong> ⚙️</p>
                <p>You write code once, use it many times!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>def greet():
    print("Hello! 👋")
    print("How are you? 😊")

# Use the function
greet()
greet()
greet()  # Can use many times!</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Create a function called "jump" that prints "Boing! 🦘" and call it 2 times!</p>
            </div>
        </div>

        <div class="lesson-content">
            <h2>🟢 Topic: Functions with Parameters</h2>

            <div class="explanation-box">
                <h3>🧠 Explanation</h3>
                <p>Functions can take information (parameters) and use them!</p>
            </div>

            <div class="code-box">
                <h3>💻 Code</h3>
                <pre><code>def say_hello(name):
    print("Hello", name + "! 🌟")
    print("Nice to meet you!")

# Use with different names
say_hello("Alex")
say_hello("Sam")
say_hello("Zoe")</code></pre>
            </div>

            <div class="activity-box">
                <h3>🎯 Activity</h3>
                <p>Create a function that takes a number and prints "Your number is: " + number</p>
            </div>
        </div>
        '''

        lesson7 = Lesson(module_id=module7.id, content=lesson7_content)
        quiz7 = Quiz(module_id=module7.id)
        db.session.add(lesson7)
        db.session.add(quiz7)
        db.session.commit()

        # Quiz questions for Module 7
        quiz7_questions = [
            Question(quiz_id=quiz7.id, question='What is a function?', options=json.dumps(['A) A variable', 'B) Reusable code block', 'C) A list']), correct_answer='B'),
            Question(quiz_id=quiz7.id, question='How to define a function?', options=json.dumps(['A) function name()', 'B) def name():', 'C) make name()']), correct_answer='B'),
            Question(quiz_id=quiz7.id, question='What are parameters?', options=json.dumps(['A) Function results', 'B) Input information', 'C) Function names']), correct_answer='B'),
            Question(quiz_id=quiz7.id, question='How to call a function?', options=json.dumps(['A) function.name', 'B) name()', 'C) call name']), correct_answer='B'),
            Question(quiz_id=quiz7.id, question='Why use functions?', options=json.dumps(['A) Make code shorter', 'B) Reuse code easily', 'C) Both A and B']), correct_answer='C'),
        ]
        db.session.add_all(quiz7_questions)

        # Module 8: Final Project
        module8 = Module(course_id=course.id, title='Final Project: Fun Chatbot', order=8)
        db.session.add(module8)
        db.session.commit()

        lesson8_content = '''
        <div class="lesson-content">
            <h2>🎯 FINAL BIG PROJECT: FUN CHATBOT</h2>

            <div class="project-intro">
                <h3>💡 Project Idea</h3>
                <p class="big-text">Create a computer that talks like your friend! 🤖💬</p>
                <p>Your chatbot will ask questions and respond based on your answers!</p>
            </div>

            <div class="project-requirements">
                <h3>🔧 What Your Chatbot Should Do</h3>
                <ul>
                    <li>✅ Ask for user's name</li>
                    <li>✅ Ask for favorite color</li>
                    <li>✅ Give different responses based on color</li>
                    <li>✅ Be friendly and fun!</li>
                </ul>
            </div>

            <div class="code-box">
                <h3>💻 Complete Code Example</h3>
                <pre><code>print("🤖 Hi! I'm your friendly chatbot!")
print("Let's chat! 💬")

name = input("What is your name? ")
print("Nice to meet you,", name + "! 😊")

color = input("What's your favorite color? ")

if color.lower() == "red":
    print("Wow! Red is a fire color! 🔥")
    print("You must be energetic! ⚡")
elif color.lower() == "blue":
    print("Blue is cool like the sky! 🌤️")
    print("You seem calm and peaceful! 😌")
elif color.lower() == "green":
    print("Green is the color of nature! 🌿")
    print("You love adventure! 🏞️")
else:
    print(color, "is a great choice! 🎨")
    print("You have unique taste! ✨")

print("Thanks for chatting with me,", name + "! 👋")
print("Come back soon! 🤗")</code></pre>
            </div>

            <div class="project-steps">
                <h3>🚀 How to Build It Step by Step</h3>
                <ol>
                    <li>Start with greeting message</li>
                    <li>Ask for name using input()</li>
                    <li>Ask for favorite color</li>
                    <li>Use if-elif-else to give different responses</li>
                    <li>End with goodbye message</li>
                </ol>
            </div>

            <div class="bonus-features">
                <h3>🎁 Bonus Features to Add</h3>
                <ul>
                    <li>⭐ Ask for age and give age-based responses</li>
                    <li>⭐ Ask for favorite food and comment on it</li>
                    <li>⭐ Add more color options</li>
                    <li>⭐ Make it loop to keep chatting!</li>
                </ul>
            </div>

            <div class="celebration">
                <h3>🎉 Congratulations!</h3>
                <p>You've completed the entire Python Adventure course! 🏆</p>
                <p>You are now a Python programmer! 🐍💻</p>
                <p>Keep coding and building amazing things! 🚀✨</p>
            </div>
        </div>
        '''

        lesson8 = Lesson(module_id=module8.id, content=lesson8_content)
        quiz8 = Quiz(module_id=module8.id)
        assignment8 = Assignment(module_id=module8.id, description='''
        🎯 **FINAL PROJECT ASSIGNMENT: Build Your Fun Chatbot!**

        **Requirements:**
        1. Your chatbot must ask for the user's name
        2. Ask for their favorite color
        3. Give different responses based on the color chosen
        4. Be friendly and fun in all messages
        5. End with a goodbye message

        **Bonus Points:**
        - Add more questions (age, food, hobby)
        - Make it loop to keep chatting
        - Add emoji reactions
        - Handle different color spellings

        **Submit your code and test it with different inputs!**
        ''')
        db.session.add(lesson8)
        db.session.add(quiz8)
        db.session.add(assignment8)
        db.session.commit()

        # Quiz questions for Module 8
        quiz8_questions = [
            Question(quiz_id=quiz8.id, question='What should your chatbot ask first?', options=json.dumps(['A) Favorite food', 'B) User name', 'C) Age']), correct_answer='B'),
            Question(quiz_id=quiz8.id, question='What controls different responses?', options=json.dumps(['A) print()', 'B) if-elif-else', 'C) input()']), correct_answer='B'),
            Question(quiz_id=quiz8.id, question='Why use .lower() with colors?', options=json.dumps(['A) Make text smaller', 'B) Handle different cases', 'C) Change color']), correct_answer='B'),
            Question(quiz_id=quiz8.id, question='What makes chatbot friendly?', options=json.dumps(['A) Fast code', 'B) Nice messages & emojis', 'C) Long code']), correct_answer='B'),
            Question(quiz_id=quiz8.id, question='What is the final project about?', options=json.dumps(['A) Making games', 'B) Building a talking program', 'C) Drawing pictures']), correct_answer='B'),
        ]
        db.session.add_all(quiz8_questions)

    if not User.query.filter_by(email='admin@hanominds.com').first():
        admin = User(name='Admin', email='admin@hanominds.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user.role == 'student':
            return redirect(url_for('student_dashboard'))
        elif user.role == 'instructor':
            return redirect(url_for('instructor_dashboard'))
        elif user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password) and user.status == 'active':
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials or account inactive.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/student-dashboard')
def student_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'student':
        return redirect(url_for('index'))

    courses = Course.query.all()
    progress = Progress.query.filter_by(user_id=user.id).all()
    
    total_modules = 0
    completed = 0
    courses_data = []

    for course in courses:
        modules = Module.query.filter_by(course_id=course.id).order_by(Module.order).all()
        total = len(modules)
        course_module_ids = [m.id for m in modules]
        comp = sum(1 for p in progress if p.module_id in course_module_ids and p.completed)
        
        total_modules += total
        completed += comp
        
        c_progress_percent = (comp / total * 100) if total > 0 else 0
        courses_data.append({
            'course': course,
            'emoji': '🐍' if 'python' in course.title.lower() else '🚀',
            'desc': 'Learn programming with fun!' if 'python' in course.title.lower() else 'A Complete Technology Curriculum',
            'progress_percent': c_progress_percent
        })

    progress_percent = (completed / total_modules * 100) if total_modules > 0 else 0

    leaderboard = Leaderboard.query.order_by(Leaderboard.points.desc()).limit(5).all()
    leaderboard_data = [{'name': User.query.get(l.user_id).name, 'points': l.points} for l in leaderboard]

    user_leaderboard = Leaderboard.query.filter_by(user_id=user.id).first()
    user_points = user_leaderboard.points if user_leaderboard else 0
    user_streak = user_leaderboard.streak if user_leaderboard else 0

    return render_template('student-dashboard.html', user=user, progress_percent=progress_percent, courses_data=courses_data, leaderboard=leaderboard_data, user_points=user_points, user_streak=user_streak)

@app.route('/course/<int:course_id>')
def course(course_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'student':
        return redirect(url_for('index'))

    course = Course.query.get_or_404(course_id)
    modules = Module.query.filter_by(course_id=course.id).order_by(Module.order).all()
    progress = Progress.query.filter_by(user_id=user.id).all()
    progress_dict = {p.module_id: p for p in progress}

    for mod in modules:
        mod.status = 'locked'
        if mod.id in progress_dict:
            if progress_dict[mod.id].completed:
                mod.status = 'completed'
            else:
                mod.status = 'current'
        elif mod.order == 1 or (mod.order > 1 and progress_dict.get(modules[mod.order-2].id, Progress()).completed):
            mod.status = 'current'

    return render_template('course.html', course=course, modules=modules)

@app.route('/module/<int:module_id>')
def module(module_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    if user.role != 'student':
        return redirect(url_for('index'))

    mod = Module.query.get_or_404(module_id)
    lesson = Lesson.query.filter_by(module_id=module_id).first()
    quiz = Quiz.query.filter_by(module_id=module_id).first()
    assignment = Assignment.query.filter_by(module_id=module_id).first()
    progress = Progress.query.filter_by(user_id=user.id, module_id=module_id).first()
    questions = []
    if quiz:
        questions = Question.query.filter_by(quiz_id=quiz.id).all()
        for q in questions:
            q.options_list = json.loads(q.options)

    if progress:
        if check_completion(progress):
            db.session.commit()

    return render_template('module.html', module=mod, lesson=lesson, quiz=quiz, assignment=assignment, progress=progress, questions=questions)

def check_completion(progress):
    from datetime import datetime, timedelta
    
    quiz_exists = Quiz.query.filter_by(module_id=progress.module_id).first() is not None
    assignment_exists = Assignment.query.filter_by(module_id=progress.module_id).first() is not None

    quiz_ok = (progress.quiz_score >= 50) if quiz_exists else True
    assignment_ok = progress.assignment_done if assignment_exists else True

    if quiz_ok and assignment_ok and not progress.completed:
        progress.completed = True
        leaderboard = Leaderboard.query.filter_by(user_id=progress.user_id).first()
        if not leaderboard:
            leaderboard = Leaderboard(user_id=progress.user_id, streak=1)
            db.session.add(leaderboard)
        else:
            leaderboard.points = (leaderboard.points or 0) + 10
            leaderboard.streak = (leaderboard.streak or 0) + 1
        return True
    return False

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'student':
        return redirect(url_for('index'))

    quiz_obj = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    progress = Progress.query.filter_by(user_id=user.id, module_id=quiz_obj.module_id).first()
    if not progress:
        progress = Progress(user_id=user.id, module_id=quiz_obj.module_id)
        db.session.add(progress)
        db.session.commit()

    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.form.get(f'q{q.id}')
            if answer is None:
                continue
            if answer.isdigit():
                selected_option = chr(ord('A') + int(answer))
            else:
                selected_option = answer
            if selected_option == q.correct_answer:
                score += 1
        progress.quiz_score = int(score / len(questions) * 100)
        flash(f'Quiz submitted! Your score: {progress.quiz_score}% 🎉', 'success')
        completed_changed = check_completion(progress)
        db.session.commit()
        if completed_changed:
            flash('Great! Module completed and next module unlocked. 🚀', 'success')
        return redirect(url_for('module', module_id=quiz_obj.module_id))

    for q in questions:
        q.options_list = json.loads(q.options)

    return render_template('quiz.html', quiz=quiz_obj, questions=questions)

@app.route('/assignment/<int:assignment_id>', methods=['GET', 'POST'])
def assignment(assignment_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'student':
        return redirect(url_for('index'))

    assign = Assignment.query.get_or_404(assignment_id)
    progress = Progress.query.filter_by(user_id=user.id, module_id=assign.module_id).first()
    if not progress:
        progress = Progress(user_id=user.id, module_id=assign.module_id)
        db.session.add(progress)
        db.session.commit()

    if request.method == 'POST':
        content = request.form['content']
        submission = Submission(user_id=user.id, assignment_id=assignment_id, content=content)
        db.session.add(submission)
        progress.assignment_done = True
        check_completion(progress)
        db.session.commit()
        return redirect(url_for('module', module_id=assign.module_id))

    return render_template('assignment.html', assignment=assign)

@app.route('/instructor-dashboard')
def instructor_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    return render_template('instructor-dashboard.html', user=user)

@app.route('/manage-modules')
def manage_modules():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    courses = Course.query.all()
    modules_by_course = {}
    for course in courses:
        modules_by_course[course] = Module.query.filter_by(course_id=course.id).order_by(Module.order).all()
        
    return render_template('manage-modules.html', modules_by_course=modules_by_course)

@app.route('/edit-module/<int:module_id>', methods=['GET', 'POST'])
def edit_module(module_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    mod = Module.query.get_or_404(module_id)
    lesson = Lesson.query.filter_by(module_id=module_id).first()
    quiz = Quiz.query.filter_by(module_id=module_id).first()
    assignment = Assignment.query.filter_by(module_id=module_id).first()

    if request.method == 'POST':
        if 'lesson_content' in request.form:
            if lesson:
                lesson.content = request.form['lesson_content']
            else:
                lesson = Lesson(module_id=module_id, content=request.form['lesson_content'])
                db.session.add(lesson)
        elif 'assignment_desc' in request.form:
            if assignment:
                assignment.description = request.form['assignment_desc']
            else:
                assignment = Assignment(module_id=module_id, description=request.form['assignment_desc'])
                db.session.add(assignment)
        # For quiz, add questions
        db.session.commit()
        return redirect(url_for('manage_modules'))

    questions = Question.query.filter_by(quiz_id=quiz.id).all() if quiz else []
    return render_template('edit-module.html', module=mod, lesson=lesson, assignment=assignment, questions=questions)

@app.route('/add-module/<int:course_id>', methods=['GET', 'POST'])
def add_module(course_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    course = Course.query.get_or_404(course_id)

    if request.method == 'POST':
        title = request.form['title']
        # Get the next order number
        max_order = db.session.query(db.func.max(Module.order)).filter_by(course_id=course.id).scalar() or 0
        new_module = Module(course_id=course.id, title=title, order=max_order + 1)
        db.session.add(new_module)
        db.session.commit()
        flash('Module added successfully! 🎉', 'success')
        return redirect(url_for('manage_modules'))

    return render_template('add-module.html')

@app.route('/view-students')
def view_students():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    students = User.query.filter_by(role='student').all()
    total_modules = Module.query.count()
    
    # Enrich student data with progress tracking
    student_data = []
    for student in students:
        progress_records = Progress.query.filter_by(user_id=student.id).all()
        
        completed_count = sum(1 for p in progress_records if p.completed)
        quiz_scores = [p.quiz_score for p in progress_records if p.quiz_score > 0]
        avg_quiz_score = sum(quiz_scores) / len(quiz_scores) if quiz_scores else 0
        
        leaderboard = Leaderboard.query.filter_by(user_id=student.id).first()
        points = leaderboard.points if leaderboard else 0
        
        completion_rate = (completed_count / total_modules * 100) if total_modules > 0 else 0
        
        student_data.append({
            'student': student,
            'modules_completed': completed_count,
            'total_modules': total_modules,
            'completion_rate': round(completion_rate, 1),
            'avg_quiz_score': round(avg_quiz_score, 1),
            'points': points
        })
    
    # Sort by completion rate
    student_data.sort(key=lambda x: x['completion_rate'], reverse=True)
    
    return render_template('view-students.html', student_data=student_data, total_modules=total_modules)


@app.route('/instructor-analytics')
def instructor_analytics():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'instructor':
        return redirect(url_for('index'))

    students = User.query.filter_by(role='student').all()
    total_modules = Module.query.count()
    
    # Build analytics for each student
    student_stats = []
    for student in students:
        progress_records = Progress.query.filter_by(user_id=student.id).all()
        
        completed_count = sum(1 for p in progress_records if p.completed)
        quiz_scores = [p.quiz_score for p in progress_records if p.quiz_score > 0]
        avg_quiz_score = sum(quiz_scores) / len(quiz_scores) if quiz_scores else 0
        
        leaderboard = Leaderboard.query.filter_by(user_id=student.id).first()
        points = leaderboard.points if leaderboard else 0
        
        badges = UserBadge.query.filter_by(user_id=student.id).count()
        
        completion_rate = (completed_count / total_modules * 100) if total_modules > 0 else 0
        
        student_stats.append({
            'student': student,
            'modules_completed': completed_count,
            'total_modules': total_modules,
            'completion_rate': round(completion_rate, 1),
            'avg_quiz_score': round(avg_quiz_score, 1),
            'points': points,
            'badges': badges,
            'progress_records': progress_records
        })
    
    # Sort by completion rate descending
    student_stats.sort(key=lambda x: x['completion_rate'], reverse=True)
    
    # Calculate class statistics
    class_stats = {
        'total_students': len(students),
        'avg_class_completion': round(sum(s['completion_rate'] for s in student_stats) / len(student_stats), 1) if student_stats else 0,
        'avg_class_quiz_score': round(sum(s['avg_quiz_score'] for s in student_stats) / len(student_stats), 1) if student_stats else 0,
        'total_modules': total_modules
    }
    
    return render_template('instructor-analytics.html', student_stats=student_stats, class_stats=class_stats)

@app.route('/admin-dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'admin':
        return redirect(url_for('index'))

    users = User.query.all()
    return render_template('admin-dashboard.html', user=user, users=users)

@app.route('/admin/add-user', methods=['POST'])
def add_user():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'admin':
        return redirect(url_for('index'))

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    new_user = User(name=name, email=email, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)