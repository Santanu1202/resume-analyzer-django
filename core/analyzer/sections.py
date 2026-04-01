def section_identification(text):
    section ={
        "contact": False,
        "education" or "academic": False,
        "projects" or "intership" or "experience": False,
        

    }
    #contact detection 
    if "email" in text or "phone no" or "contact no" in text:
        section["contact"] = True
    #eduction detection
    if "education" or "academic" in text:
        section["education" or "academic"] = True
    
    #internship detection
    if "projects" or "intership" or "experience" in text:
        section["project" or "intership" or "experience"] = True
    return section