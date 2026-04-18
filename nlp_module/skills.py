from nlp_module.skill_library import SKILL_LIBRARY
import re

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for canonical,aliases in SKILL_LIBRARY.items():
        for alias in aliases:
            pattern = r'(?<!\w)' + re.escape(alias.lower()) + r'(?!\w)'
            if re.search(pattern,text):
                found_skills.add(canonical)
                break
        
    return found_skills

def match_skills(resume_raw,jd_raw):
    resume_skills = extract_skills(resume_raw)
    jd_skills = extract_skills(jd_raw)

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills
    extra = resume_skills - jd_skills

    return resume_skills, jd_skills, matched, missing, extra

def match_score(matched, jd_skills):
    if len(jd_skills) == 0:
        return 100
    
    score = (len(matched)/len(jd_skills)) * 100
    return round(score,2)

def get_skill_report(resume_raw,jd_raw):
    #Master Function

    resume_skills, jd_skills, matched, missing, extra = match_skills(resume_raw,jd_raw)
    score = match_score(matched,jd_skills)

    return {
        'Score' : score,
        'Details' : {
            'Resume_skills' : list(resume_skills),
            'Jd_skills' : list(jd_skills),
            'Matched_skills' : list(matched),
            'Missing_skills' : list(missing),
            'Extra_skills' : list(extra)
        }
    }