#list of skill search in resume
SKILLS_DB = [
    "python","django","flask","pandas","java","sql","javascript","react","aws","docker","kubernetes","git","linux","c++","c#","ruby","php","html","css","good communication skills","sales","negotiation","project management","team leadership","problem-solving","critical thinking","time management","adaptability","creativity","data analysis","machine learning","deep learning","natural language processing","springboot","hibernate","angular","vue.js","node.js","express.js","typescript","graphql","restful APIs","microservices","devops","agile methodologies","scrum","kanban","test-driven development (TDD)","continuous integration/continuous deployment (CI/CD)","version control (Git)","cloud computing (AWS, Azure, GCP)","containerization (Docker, Kubernetes)","big data technologies (Hadoop, Spark)","data visualization (Tableau, Power BI)","cybersecurity fundamentals","c","c++","c#","ruby","php","mongodb","tableau","power bi","hadoop","spark","pearl","scala","go","rust","swift","kotlin","objective-c","matlab","sas","stata","excel","powerpoint","MS-word"
]      
def extract_skills(text):
    words = set(text.split())  #split text into words and convert to set for faster checking
    found_skills = []
    #LOOP THROUGH PREDEFINED SKILLS
    for skill in SKILLS_DB:
       if len(skill) == 1:
           continue
       skill_words = skill.split() #split multiword skill 
       if all(word in words for word in skill_words): #check if all words of skill are in text
            found_skills.append(skill)
    return found_skills
