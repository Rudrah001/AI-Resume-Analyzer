from nlp_module.preprocess import pre_process
from nlp_module.skills import get_skill_report, extract_skills
from nlp_module.education import get_education_report
from nlp_module.similarity import tfidf_similarity, sbert_similarity
from nlp_module.experience import extract_experience_section, extract_project_section, remove_dates

WEIGHTS = {
    'skills': 0.5,
    'education': 0.3,
    'similarity': 0.2,
    'sbert_weight': 0.7,
    'tfidf_weight': 0.3,
}

def build_resume_context(resume_text):

    try:
        skills_set = extract_skills(resume_text)
        skills_text = ' '.join(skills_set)
        
        exp_section = remove_dates(extract_experience_section(resume_text))
        proj_section = remove_dates(extract_project_section(resume_text))
        
        context = f'{exp_section} {proj_section} {skills_text}'
        return context.strip()
    
    except Exception as e:
        print(f"Warning: Error building resume context - {e}")
        return resume_text 


def calculate_similarity_score(resume_context, jd_text):

    try:
        cleaned_resume = pre_process(resume_context)
        cleaned_jd = pre_process(jd_text)
        
        tfidf_score = float(tfidf_similarity(cleaned_resume, cleaned_jd))
        sbert_score = float(sbert_similarity(resume_context, jd_text))
        
        combined = float(
            WEIGHTS['sbert_weight'] * sbert_score +
            WEIGHTS['tfidf_weight'] * tfidf_score
        )
        
        return {
            'combined': round(combined, 2),
            'sbert': round(sbert_score,2),
            'tfidf': round(tfidf_score,2),
        }
    
    except Exception as e:
        print(f"Warning: Similarity calculation failed - {e}")
        return {'combined': 0, 'sbert': 0, 'tfidf': 0, 'error': str(e)}


def analyze_resume(resume_text, jd_text):

    if not resume_text or not jd_text:
        return {
            'error': 'Empty resume or JD text provided',
            'final_score': 0,
        }
    
    try:
        skill_report = get_skill_report(resume_text, jd_text)
        
        education_report = get_education_report(resume_text, jd_text)
        
        resume_context = build_resume_context(resume_text)
        similarity_scores = calculate_similarity_score(resume_context, jd_text)
        
        final_score = float(
            WEIGHTS['skills'] * skill_report['Score'] +
            WEIGHTS['education'] * education_report['Score'] +
            WEIGHTS['similarity'] * similarity_scores['combined']
        )
        
        return {
            'final_score': round(final_score, 2),
            
            'skill_score': skill_report['Score'],
            'education_score': education_report['Score'],
            'similarity_score': similarity_scores['combined'],
            
            'skill_details': skill_report['Details'],
            'education_details': education_report['Details'],
            'similarity_details': {
                'sbert': similarity_scores['sbert'],
                'tfidf': similarity_scores['tfidf'],
            },
            
            # 'weights': WEIGHTS,
            
            # 'resume_processed': resume_context[:500] + '...' if len(resume_context) > 500 else resume_context,
        }
    
    except Exception as e:
        return {
            'error': f'Analysis failed: {str(e)}',
            'final_score': 0,
        }