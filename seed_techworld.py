import json
import re
from models import db, Course, Module, Lesson, Quiz, Question, Assignment

def run_seed():
    with open('tech_world_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create course
        course = Course.query.filter_by(title="Tech World for Kids").first()
        if not course:
            course = Course(title="Tech World for Kids")
            db.session.add(course)
            db.session.commit()
            print("Created course:", course.title)
        else:
            print("Course already exists! Wiping old modules...")
            Module.query.filter_by(course_id=course.id).delete()
            db.session.commit()

        # Custom options mapping for questions without A) B) C) D) format
        custom_q_map = {
            "True or False: A pencil is technology.": (["A) True", "B) False"], 'A'),
            "Which type of tech can learn from data?": (["A) AI", "B) Hardware", "C) Website", "D) App"], 'A'),
            "Minecraft is an example of which tech type?": (["A) Game", "B) Hardware", "C) Website", "D) App"], 'A'),
            "Zomato / Swiggy is which category of tech?": (["A) Food Delivery / Tech", "B) Hardware", "C) Social Media", "D) Games"], 'A'),
            "True or False: Technology is only used at school.": (["A) True", "B) False"], 'B'),
            "What is WhatsApp's main job?": (["A) Messaging & Calls", "B) Watching Videos", "C) Playing Games", "D) Buying stuff"], 'A'),
            "True or False: Every app needs the internet to work.": (["A) True", "B) False"], 'B'),
            "Difference between an app and a website?": (["A) App lives on phone, website on internet", "B) Both live on phone", "C) Both live on internet", "D) None of the above"], 'A'),
            "In the restaurant analogy, the kitchen equals what?": (["A) Backend", "B) Frontend", "C) Cashier", "D) Manager"], 'A'),
            "True or False: Most users know what the backend does.": (["A) True", "B) False"], 'B'),
            "True or False: Every company starts with hundreds of people.": (["A) True", "B) False"], 'B'),
            "In our school play analogy, testing equals what?": (["A) The small test run", "B) Writing script", "C) Opening night", "D) Finding actors"], 'A'),
            "True or False: Apps are finished forever once they launch.": (["A) True", "B) False"], 'B'),
            "True or False: Apps are perfect when they first launch.": (["A) True", "B) False"], 'B'),
            "True or False: A game must be perfect before any testing begins.": (["A) True", "B) False"], 'B'),
            "YouTube is the world's second largest what after Google?": (["A) Search Engine", "B) Game", "C) Online Shop", "D) Social Network"], 'A'),
            "True or False: You have to pay to watch most YouTube content.": (["A) True", "B) False"], 'B'),
            "True or False: Investors always recognise great startup ideas immediately.": (["A) True", "B) False"], 'B'),
            "True or False: You need to be an adult to start a business.": (["A) True", "B) False"], 'B'),
            "If you earn Rs 500 and spend Rs 380, what is your profit?": (["A) Rs 120", "B) Rs 880", "C) Rs 500", "D) Rs 380"], 'A'),
            "Which is better: high revenue with high costs, or lower revenue with lower costs?": (["A) Lower revenue with lower costs (More profit)", "B) High revenue with high costs", "C) They are exactly the same", "D) None of the above"], 'A'),
            "True or False: If an app is free, the company earns no money from it.": (["A) True", "B) False"], 'B'),
        }

        for m_data in data:
            mod = Module(course_id=course.id, title=m_data['title'], order=m_data['num'])
            db.session.add(mod)
            db.session.commit()

            # Construct HTML Lesson Content
            html_parts = []
            for i, topic in enumerate(m_data['topics']):
                html_parts.append(f"""
        <div class="lesson-content">
            <h2>🟢 Topic {i+1}: {topic['name']}</h2>

            <div class="explanation-box">
                <h3>🧠 The Story</h3>
                <p class="big-text">{topic['story']}</p>
            </div>

            <div class="example-box">
                <h3>🌍 Real-Life Example</h3>
                <p>{topic['realLife']}</p>
            </div>

            <div class="fun-box">
                <h3>😂 Funny Example</h3>
                <p>{topic['funny']}</p>
            </div>

            <div class="activity-box">
                <h3>🎯 Classroom Activity</h3>
                <p>{topic['activity']}</p>
            </div>
        </div>
                """)

            lesson = Lesson(module_id=mod.id, content='\\n'.join(html_parts))
            db.session.add(lesson)

            # Quiz Setup
            quiz = Quiz(module_id=mod.id)
            db.session.add(quiz)
            db.session.commit()

            # Process Project Assignment
            proj = m_data.get('project')
            if proj:
                assignment_desc = f"🎯 **MINI PROJECT: {proj['title']}**\\n\\n"
                for step in proj['steps']:
                    assignment_desc += f"- {step}\\n"
                assignment_desc += f"\\n**What you will learn:** {proj['learn']}"
                
                assignment = Assignment(module_id=mod.id, description=assignment_desc)
                db.session.add(assignment)

            # Process Questions
            for topic in m_data['topics']:
                for q_data in topic['quiz']:
                    q_text = q_data['q'].strip()
                    hint = q_data['hint'].strip()
                    
                    options = []
                    correct_answer = 'A'

                    if q_text in custom_q_map:
                        options = custom_q_map[q_text][0]
                        correct_answer = custom_q_map[q_text][1]
                    elif "A)" in hint and "B)" in hint:
                        # Parse options using regex. Example: A) Apple B) Banana
                        # Handle potential missing D)
                        tokens = re.split(r'([A-D]\))', hint)
                        current_opt = ""
                        for token in tokens:
                            token = token.strip()
                            if token in ['A)', 'B)', 'C)', 'D)']:
                                if current_opt:
                                    options.append(current_opt.strip())
                                current_opt = token
                            else:
                                current_opt += " " + token
                        if current_opt:
                            options.append(current_opt.strip())
                        correct_answer = 'A' # Defaulting A as correct since doc didn't specify. AI heuristic can't evaluate here.
                    else:
                        # Fallback
                        options = [f"A) {hint}", "B) True", "C) False", "D) None"]
                        correct_answer = 'A'
                    
                    # Ensure options array is correctly formatted JSON list
                    ques = Question(
                        quiz_id=quiz.id,
                        question=q_text,
                        options=json.dumps(options),
                        correct_answer=correct_answer
                    )
                    db.session.add(ques)

            db.session.commit()
            print(f"Added module {mod.order}: {mod.title}")

if __name__ == '__main__':
    from app import app
    with app.app_context():
        run_seed()
        print('Tech World for Kids seeding complete!')
