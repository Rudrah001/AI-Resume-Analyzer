from nlp_module.education_library import DEGREE_LEVELS, FIELD_KEYWORDS, FIELD_GROUPS, ADJACENT_GROUPS, DEGREE_HIERARCHY
import re

def extract_education_section(resume_text):
    pattern = r'^[\s]*(education|academic|qualification)[:\s]*\n+([\s\S]*?)(?=^[\s]*(experience|skills|technical skills|projects|certifications?)[:\s]*$|\Z)'    
    match = re.search(pattern,resume_text,re.IGNORECASE|re.DOTALL|re.MULTILINE)
    if match:
        return match.group(2)
    return resume_text

def extract_degree(text):
    text = text.lower()
    for degree,aliases in DEGREE_LEVELS.items():
        for alias in aliases:
            pattern = r'\b'+re.escape(alias.lower())+r'\b'
            if re.search(pattern, text):
                return degree
    
    return None

def extract_field(text):
    text = text.lower()
    for field,aliases in FIELD_KEYWORDS.items():
        for alias in aliases:
            pattern = r'\b'+re.escape(alias.lower())+r'\b'
            if re.search(pattern,text):
                return field
            
    return None

def get_field_group(field):
    if field is None:
        return None
    for group,aliases in FIELD_GROUPS.items():
        if field in aliases:
            return group
    return None

def get_field_score(resume_field, jd_field):
    if resume_field is None and jd_field is None:
        return 100
    
    if jd_field is None:
        return 100
    
    if resume_field is None:
        return 50
    
    if resume_field == jd_field:
        return 100
    
    resume_group = get_field_group(resume_field)
    jd_group = get_field_group(jd_field)

    if resume_group and jd_group and resume_group == jd_group:
        return 75
    
    if resume_group and jd_group:
        adjacent = ADJACENT_GROUPS.get(jd_group,[])
        if resume_group in adjacent:
            return 40
        
    return 15

def education_score(resume_text, jd_text):
    if not resume_text and not jd_text:
        return 0, {'reason':'empty string'}
    
    education_section = extract_education_section(resume_text)

    resume_degree = extract_degree(education_section)
    jd_degree = extract_degree(jd_text)
    resume_field = extract_field(education_section)
    jd_field = extract_field(jd_text)

    if jd_degree is None:
        return 100, {
            "reason"        : "No education requirement specified in JD",
            "resume_degree" : resume_degree,
            "resume_field"  : resume_field,
            "jd_degree"     : None,
            "jd_field"      : None,
        }
 
    if resume_degree is None:
        return 50, {
            "reason"        : "Could not determine education from resume",
            "resume_degree" : None,
            "resume_field"  : resume_field,
            "jd_degree"     : jd_degree,
            "jd_field"      : jd_field,
        }
    
    resume_level = DEGREE_HIERARCHY.get(resume_degree,0)
    jd_level = DEGREE_HIERARCHY.get(jd_degree,0)

    if resume_level>=jd_level:
        degree_score = 100
    else:
        degree_score = round((resume_level/jd_level)*100,2)

    field_score = get_field_score(resume_field,jd_field)

    final_score = round((0.7*degree_score) + (0.3*field_score),2)

    return final_score, {
        "resume_degree" : resume_degree,
        "jd_degree"     : jd_degree,
        "resume_field"  : resume_field,
        "jd_field"      : jd_field,
        "degree_score"  : degree_score,
        "field_score"   : field_score,
    }

def get_education_report(resume_text, jd_text):
    #Master Function

    score,details = education_score(resume_text, jd_text)

    return {
        'Score' : score,
        'Details' : details
    }