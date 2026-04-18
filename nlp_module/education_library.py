# =============================================================================
# EDUCATION LIBRARY FOR RESUME ANALYZER
# Contains: Degree levels and Field of study keywords
# Usage: from education_library import DEGREE_LEVELS, DEGREE_HIERARCHY, FIELD_KEYWORDS
# =============================================================================


# -----------------------------------------------------------------------------
# DEGREE LEVELS
# Each degree maps to a list of aliases/shortforms found in resumes and JDs
# -----------------------------------------------------------------------------

DEGREE_LEVELS = {
    "phd": [
        "phd", "ph.d", "ph.d.", "doctorate", "doctoral",
        "doctor of philosophy", "d.phil", "dphill"
    ],
    "masters": [
        "master", "masters", "master's",
        "msc", "m.sc", "m.sc.",
        "mtech", "m.tech", "m.tech.",
        "mba", "m.b.a",
        "me", "m.e", "m.e.",
        "mca", "m.c.a",
        "mphil", "m.phil",
        "ma", "m.a", "m.a.",
        "mcom", "m.com",
        "llm", "l.l.m",
        "postgraduate", "post graduate", "pg",
        "masters degree", "master degree"
    ],
    "bachelors": [
        "bachelor", "bachelors", "bachelor's",
        "btech", "b.tech", "b.tech.",
        "bsc", "b.sc", "b.sc.",
        "be", "b.e", "b.e.",
        "bca", "b.c.a",
        "bba", "b.b.a",
        "bcom", "b.com",
        "ba", "b.a", "b.a.",
        "bfa", "b.f.a",
        "llb", "l.l.b",
        "mbbs", "m.b.b.s",
        "bds", "b.d.s",
        "bpharm", "b.pharm", "b.pharmacy",
        "undergraduate", "under graduate", "ug",
        "bachelors degree", "bachelor degree",
        "four year degree", "4 year degree"
    ],
    "graduate": [
        "graduate", "bachelor"
    ],
    "diploma": [
        "diploma", "polytechnic", "poly",
        "advanced diploma", "post diploma",
        "pgdm", "p.g.d.m",
        "pgdca", "p.g.d.c.a",
        "certificate course", "certification course"
    ],
    "highschool": [
        "high school", "highschool",
        "12th", "12 th", "class 12",
        "hsc", "h.s.c",
        "intermediate", "inter",
        "10+2", "plus two",
        "senior secondary", "higher secondary",
        "a levels", "a-levels"
    ],
}


# -----------------------------------------------------------------------------
# DEGREE HIERARCHY
# Higher number = higher qualification
# Used to compare resume degree vs JD requirement
# -----------------------------------------------------------------------------

DEGREE_HIERARCHY = {
    "phd"        : 4,
    "masters"    : 3,
    "bachelors"  : 2,
    "diploma"    : 1,
    "highschool" : 0,
}


# -----------------------------------------------------------------------------
# FIELD OF STUDY KEYWORDS
# Covers all major academic disciplines
# -----------------------------------------------------------------------------

