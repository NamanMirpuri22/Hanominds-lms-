const fs = require('fs');

const modules = [
  {
    num:1, title:"What is Technology?", days:"Days 1–3",
    topics:[
      {
        name:"What is technology?",
        story:"Imagine you wake up in the morning and your phone alarm goes off. You check the weather app. Your mom orders breakfast through Zomato. Your dad watches news on YouTube. Your school bell is connected to a digital timer. ALL of this is technology. Technology is anything humans created to solve a problem or make life easier — from a pencil to a spaceship!",
        realLife:"When you watch a YouTube video, technology decides which video to show you next. When you use Google Maps to reach somewhere, technology figures out the fastest route in seconds.",
        funny:"Before smartphones, if you forgot where your friend lived, you were just lost. You would wander around like a confused pigeon hoping to recognise the building. Technology fixed that. Now we just wander around staring at our phones instead.",
        activity:"Make a list of 10 things you used today that involve technology. Then circle which ones did not exist 20 years ago. Surprise — almost all of them!",
        quiz:[
          {q:"Which of these is technology?",hint:"A) A rock  B) A river  C) A smartphone  D) A cloud"},
          {q:"Who creates technology?",hint:"A) Aliens  B) Nature  C) Humans  D) Robots (that humans made)"},
          {q:"True or False: A pencil is technology.",hint:"It was invented to solve a problem!"},
          {q:"Which problem does Google Maps solve?",hint:"A) Hunger  B) Getting lost  C) Loneliness  D) Bad music"},
          {q:"What is the main purpose of technology?",hint:"A) Look cool  B) Solve problems  C) Confuse adults  D) Make kids stare at screens"},
        ]
      },
      {
        name:"Types of technology",
        story:"Technology is like a big family with different cousins. Mobile apps are your phone friends. Websites are digital shops and libraries. AI is the really smart cousin who learns everything. Games are the fun cousin. Hardware is the physical stuff like laptops and tablets. Each type has a different job but they all live in the same digital neighbourhood!",
        realLife:"Instagram is a mobile app. Google.com is a website. Siri is AI. Minecraft is a game. Your laptop is hardware. You use all of them — you are basically a tech expert already!",
        funny:"AI is the cousin who reads every book ever written and still loses at FIFA because strategy is different from knowledge. But AI is learning football too. Be very afraid.",
        activity:"Draw a spider diagram with Technology in the centre. Branch out with 5 types: app, website, AI, hardware, game — and write one example for each from your own life.",
        quiz:[
          {q:"Instagram is which type of technology?",hint:"A) Hardware  B) Website  C) Mobile app  D) AI"},
          {q:"Which type of tech can learn from data?",hint:"Think: the smart cousin..."},
          {q:"What is hardware?",hint:"A) A maths problem  B) Physical tech devices  C) A coding language  D) An app store"},
          {q:"Minecraft is an example of which tech type?",hint:"Simple one!"},
          {q:"Which technology uses the internet most directly?",hint:"A) Pencil  B) Calculator  C) Website  D) Chair"},
        ]
      },
      {
        name:"Technology in daily life",
        story:"From the moment you wake up to the second you sleep, technology is around you like an invisible friend. Alarm clocks, food delivery apps, school management systems, streaming music, video calls with grandparents — every single moment now has a tech layer. It is less like using technology and more like breathing it.",
        realLife:"When your school puts homework on an app, that is EdTech. When your parents pay electricity bills online, that is FinTech. When you video call relatives abroad, that is Communication Tech. You live in all these categories simultaneously!",
        funny:"My grandad still writes letters to people. By the time the letter arrives, the news is three weeks old and the person has already found out, forgotten, and moved on. Technology made sure information travels faster than the problem it describes.",
        activity:"Track your tech usage timeline for one full day. Every hour, note which technology you used. At the end, count: how many hours were completely tech-free?",
        quiz:[
          {q:"What is EdTech?",hint:"A) Education Technology  B) Editing Technology  C) Entertainment Technology  D) Electric Technology"},
          {q:"Zomato / Swiggy is which category of tech?",hint:"Think about what problem it solves..."},
          {q:"True or False: Technology is only used at school.",hint:"Think of your full day..."},
          {q:"Which tech is used when you video call someone?",hint:"A) Hardware only  B) Communication technology  C) AI only  D) Games"},
          {q:"Which company helped people buy things online?",hint:"A) Netflix  B) Amazon  C) Spotify  D) Discord"},
        ]
      }
    ],
    project:{
      title:"My Tech Life Map",
      steps:[
        "List every technology you use in a week",
        "Categorise each one: app / website / hardware / AI / game",
        "Draw connections between them (e.g. phone leads to apps leads to notifications)",
        "Identify which 3 you would miss most if they disappeared tomorrow",
        "Present to the class: 'If I had to live without tech for a week...'"
      ],
      learn:"Category thinking, observational skills, and the surprisingly massive role of tech in daily life."
    }
  },
  {
    num:2, title:"How Apps & Websites Work", days:"Days 4–7",
    topics:[
      {
        name:"What is an app?",
        story:"An app (short for application) is like a tiny robot that lives in your phone and does one specific job really well. The camera app takes photos. The calculator does maths. Spotify plays music. Each robot has its own personality, design, and skill set. Someone had to design the robot, program its brain, test it, and release it to the world. That entire process — from idea to your phone — is app development!",
        realLife:"WhatsApp is an app. It has one job: let people message and call each other. Even though it looks simple, WhatsApp has thousands of engineers maintaining it for 2 billion people every day.",
        funny:"There are over 5 million apps on the Play Store. At least 4.9 million of them are apps someone built, forgot about, and never updated. There is probably an app for counting your socks that last worked in 2013.",
        activity:"Pick your 3 favourite apps. For each one, write: What is its one main job? Who would use it? What would happen if it disappeared tomorrow?",
        quiz:[
          {q:"What does app stand for?",hint:"A) Apple  B) Application  C) Apparatus  D) Append"},
          {q:"How many apps are on major app stores?",hint:"A) Hundreds  B) Thousands  C) Millions  D) Billions"},
          {q:"What is WhatsApp's main job?",hint:"Think: its core purpose..."},
          {q:"Who builds apps?",hint:"A) Only big companies  B) Developers and designers  C) The government  D) Robots automatically"},
          {q:"True or False: Every app needs the internet to work.",hint:"Think of offline apps like a calculator or camera..."},
        ]
      },
      {
        name:"What is a website?",
        story:"A website is like a digital billboard that anyone in the world can visit. While an app lives inside your phone, a website lives on the internet — accessible from any device with a browser. Think of the internet as a giant city. Every website is a shop or building in that city. When you type google.com you are visiting Google's building. The address (google.com) is called a domain name — it is basically the GPS coordinates of that building.",
        realLife:"Wikipedia is a website — a giant digital library where millions of people contribute and read. Amazon.com is a website — a digital shopping mall that never closes and never has parking problems.",
        funny:"In the early 2000s, websites were so basic they looked like your little cousin's art project — blinking text, tiled backgrounds, animated gifs of dancing babies. We have come a long way. Or have we? Some government websites disagree.",
        activity:"Visit 5 different websites today. For each one write: What is its domain name? What does it do? Is it a shop, library, news site, entertainment or service?",
        quiz:[
          {q:"What is a domain name?",hint:"A) The website's password  B) The web address like google.com  C) A type of app  D) A bank account"},
          {q:"What do you need to visit a website?",hint:"A) A special card  B) A subscription  C) A browser and internet  D) Permission"},
          {q:"Difference between an app and a website?",hint:"One lives on your phone, one lives on..."},
          {q:"Amazon is primarily which type of online business?",hint:"A) Social media  B) E-commerce  C) Gaming  D) Search engine"},
          {q:"Who can visit a public website?",hint:"A) Only that country  B) Only paying members  C) Anyone with internet  D) Only adults"},
        ]
      },
      {
        name:"Frontend vs backend",
        story:"Think of a restaurant. The front of house is what you see — the decor, the menu, the waiter smiling at you. The kitchen is what you never see — the chef cooking, the dishwasher cleaning, the ingredients being prepared. A website works exactly the same. The frontend is what you see (colours, buttons, images). The backend is what you cannot see (the database storing your data, the server processing your requests). Both are equally important.",
        realLife:"When you scroll Instagram, the pretty pictures and heart buttons are the frontend. When you like a photo and it saves forever and updates your friend's notification, that is the backend. Two different teams build these two different things.",
        funny:"Frontend developers and backend developers argue about who has the more important job constantly. Frontend says you'd look at nothing without us. Backend says you'd have nothing to show without us. They're both right and they both know it and it drives them crazy.",
        activity:"Pick any app you use. Draw two columns — FRONTEND (things you can see) and BACKEND (things that must happen invisibly). Try to list at least 4 items in each column.",
        quiz:[
          {q:"What is the frontend of a website?",hint:"A) Hidden database  B) Part users can see and interact with  C) The server  D) The coding language"},
          {q:"What does the backend handle?",hint:"A) Colours and fonts  B) Buttons and images  C) Data storage and server logic  D) Profile pictures"},
          {q:"In the restaurant analogy, the kitchen equals what?",hint:"Think about what is hidden from the customer..."},
          {q:"Which team makes buttons look beautiful?",hint:"A) Backend  B) Frontend  C) Database team  D) Security team"},
          {q:"True or False: Most users know what the backend does.",hint:"Think about how invisible it is..."},
        ]
      }
    ],
    project:{
      title:"Website vs App Detective Case",
      steps:[
        "List 10 digital products you know",
        "For each one: Is it an app, a website, or both?",
        "For those that are both, identify what is different about each version",
        "Identify which version relies more on frontend vs backend",
        "Present your detective report to the class"
      ],
      learn:"App vs website distinction, frontend vs backend awareness, and analytical thinking."
    }
  },
  {
    num:3, title:"Inside a Tech Company", days:"Days 8–11",
    topics:[
      {
        name:"What is a company?",
        story:"A company is basically a group of people who got together to solve a problem and decided to get paid for it. Imagine you and your friends decide to make the world's best homework helper app. You need someone to design it, someone to code it, someone to test it, and someone to tell people about it. Congratulations — you just formed a company. Every big tech company started exactly this way.",
        realLife:"Apple started with 3 people in a garage. Google started with 2 university students. WhatsApp was built by 2 people who both got rejected by Facebook earlier — then Facebook bought WhatsApp for 19 billion dollars. Life is funny.",
        funny:"Every company has a meeting where 12 people discuss something that could have been an email. This is a universal law of company physics. It cannot be changed. Physicists have studied this.",
        activity:"Imagine you are starting a company to solve a problem at your school. Name the company. What problem does it solve? Who are the first 3 team members and what does each person do?",
        quiz:[
          {q:"What is the main purpose of a company?",hint:"A) Have meetings  B) Solve a problem and earn money doing it  C) Hire as many people as possible  D) Make a nice logo"},
          {q:"Where did Apple famously start?",hint:"A) A school  B) An office tower  C) A garage  D) A coffee shop"},
          {q:"Who started Google?",hint:"A) Steve Jobs  B) Mark Zuckerberg  C) Larry Page and Sergey Brin  D) Elon Musk"},
          {q:"True or False: Every company starts with hundreds of people.",hint:"Think of WhatsApp, Apple, Google..."},
          {q:"What did Facebook pay for WhatsApp?",hint:"A) $1 million  B) $19 billion  C) $1 billion  D) Nothing"},
        ]
      },
      {
        name:"Different roles in a tech company",
        story:"A tech company is like a cricket team — everyone has a different position but they are playing the same match. The Developer writes the code (the all-rounder). The Designer makes everything beautiful and easy to use (the stylish opening batsman). The Tester tries to break things before users can (the wicketkeeper). The Manager keeps everyone organised and on schedule (the captain). The Product Manager decides what to build next (the coach with the big picture).",
        realLife:"When Instagram releases a new feature like Reels, the PM decided it, the Designer drew it, the Developer built it, the Tester found bugs, and the Manager kept everyone on deadline. All five roles were needed for that one feature.",
        funny:"Testers are the only people whose job description literally includes 'try to break things.' They click every button in the wrong order, type random letters into text boxes, and try to crash the app in creative ways. They are chaotic good.",
        activity:"Role play! In groups of 4, each person picks a role: Developer, Designer, Tester, or Manager. Together, plan how you would add a dark mode to your school app. What does each role contribute?",
        quiz:[
          {q:"What is the main job of a Developer?",hint:"A) Draw mockups  B) Write code  C) Find bugs  D) Organise meetings"},
          {q:"A UI/UX Designer focuses on what?",hint:"A) Server infrastructure  B) How the product looks and feels  C) Business strategy  D) Marketing"},
          {q:"What does a Tester do?",hint:"A) Teaches others  B) Writes code  C) Deliberately tries to find bugs  D) Designs logos"},
          {q:"In cricket terms who is the captain of a tech team?",hint:"A) Developer  B) Designer  C) Manager  D) Tester"},
          {q:"Which role decides WHAT to build next?",hint:"A) Designer  B) Product Manager  C) Tester  D) HR Manager"},
        ]
      },
      {
        name:"How a team builds a product",
        story:"Building a tech product is like planning a school play. First everyone decides what the play is about (planning). Then the script is written (design). Then the actors rehearse (development). Then you do a test run for a small audience (testing). Then the big opening night (launch). Finally everyone gives feedback and you improve for the next show (updates). Tech teams follow the exact same steps — called the Product Development Lifecycle.",
        realLife:"When Spotify releases a new feature like the AI DJ playlist creator, it went through all these stages over several months before you ever saw it. What looks like a simple button represents thousands of hours of work.",
        funny:"In the planning meeting, someone always says it will only take two weeks. This is the biggest lie in software development. It always takes three times longer. Always. This is called Hofstadter's Law and it even applies to itself.",
        activity:"In teams of 4 to 5, plan a simple product — a lost and found app for your school. Complete all 5 stages on paper: Plan, Design, Build (describe features), Test (what could go wrong?), Launch (who will use it?).",
        quiz:[
          {q:"What is the first stage of building a product?",hint:"A) Testing  B) Launch  C) Planning  D) Marketing"},
          {q:"In our school play analogy, testing equals what?",hint:"The small test run before opening night..."},
          {q:"What happens after a product launches?",hint:"A) Everyone stops working  B) Team collects feedback and improves it  C) Company closes  D) Testers relax"},
          {q:"Why do teams test before launching?",hint:"A) To delay the launch  B) Find and fix problems before users see them  C) Make the team feel busy  D) Required by law"},
          {q:"True or False: Apps are finished forever once they launch.",hint:"Think of how often your apps update..."},
        ]
      }
    ],
    project:{
      title:"Dream Team Org Chart",
      steps:[
        "Pick an app idea — any idea at all!",
        "Decide which 6 roles your team needs",
        "Write each role's main daily responsibility in one sentence",
        "Draw the org chart showing who reports to who",
        "Present: 'This is our team and here is why we need every single person'"
      ],
      learn:"Organisational thinking, understanding team roles, and how different skills combine to build one product."
    }
  },
  {
    num:4, title:"How a Product is Built", days:"Days 12–15",
    topics:[
      {
        name:"Idea to design to development to testing to launch",
        story:"Every app that millions of people love started as a scribble. Instagram was sketched on a napkin. The idea for WhatsApp came when a founder noticed phone contacts — why not show what people are doing? Good ideas often come from noticing a problem you personally face. Then scribbles become wireframes (rough drawings of screens). Designers make them beautiful. Developers build them. Testers break them and get them fixed. Then launch day!",
        realLife:"Snapchat was originally called Picaboo. The name changed. The idea of disappearing photos was considered weird and useless by many investors. It now has 375 million daily users. Ideas evolve. First versions are rarely final ones.",
        funny:"Version 1 of most apps is what developers call embarrassing in hindsight. The first YouTube video ever uploaded was a man at the zoo talking about elephants for 18 seconds. Not exactly the future of media. And yet, here we are.",
        activity:"Take a simple idea — a water reminder app. Draw 3 simple screen sketches: the home screen, the settings screen, and the reminder notification. You have just made a wireframe!",
        quiz:[
          {q:"What is a wireframe?",hint:"A) A type of code  B) A rough sketch of app screens  C) A network cable  D) A type of phone case"},
          {q:"What was Instagram originally sketched on?",hint:"A) A computer  B) A whiteboard  C) A napkin  D) A sticky note"},
          {q:"What was Snapchat originally called?",hint:"A) Flashchat  B) Picaboo  C) Disappear  D) PhotoSnap"},
          {q:"When does the development phase happen?",hint:"A) Before the idea  B) After design, before testing  C) After launch  D) Before design"},
          {q:"True or False: Apps are perfect when they first launch.",hint:"Think of app update notifications..."},
        ]
      },
      {
        name:"Building a simple game — the story",
        story:"Let's build CatchTheApple — a game where a basket moves left and right to catch falling apples. Step 1 Idea: Let's make a catching game. Step 2 Design: Draw the basket, apple, and score counter on paper. Step 3 Development: Code — when LEFT key pressed, move basket left. Step 4 Testing: Play it. Does it crash? Is it too hard? Step 5 Launch: Share with friends. Step 6 Feedback: Add more apples! This is the exact same process any professional game studio uses.",
        realLife:"Angry Birds was rejected by 51 publishers before finding success. The team kept iterating — improving based on feedback — through all 5 stages many times before the world ever played it.",
        funny:"The first time developers test a game, the character usually moves in the wrong direction, floats off the screen, or falls through the floor into digital oblivion. This is completely normal. Every game you love had a phase where nothing worked.",
        activity:"Design your own mini game on paper. Name it. Draw the main screen. List 3 rules. List 2 things that could go wrong (testing step). Who is your target player?",
        quiz:[
          {q:"In game development, what is iterating?",hint:"A) Starting over completely  B) Giving up  C) Improving based on feedback  D) Releasing to the public"},
          {q:"How many publishers rejected Angry Birds first?",hint:"A) 5  B) 11  C) 51  D) 1"},
          {q:"What happens during the testing phase of a game?",hint:"A) Designing new levels  B) Coding the game engine  C) Playing it to find what's broken  D) Marketing to players"},
          {q:"What is feedback in product development?",hint:"A) Comments from users about what works or doesn't  B) A type of error  C) The sound a phone makes  D) A marketing strategy"},
          {q:"True or False: A game must be perfect before any testing begins.",hint:"Think of our apples falling through the floor example..."},
        ]
      }
    ],
    project:{
      title:"Paper Prototype Challenge",
      steps:[
        "Write your app idea in one sentence: problem + solution",
        "Sketch 3 screens on paper: home screen, main feature, settings",
        "Write what happens when the user taps each button",
        "Run a test with a classmate — can they understand how to use it?",
        "Collect feedback and improve one thing based on their response"
      ],
      learn:"Design thinking, user testing, iteration, and empathy with users."
    }
  },
  {
    num:5, title:"Real-Life Company Examples", days:"Days 16–18",
    topics:[
      {
        name:"How Google works",
        story:"Google is like a librarian who has read every single page on the internet — billions of web pages — and memorised where to find what. When you search best samosas near me, Google's brain (called an algorithm) looks through its giant index and decides which results would actually help you most. It ranks them by how many other sites link to them, how relevant the words are, how fast the page loads, and how trustworthy the source is. All in about 0.3 seconds. Google runs this for 8.5 billion searches every day.",
        realLife:"Google earns money mainly through ads. When businesses want to appear at the top of search results, they pay Google. That is why some results have a tiny Ad label. The free Google you use is funded by businesses competing for your attention.",
        funny:"Google knows so much about you that it sometimes feels like it reads minds. You mention pizza to your friend. An hour later, Google shows pizza ads. This is either brilliant technology or terrifying. Often both simultaneously.",
        activity:"Do a Google search and look at the results. Identify which results are ads (look for the Ad label). Which are organic (not paid)? Why do certain results appear at the top?",
        quiz:[
          {q:"What is Google's algorithm?",hint:"A) A type of computer  B) Rules that decide which results to show  C) The search bar  D) Google's logo"},
          {q:"How many searches does Google process daily?",hint:"A) 1 million  B) 500 million  C) 8.5 billion  D) 1 trillion"},
          {q:"How does Google mainly earn money?",hint:"A) Selling computers  B) Monthly subscriptions  C) Online advertising  D) Selling data"},
          {q:"What does Ad mean next to a Google result?",hint:"A) The best result  B) A paid advertisement  C) An official government result  D) An auto-result"},
          {q:"How fast does Google return search results?",hint:"A) 10 seconds  B) 1 minute  C) About 0.3 seconds  D) 5 seconds"},
        ]
      },
      {
        name:"How YouTube works",
        story:"YouTube is essentially a giant video library run by recommendation robots. You upload a video and YouTube stores it on thousands of servers. Then YouTube's recommendation AI watches what people watch, how long they watch it, what they click next, and uses all of that to decide what video this person should watch next. The goal? Keep you watching as long as possible. When you go down a rabbit hole of videos for 3 hours, you have just been very successfully recommended to.",
        realLife:"YouTube is the world's second largest search engine after Google. More video content is uploaded to YouTube in 24 hours than all Hollywood studios combined produced in the last 10 years.",
        funny:"YouTube's recommendation algorithm is so powerful that you can start watching how to cook pasta and 30 minutes later be watching a documentary about medieval swords from 15th century Europe. Nobody knows how. Not even YouTube. The algorithm is a mystery even to the people who built parts of it.",
        activity:"Watch your YouTube homepage and analyse: How many videos are from channels you never subscribed to? What pattern do you notice in what is recommended? Write 5 observations.",
        quiz:[
          {q:"What is YouTube's recommendation AI trying to do?",hint:"A) Teach you things  B) Keep you watching as long as possible  C) Show most viewed only  D) Show videos in upload order"},
          {q:"YouTube is the world's second largest what after Google?",hint:"Think of what you use it for..."},
          {q:"Where does YouTube store all its videos?",hint:"A) On your phone  B) On creators' computers  C) On thousands of servers  D) On government systems"},
          {q:"What is a recommendation algorithm?",hint:"A) A rule book for uploaders  B) Rules that decide what to show you next  C) A type of video format  D) A comment filter"},
          {q:"True or False: You have to pay to watch most YouTube content.",hint:"Think of your experience..."},
        ]
      },
      {
        name:"How Instagram works",
        story:"Instagram started as a photo-sharing app in 2010. Two founders. Ten weeks to build. Twenty-five thousand users on day one. Within two years, Facebook bought it for 1 billion dollars — even though Instagram had only 13 employees at the time. Today Instagram has AI systems that decide which posts appear in your feed, which ads you see, how to detect inappropriate content, and how to connect strangers who might become friends. What started as nice photos is now a giant AI-powered social platform with 2 billion users.",
        realLife:"Every filter you use on Instagram is a machine learning model someone trained. The Suggested Reels you did not ask for is an AI that predicted you would like it. Even the You're all caught up message was designed by a UX team to make you feel good about your scrolling habits.",
        funny:"Instagram was originally called Burbn and was a check-in app, not a photo app. The founders noticed people only used one feature: sharing photos. So they threw out everything else and rebuilt it as a photo app. This taught every startup founder a valuable lesson: watch what your users actually do, not what they say they will do.",
        activity:"Open Instagram (or think about it). Find 5 things that were clearly designed by a UX team — buttons, flows, messages. For each, answer: why was it designed that way? What user need does it solve?",
        quiz:[
          {q:"When was Instagram founded?",hint:"A) 2005  B) 2010  C) 2015  D) 2020"},
          {q:"How many employees did Instagram have when Facebook bought it for $1 billion?",hint:"A) 1000  B) 500  C) 13  D) 0 — it was automated"},
          {q:"What was Instagram originally called?",hint:"A) PhotoShare  B) Picstagram  C) Burbn  D) Instabook"},
          {q:"What made the founders pivot from Burbn to Instagram?",hint:"A) A school project  B) Users only used one feature: photo sharing  C) A rival app launched  D) An investor demanded it"},
          {q:"What technology decides which posts appear first in your feed?",hint:"A) Founders manually sorting  B) Alphabetical order  C) AI recommendation algorithms  D) Upload time only"},
        ]
      }
    ],
    project:{
      title:"Company Origin Story Research",
      steps:[
        "Pick one company: Zomato, Flipkart, CRED, Paytm, or any you admire",
        "Find: who founded it, what problem it solved, and what year it started",
        "Research what their first version looked like",
        "Identify the biggest challenge they overcame",
        "Present as a storyteller — make it dramatic and engaging in 5 minutes"
      ],
      learn:"Research skills, storytelling, and understanding the startup journey from zero to giant."
    }
  },
  {
    num:6, title:"Introduction to Startups", days:"Days 19–21",
    topics:[
      {
        name:"What is a startup?",
        story:"A startup is a young company trying to solve a big problem in a new way and grow very, very fast. The key word is new. Not just open a shop but completely reimagine how shopping works. Startups are like experimental rockets — most of them do not make it to orbit, but the ones that do change the world. Uber reimagined taxis. Airbnb reimagined hotels. Spotify reimagined music. All were startups once. All were called crazy ideas by people who should have invested.",
        realLife:"BYJU'S started as one teacher named Byju Raveendran teaching students. He filmed his classes. Students shared them. Demand exploded. Today it is India's first edtech unicorn — a startup valued at over 1 billion dollars. Starting small is literally how startups work.",
        funny:"Investors rejected Airbnb early on because they thought strangers sleeping in strangers' homes is a bizarre and dangerous idea. Which is completely reasonable. And also wrong. Sometimes the craziest ideas become the most successful ones. This is both encouraging and terrifying.",
        activity:"Research one Indian startup (Zomato, CRED, Zepto, Dunzo, etc.). Find out: What problem did they solve? How did they start? How big are they now? Present it in 5 bullet points.",
        quiz:[
          {q:"What makes a startup different from a regular business?",hint:"A) More employees  B) Tries to grow very fast solving a new problem  C) Located in Silicon Valley  D) No competition"},
          {q:"A startup valued at over $1 billion is called a what?",hint:"A) Dragon  B) Unicorn  C) Billion-company  D) Mega-corp"},
          {q:"Which Indian startup started with one teacher filming classes?",hint:"A) Zomato  B) Swiggy  C) BYJU'S  D) Paytm"},
          {q:"Airbnb reimagined which industry?",hint:"A) Transport  B) Food delivery  C) Hotels and accommodation  D) Banking"},
          {q:"True or False: Investors always recognise great startup ideas immediately.",hint:"Think of all the companies initially rejected..."},
        ]
      },
      {
        name:"How students can build their own ideas",
        story:"You do not need to be 25 and in Silicon Valley to have a great startup idea. The best ideas come from people who personally experience a problem. You are in school — what annoys you? Remembering homework deadlines? Finding study partners? Knowing what is for lunch? Every one of these is a real problem that a smart, motivated student could start building a solution for today, not someday. The only thing separating an idea from a startup is the decision to start.",
        realLife:"Nick D'Aloisio sold his app Summly to Yahoo for 30 million dollars when he was just 17 years old. Fraser Doherty started SuperJam at age 14 selling jam to supermarkets. Moziah Bridges started a bow tie company at age 9 that made over 700,000 dollars. Age is truly not the barrier. Waiting is.",
        funny:"Most people say I had that idea first about every big company. The difference between having an idea and building a startup is approximately 10,000 hours of work. Ideas are free. Execution is the product.",
        activity:"Complete the Startup Starter Kit: Name one problem you personally face at school. Invent a simple solution. Who else has this problem? What would it cost to build a basic version? Give it a name.",
        quiz:[
          {q:"What is the most important first step to building a startup?",hint:"A) Raising money  B) Getting a team  C) Identifying a real problem  D) Building a website"},
          {q:"At what age did Nick D'Aloisio sell his app Summly?",hint:"A) 14  B) 17  C) 21  D) 25"},
          {q:"True or False: You need to be an adult to start a business.",hint:"Think of our examples..."},
          {q:"What separates an idea from a startup?",hint:"A) Money  B) A famous name  C) Execution and hard work  D) An office"},
          {q:"The best startup ideas come from what?",hint:"A) Reading business books  B) Watching other companies  C) Personally experiencing the problem  D) Random brainstorming"},
        ]
      }
    ],
    project:{
      title:"Startup Problem Hunt",
      steps:[
        "Walk around school or think about your daily routine",
        "List 5 genuine frustrations or inefficiencies you notice",
        "For each: describe what the solution would look like",
        "Pick your favourite problem and name a startup solving it",
        "Pitch it in 60 seconds: problem, solution, who uses it"
      ],
      learn:"Problem identification, entrepreneurial thinking, and concise communication."
    }
  },
  {
    num:7, title:"Basic Money & Business Concepts", days:"Days 22–24",
    topics:[
      {
        name:"What is profit?",
        story:"Profit is what is left after you have paid for everything. Imagine you make lemonade and sell it. You spend 50 rupees on lemons, sugar, and cups. You earn 120 rupees from selling 30 glasses. Your profit is 70 rupees (120 minus 50). Companies think about this at massive scale. If Zomato spends 10 crore running its platform but earns 15 crore from delivery charges and restaurant commissions, the 5 crore left is their profit.",
        realLife:"Many startups run at a loss for years intentionally — spending more than they earn to grow fast. Amazon lost money for almost 10 years while building its platform. Now it is one of the most profitable companies on earth. Growing fast sometimes requires losing money strategically.",
        funny:"My lemonade business had a problem. My little sister kept drinking the inventory before I could sell it. That is not a profit problem — that is a supply chain problem. Which is just a fancy way of saying: my sister ate my profits.",
        activity:"Lemonade Business Simulation: You have 200 rupees to spend. Make a budget for ingredients, cups, and signage. Set a price per glass. Decide how many glasses you will make and sell. Calculate your expected profit. What could go wrong?",
        quiz:[
          {q:"Profit equals Revenue minus what?",hint:"A) Taxes  B) Cost (expenses)  C) Salary  D) Investment"},
          {q:"If you earn Rs 500 and spend Rs 380, what is your profit?",hint:"Simple subtraction!"},
          {q:"Running at a loss means what?",hint:"A) Spending more than you earn  B) Losing your phone  C) Having low profits  D) Paying taxes"},
          {q:"Why did Amazon run at a loss for years?",hint:"A) Bad management  B) Intentionally to grow fast  C) High tax rates  D) No customers"},
          {q:"Which is better: high revenue with high costs, or lower revenue with lower costs?",hint:"Think about what is actually left at the end..."},
        ]
      },
      {
        name:"How apps earn money",
        story:"Here is the thing about free apps — they are not really free. They cost someone something, just not you directly (usually). There are several clever business models. Advertising: apps show you ads and get paid by the advertiser (Instagram, YouTube). Freemium: basic version free, premium features cost money (Spotify, Duolingo). In-app purchases: the app is free but items inside cost money (every mobile game ever). Subscription: pay monthly or yearly (Netflix, Hotstar). Marketplace: charge a percentage of every sale (Amazon, Swiggy).",
        realLife:"YouTube is free to watch. But when you watch an ad, a business paid YouTube money for your attention. You are not the customer — you are the product being delivered to advertisers. This is not a criticism, just how it works. And it works very well.",
        funny:"Mobile games are scientifically engineered to make you want to spend 79 rupees at the exact moment you are most frustrated. The power-up that appears precisely when your character dies for the 10th time is not an accident. Somewhere, a game designer studied human psychology for this exact moment.",
        activity:"Pick 3 apps you use daily. For each one, identify its business model: Ads, Freemium, Subscription, In-app purchase, or Marketplace. If it seems free with no ads, how might it actually earn money?",
        quiz:[
          {q:"What is the freemium business model?",hint:"A) Everything free forever  B) Basic free, advanced features cost money  C) First month free then paid  D) Free for students only"},
          {q:"How does YouTube earn money if watching is free?",hint:"A) Selling merchandise  B) Government grants  C) Advertising  D) Selling your videos"},
          {q:"In-app purchases are most common in which type of app?",hint:"A) Productivity apps  B) News apps  C) Mobile games  D) Calculator apps"},
          {q:"Netflix uses which business model?",hint:"A) Advertising  B) Subscription  C) Marketplace  D) Freemium"},
          {q:"True or False: If an app is free, the company earns no money from it.",hint:"Think carefully..."},
        ]
      }
    ],
    project:{
      title:"Business Model X-Ray",
      steps:[
        "Choose 5 apps with different business models",
        "Identify each one: Ads, Subscription, Freemium, Marketplace, or In-App Purchase",
        "Estimate roughly how much each model might earn per 1 million users",
        "Rank them: which model seems most profitable and why?",
        "Design a hybrid business model for your own app idea"
      ],
      learn:"Business model literacy, financial thinking, and product strategy."
    }
  },
  {
    num:8, title:"Mini Project — Your App Idea", days:"Day 25",
    topics:[
      {
        name:"Design your own app idea",
        story:"This is your moment. You have learned what technology is, how apps work, who builds them, how they earn money, and how real startups began. Now it is your turn. Pick a problem — something that annoys you, something your school needs, something your community is missing. Now design the solution. Give it a name, describe what it does, draw the main screen, explain who will use it, and figure out how it will make money. This is exactly what every startup founder does on day one.",
        realLife:"The process you are about to follow is the same one used by founders of billion-dollar companies. The main difference is they kept going after day one. You can too.",
        funny:"Every app idea sounds ridiculous to someone when first described. A website where strangers share their homes — Airbnb. A social network but only for universities — Facebook. Your idea might sound weird too. That might be a very good sign.",
        activity:"Complete the full App Idea Canvas: 1) App name  2) The problem it solves  3) How it solves it  4) Main 3 features  5) Who will use it  6) Business model  7) Draw the home screen  8) Deliver your 30-second pitch.",
        quiz:[
          {q:"What is the most important starting point of any app idea?",hint:"A) The logo  B) The name  C) A real problem worth solving  D) The funding"},
          {q:"A 30-second pitch describes what?",hint:"A) A sports match  B) A quick explanation of your idea and why it matters  C) A cricket delivery  D) A design mockup"},
          {q:"What is a target user?",hint:"A) The company founder  B) The developer  C) The specific type of person your app is designed for  D) An investor"},
          {q:"Why should you define a business model before building?",hint:"A) Investors require it  B) To understand how the app will survive financially  C) For the logo design  D) Not important at first"},
          {q:"What does an App Canvas include?",hint:"A) Only name and logo  B) Problem, solution, features, users, business model  C) Only technical architecture  D) Marketing plan only"},
        ]
      }
    ],
    project:{
      title:"The App Idea — Full Canvas & Pitch",
      steps:[
        "Complete the App Idea Canvas (all 8 sections listed in the activity above)",
        "Sketch the home screen of your app on paper — keep it simple and clear",
        "Write a 30-second pitch: Problem, Solution, Who uses it, How it makes money",
        "Present your pitch to the class in Dragon's Den format",
        "Receive feedback from classmates and the teacher — improve one thing"
      ],
      learn:"Combining all 8 modules: technology, design thinking, company roles, product stages, business models, and startup mindset — all in one creative project."
    }
  }
];

fs.writeFileSync('tech_world_data.json', JSON.stringify(modules, null, 2));
