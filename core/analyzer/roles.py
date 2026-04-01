ROLE_SKILLS = {
    "Backend Developer": ["java","python","django","springboot","sql"],
    "Frontend Developer": ["html","css","react","javascript"],
    "Full Stack Developer":["html","css","javascript","python","java","node.js"],  
    "Data Scientist / Analyst":["python","pandas","machine learning","data analyst","sql","mongodb"],
    "Mobile App Developer":["kotlin","java","swift"],
    "DevOps Engineer":["aws","docker","kubernetes","devops","ci/cd"],
    "Software Engineer":["c#","java","python","php","sql"], 
    "Buisness Management Role":["project managemanet","good communication skill","team leadership","negotiation","sales","time management"]                   
}
def predict_role(skills):
    skills = set(skills)   #faster checking
    #Full stack developer 
    if ({"html","css","javascript"} & skills) and ({"python","django","node.js"} & skills):
        return "Full Stack Developer"
   
    #backend developer 
    elif len({"python","django","java","springboot","node.js"} & skills) >= 2:
        return "Backend Developer"
    
    #frontend developer
    elif len({"html","css","javascript","react","angular","vue.js"} & skills) >= 2:
        return "Frontend Developer"
    
    
    #Data scientist / Analyst
    elif len({"python","pandas","machine learning","data analyst","sql","mongodb"} & skills) >= 2:
            return "Data Scientist / Analyst"
    #mobile apps developer 
    elif len({"kotlin","java","swift"} & skills) >= 2:
        return "Mobile App Developer"
    #Devops engineer
    elif len({"aws","docker","kubernets","devops","ci/cd"} & skills) >= 2:
        return "DevOps Engineer"
    #software engineer
    elif len({"c","c++","c#","java","python","php","sql"} & skills) >= 2:
        return "Software Engineer"
    #buisness management role 
    elif len({"project managemanet","good communication skill","team leadership","negotiation","sales"} & skills) >= 2:
        return "Buisness Management Role"
    else:
        return " "