FIELD_KEYWORDS = {

    # --- COMPUTER SCIENCE & IT ---
    "computer science": [
        "computer science", "cse", "cs",
        "computing", "computer engineering",
        "b.tech cse", "btech cse", "bsc cs"
    ],
    "computer applications": [
        "computer applications", "bca", "mca",
        "application software"
    ],
    "information technology": [
        "information technology", "it",
        "information systems", "information science",
        "it engineering"
    ],
    "software engineering": [
        "software engineering", "software development",
        "software technology"
    ],
    "data science": [
        "data science", "data analytics",
        "big data", "data engineering",
        "business analytics", "business intelligence"
    ],
    "artificial intelligence": [
        "artificial intelligence", "ai",
        "machine learning", "ml",
        "ai and ml", "ai & ml",
        "intelligent systems"
    ],
    "cybersecurity": [
        "cybersecurity", "cyber security",
        "information security", "network security",
        "ethical hacking"
    ],

    # --- ELECTRONICS & ELECTRICAL ---
    "electronics": [
        "electronics", "ece",
        "electronics and communication",
        "electronics & communication",
        "embedded systems", "vlsi"
    ],
    "electrical engineering": [
        "electrical engineering", "eee",
        "electrical and electronics",
        "electrical & electronics",
        "power systems", "electrical"
    ],
    "instrumentation": [
        "instrumentation", "instrumentation engineering",
        "instrumentation and control"
    ],
    "telecommunications": [
        "telecommunications", "telecom",
        "communication engineering",
        "wireless communication"
    ],

    # --- MECHANICAL & CIVIL ---
    "mechanical engineering": [
        "mechanical engineering", "mechanical", "mech",
        "manufacturing engineering",
        "production engineering",
        "industrial engineering",
        "automobile engineering"
    ],
    "civil engineering": [
        "civil engineering", "civil",
        "structural engineering",
        "construction engineering",
        "environmental engineering"
    ],
    "aerospace engineering": [
        "aerospace engineering", "aerospace",
        "aeronautical engineering", "aeronautical",
        "avionics"
    ],
    "chemical engineering": [
        "chemical engineering", "chemical",
        "petrochemical engineering",
        "process engineering"
    ],

    # --- MATHEMATICS & STATISTICS ---
    "mathematics": [
        "mathematics", "maths", "math",
        "applied mathematics", "pure mathematics",
        "mathematical sciences"
    ],
    "statistics": [
        "statistics", "stats",
        "applied statistics",
        "statistical computing"
    ],
    "physics": [
        "physics", "applied physics",
        "engineering physics"
    ],

    # --- BUSINESS & MANAGEMENT ---
    "business administration": [
        "business administration", "bba", "mba",
        "business management", "general management",
        "corporate management"
    ],
    "finance": [
        "finance", "financial management",
        "banking and finance", "banking & finance",
        "investment management", "financial services"
    ],
    "accounting": [
        "accounting", "accountancy",
        "chartered accountancy", "ca",
        "cost accounting", "financial accounting",
        "cpa", "acca"
    ],
    "marketing": [
        "marketing", "marketing management",
        "digital marketing", "sales and marketing",
        "sales & marketing", "brand management"
    ],
    "human resources": [
        "human resources", "hr",
        "human resource management", "hrm",
        "people management", "talent management",
        "organizational behavior"
    ],
    "operations management": [
        "operations management", "operations",
        "supply chain management", "supply chain",
        "logistics management", "logistics",
        "operations research"
    ],
    "entrepreneurship": [
        "entrepreneurship", "startup management",
        "venture management", "innovation management"
    ],

    # --- ECONOMICS ---
    "economics": [
        "economics", "eco",
        "applied economics", "econometrics",
        "development economics", "business economics"
    ],

    # --- LAW ---
    "law": [
        "law", "llb", "llm",
        "legal studies", "jurisprudence",
        "corporate law", "criminal law",
        "international law", "cyber law"
    ],

    # --- MEDICINE & HEALTHCARE ---
    "medicine": [
        "medicine", "mbbs", "medical",
        "general medicine", "clinical medicine"
    ],
    "nursing": [
        "nursing", "bsc nursing",
        "general nursing", "clinical nursing"
    ],
    "pharmacy": [
        "pharmacy", "pharmaceutical sciences",
        "pharmacology", "b.pharm", "m.pharm",
        "clinical pharmacy"
    ],
    "dentistry": [
        "dentistry", "dental science",
        "bds", "oral health"
    ],
    "public health": [
        "public health", "community health",
        "health management", "epidemiology",
        "health informatics"
    ],
    "biotechnology": [
        "biotechnology", "biotech",
        "bioinformatics", "biomedical engineering",
        "biomedical", "life sciences",
        "microbiology", "biochemistry",
        "molecular biology", "genetics"
    ],

    # --- DESIGN & ARTS ---
    "design": [
        "design", "graphic design",
        "ui design", "ux design", "ui/ux",
        "product design", "industrial design",
        "visual design", "interaction design"
    ],
    "fine arts": [
        "fine arts", "bfa", "visual arts",
        "applied arts", "creative arts",
        "animation", "multimedia"
    ],
    "architecture": [
        "architecture", "b.arch", "m.arch",
        "urban planning", "interior design",
        "landscape architecture"
    ],

    # --- HUMANITIES & SOCIAL SCIENCES ---
    "psychology": [
        "psychology", "applied psychology",
        "clinical psychology", "organizational psychology",
        "behavioral science"
    ],
    "sociology": [
        "sociology", "social science",
        "social work", "anthropology"
    ],
    "english": [
        "english", "english literature",
        "english language", "linguistics",
        "communication studies", "journalism",
        "mass communication", "media studies"
    ],
    "history": [
        "history", "ancient history",
        "modern history", "historical studies"
    ],
    "political science": [
        "political science", "political studies",
        "public administration", "international relations",
        "governance"
    ],
    "geography": [
        "geography", "geospatial science",
        "gis", "remote sensing",
        "environmental science"
    ],

    # --- EDUCATION ---
    "education": [
        "education", "b.ed", "m.ed",
        "teaching", "pedagogy",
        "educational technology",
        "curriculum development"
    ],

    # --- HOSPITALITY & TOURISM ---
    "hospitality": [
        "hospitality", "hotel management",
        "hospitality management",
        "food and beverage", "catering"
    ],
    "tourism": [
        "tourism", "travel and tourism",
        "tourism management"
    ],

    # --- AGRICULTURE ---
    "agriculture": [
        "agriculture", "agricultural science",
        "agronomy", "horticulture",
        "food technology", "food science",
        "dairy technology"
    ],
}


