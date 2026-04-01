from django.shortcuts import render
from .resume_parser import extract_text
from .skills import extract_skills
from .roles import predict_role , ROLE_SKILLS
from .sections import section_identification 


# Create your views here.
def home(request):        #when homepage opens runs this function and request is passed to it
    return render(request, 'index.html')  #show index.html page to user
def analyze(request):
    if request.method == 'POST':
        file = request.FILES['resume']     #get file 
        text = extract_text(file)           #extract files 
        skills = extract_skills(text)       #extract text
        role = predict_role(skills)  #predict role based on skills
        required_skills = ROLE_SKILLS.get(role, [])   #required skill 

        sections = section_identification(text)  #identify sections in the resume
        #ATS Score logic
    
        matched = 0
        for skill in required_skills:
            if skill in skills:
                matched += 1
        if len(required_skills) > 0:
            score = int((matched/len(required_skills))*100)
        else:
            score = 0
        
        #section penalties
        if not sections["contact"]:
            score -= 10
        if not sections["education" or "academic"]:
            score -= 10
        if not sections[ "projects" or "intership" or "experience"]:
            score -= 10
        if score < 20:
            score = 20
        
       #missing skill logic  
        missing = []
        for skill in required_skills:
            if skill  not in skills:
                missing.append(skill)
        #dynamic  suggestion 
        improvement = []
        if len(skills) <3:
            missing.append("add more skills")
        if "project" or "internship" not in text:
            improvement.append("Add some project or internship")
        else:
             if score <= 50:
              improvement.append("Your resume needs significant changes")
             elif score > 50 and score <= 80:
               improvement.append("Your resume is good but can be improved")
             else:
               improvement.append("Your resume is excellent!")
        return render(request, 'result.html', {
            'score': score,
            'role': role,
            'skills': skills,
            'missing': missing,
            'improvement': improvement,
            
        })