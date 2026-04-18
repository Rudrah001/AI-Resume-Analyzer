# from preprocess import preprocess
# from similarity import calculate_similarity

# resume = "I have experience in Python, SQL, and machine learning."
# jd = "Looking for a candidate with Python and machine learnin experience."

# resume_cleaned = preprocess(resume)
# jd_cleaned = preprocess(jd)

# score = calculate_similarity(resume_cleaned,jd_cleaned)
# print(score)
# # print(cleaned)

# from skills import extract_skills, match_score, match_skills

# resume = 'I have experience in Python, SQL, c++ and Machine Learning, kubernetes'
# jd = 'Looking for a candidate with Python, Java and ML experience'

# resume_skills, jd_skills, matched, missing, extra = match_skills(resume,jd)
# print('resume_skills', resume_skills)
# print('jd_skills', jd_skills)
# print('matched_skills', matched)
# print('missing_skills', missing)
# print('extra_skills', extra)

# score = match_score(matched,jd_skills)
# print(score)

# from education import education_score, extract_education_section

resume = '''AMAN CHAUHAN 
New Delhi, India | +91-7291888152 | i.am.aman5204@gmail.com | linkedin.com/in/aman-chauhan05 
PROFESSIONAL SUMMARY 
Data Analyst with 2.5+ years of experience in data analysis, dashboard development and reporting automation. Skilled in 
collecting and transforming raw data into actionable business insights through data storytelling and advanced analytics. 
Experienced in performing trend, variance, and root cause analysis, and building automated reporting solutions that improve 
efficiency and support data-driven decision-making for stakeholders. Strong in stakeholder management, data governance and 
process optimization. 
SKILLS & SPECIALIZATION  - - - - 
Tools: SQL, Python, BigQuery, Advanced Excel, Power Automate, Power BI, Google Looker Studio, Tableau. 
Data Analysis & Reporting: KPI Tracking, Variance Analysis, Trend Analysis, Root Cause Analysis, Ad-hoc Analysis. 
Data Governance & Automation: Data Validation, Data Accuracy & Integrity, Data Documentation, Data Security & 
Confidentiality, Reporting Automation, Process Optimization, Workflow Automation. 
Stakeholder & Business Collaboration: Stakeholder Management, Requirement Gathering, Cross-functional Collaboration and 
Business Communication. 
WORK EXPERIENCE 
Data Analyst | Admiral Solutions, Gurugram - 
Oct 2023 – Present 
Developed and delivered automated business reports and executive dashboards using SQL, BigQuery, Excel, and Power BI for 
leadership decision-making. - - - - - - - 
Collected, validated, and integrated data from multiple sources (SQL, Big Query, Excel), ensuring data accuracy, integrity, and 
consistency across reporting systems. 
Performed trend, variance, performance and root cause analysis to identify anomalies, improvement opportunities, and provided 
actionable insights to optimize underperforming areas. 
Built interactive dashboards in Power BI and Looker Studio to track KPIs, performance, and growth across teams. 
Automated reporting workflows using Power Automate and Excel, reducing manual effort. 
Standardized reporting processes, creating a scalable and centralized reporting framework and delivered ad-hoc analysis and 
insights to cross-functional stakeholders within tight timelines. 
Customer Support Executive | Concentrix & Teleperformance, Gurugram 
Apr 2021 – Sep 2023 
Dispute Handler (Concentrix): Handled financial, banking, and cryptocurrency-related customer queries for Coinbase and Chime at 
Concentrix, efficiently resolving disputes for US customers through email and chat support. 
Customer Sales Executive (Teleperformance): Executed outbound sales calls for RBL Bank at Teleperformance, selling instant cash 
loan products against credit cards and closing deals with eligible customers. 
PROJECTS & KEY ACHIEVEMENTS - - - - 
Customer Feedback Analytics Project: Analyzed customer feedback to identify key trends, segments, and customer sentiments, 
developed an interactive Looker Studio dashboard to visualize insights with automation and track performance with actionable insights 
to support management decision-making and improve customer experience. 
Customer Retention Analysis Project: Analysed retention data to identify trends and behaviour patterns, conducted root cause 
analysis to uncover key drivers of churn and retention. delivered insights to support strategies for improving retention and business 
performance. 
Monthly Performance Analysis Project: Analyzed Monthly Top & bottom performers, find trends & gaps in departments, and 
stakeholders in Process Optimization. 
Reward & Recognition: Led team to 1st place in BI Hackathon - shared analysis & trends over company performances & metrics 
with automated daily performance tracking. Awarded with multiple title - Shining Star, Stakeholder Champion & Best Appreciation 
for delivery excellence and stakeholder impact. 
EDUCATION - - 
Data Science Certification - UpGrad | 2023 
B.A. in Economics - Delhi University | 2020 | Self-driven transition into data analytics via structured certification and industry projects.
'''

jd = '''Job Title: Data Analyst
Company: Nexora Analytics

About the Role:
We are looking for an experienced Data Analyst to join our Business Intelligence team. 
The ideal candidate has hands-on experience in data analysis, dashboard development, 
and reporting automation, and can translate complex data into clear, actionable insights 
for stakeholders across the organization.

Responsibilities:
- Design and maintain interactive dashboards and reports using Power BI, Looker Studio, 
  or Tableau to track KPIs and business performance
- Write and optimize SQL queries to extract, transform, and analyze large datasets from 
  BigQuery or similar data warehouses
- Perform trend analysis, variance analysis, and root cause analysis to identify 
  anomalies and business opportunities
- Automate recurring reports and workflows using Power Automate or Python to reduce 
  manual effort and improve efficiency
- Collaborate with cross-functional stakeholders to gather requirements and deliver 
  ad-hoc analysis within tight timelines
- Ensure data accuracy, integrity, and consistency across reporting systems through 
  proper data validation and governance practices

Requirements:
- 2+ years of experience in data analysis or business intelligence role
- Proficiency in SQL and experience with cloud data platforms such as BigQuery
- Hands-on experience with BI tools — Power BI, Looker Studio, or Tableau
- Strong working knowledge of Advanced Excel including pivot tables and automation
- Experience with reporting automation using Power Automate or similar tools
- Familiarity with Python for data analysis using Pandas or NumPy
- Strong communication and stakeholder management skills
- Bachelor's degree in Economics, Statistics, Computer Science, or a related field

Good to Have:
- Experience with data governance, documentation, and data security practices
- Exposure to customer analytics, retention analysis, or feedback analytics
- Experience presenting insights to leadership or executive stakeholders'''

# score,details = education_score(resume,jd)
# print(score,details)

# from analyzer import analyzer
# import time

# t1 = time.time()

# result = analyzer(resume,jd)
# print(result['final_score'])
# print(result['skill_details'])
# print(result['education_details'])
# print(result['sim'])

# t2 = time.time()
# print(t2-t1)

# from experience import extract_experience_section, extract_project_section, remove_dates
# from skills import extract_skills
# from similarity import sbert_similarity

# pro = extract_project_section(resume)
# exp = extract_experience_section(resume)
# print(remove_dates(exp))

# sk = extract_skills(resume)
# sk = ' '.join(sk)
# com = f"{sk} {exp} {pro}"
# print(remove_dates(com))

# score = sbert_similarity(resume,jd)
# print(score)

from nlp_module.analyzer import analyze_resume
import time
t1 = time.time()

analyze = analyze_resume(resume,jd)
print(analyze['final_score'],analyze['similarity_score'],analyze['similarity_details'],analyze['skill_score'],analyze['education_score'])
print(analyze['skill_details'])
print(analyze['education_details'])
print(time.time()-t1)