# =============================================================================
# FIELD GROUPS
# Fields that belong to the same family/domain
# Used to determine how related two different fields are
# =============================================================================

FIELD_GROUPS = {
    "tech": [
        "computer science", "information technology",
        "software engineering", "data science",
        "artificial intelligence", "computer applications",
        "electronics", "electrical engineering",
        "telecommunications", "cybersecurity",
    ],
    "engineering": [
        "mechanical engineering", "civil engineering",
        "aerospace engineering", "chemical engineering",
        "instrumentation",
    ],
    "science": [
        "mathematics", "statistics", "physics",
        "biotechnology",
    ],
    "business": [
        "business administration", "finance",
        "accounting", "marketing",
        "human resources", "operations management",
        "economics", "entrepreneurship",
    ],
    "medicine": [
        "medicine", "nursing", "pharmacy",
        "dentistry", "public health",
    ],
    "humanities": [
        "english", "history", "political science",
        "sociology", "geography", "psychology",
        "education",
    ],
    "design": [
        "design", "fine arts", "architecture",
    ],
    "hospitality": [
        "hospitality", "tourism", "agriculture",
    ],
    "law": [
        "law",
    ],
}


# =============================================================================
# ADJACENT GROUPS
# Groups that partially overlap or are related to each other
# Used to give partial credit for related but not same domain fields
# =============================================================================

ADJACENT_GROUPS = {
    "tech"        : ["engineering", "science"],
    "engineering" : ["tech", "science"],
    "science"     : ["tech", "engineering", "medicine"],
    "business"    : ["law", "humanities"],
    "medicine"    : ["science"],
    "humanities"  : ["business", "law"],
    "design"      : ["tech", "humanities"],
    "law"         : ["business", "humanities"],
    "hospitality" : ["business"],
}


# =============================================================================
# QUICK STATS
# =============================================================================

if __name__ == "__main__":
    total_degrees = len(DEGREE_LEVELS)
    total_degree_aliases = sum(len(v) for v in DEGREE_LEVELS.values())
    total_fields = len(FIELD_KEYWORDS)
    total_field_aliases = sum(len(v) for v in FIELD_KEYWORDS.values())

    print(f"Degree levels        : {total_degrees}")
    print(f"Degree aliases       : {total_degree_aliases}")
    print(f"Field categories     : {total_fields}")
    print(f"Field aliases        : {total_field_aliases}")