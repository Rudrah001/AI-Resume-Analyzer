# =============================================================================
# SKILL LIBRARY FOR RESUME ANALYZER
# Covers: Tech, Data Science, ML/AI, Cloud, DevOps, Databases, Soft Skills
# Structure: { canonical_name : [alias1, alias2, ...] }
# Usage: from skill_library import SKILL_LIBRARY
# =============================================================================

SKILL_LIBRARY = {

    # -------------------------------------------------------------------------
    # PROGRAMMING LANGUAGES
    # -------------------------------------------------------------------------
    "python": [
        "python", "python3", "python 3", "py"
    ],
    "javascript": [
        "javascript", "js", "es6", "es2015", "ecmascript", "vanilla js", "vanilla javascript"
    ],
    "typescript": [
        "typescript", "ts"
    ],
    "java": [
        "java", "java 8", "java 11", "java 17", "core java", "advanced java"
    ],
    "c++": [
        "c++", "cpp", "c plus plus"
    ],
    "c": [
        "c programming", "c language"
    ],
    "c#": [
        "c#", "csharp", "c sharp", "dotnet c#"
    ],
    "r": [
        "r programming", "r language", "r studio", "rstudio"
    ],
    "go": [
        "go", "golang", "go language"
    ],
    "rust": [
        "rust", "rust lang", "rust language"
    ],
    "kotlin": [
        "kotlin", "kotlin android"
    ],
    "swift": [
        "swift", "swift ios", "swiftui"
    ],
    "php": [
        "php", "php7", "php8"
    ],
    "ruby": [
        "ruby", "ruby on rails", "ror"
    ],
    "scala": [
        "scala", "scala spark"
    ],
    "perl": [
        "perl"
    ],
    "shell scripting": [
        "shell", "bash", "shell script", "shell scripting", "bash scripting",
        "zsh", "sh scripting"
    ],
    "matlab": [
        "matlab"
    ],

    # -------------------------------------------------------------------------
    # WEB FRONTEND FRAMEWORKS & LIBRARIES
    # -------------------------------------------------------------------------
    "react": [
        "react", "reactjs", "react.js", "react js"
    ],
    "angular": [
        "angular", "angularjs", "angular.js", "angular 2", "angular 14"
    ],
    "vue": [
        "vue", "vuejs", "vue.js", "vue js"
    ],
    "next.js": [
        "next", "nextjs", "next.js", "next js"
    ],
    "html": [
        "html", "html5", "hypertext markup language"
    ],
    "css": [
        "css", "css3", "cascading style sheets"
    ],
    "sass": [
        "sass", "scss"
    ],
    "tailwind css": [
        "tailwind", "tailwindcss", "tailwind css"
    ],
    "bootstrap": [
        "bootstrap", "bootstrap 4", "bootstrap 5"
    ],
    "jquery": [
        "jquery"
    ],
    "redux": [
        "redux", "redux toolkit", "react redux"
    ],

    # -------------------------------------------------------------------------
    # WEB BACKEND FRAMEWORKS
    # -------------------------------------------------------------------------
    "django": [
        "django", "django rest", "django rest framework", "drf"
    ],
    "flask": [
        "flask", "flask api", "flask python"
    ],
    "fastapi": [
        "fastapi", "fast api"
    ],
    "express": [
        "express", "expressjs", "express.js", "express js"
    ],
    "node.js": [
        "node", "nodejs", "node.js", "node js"
    ],
    "spring boot": [
        "spring", "spring boot", "spring framework", "spring mvc"
    ],
    "asp.net": [
        "asp.net", "aspnet", "asp net", ".net", "dotnet"
    ],
    "laravel": [
        "laravel"
    ],
    "fastify": [
        "fastify"
    ],

    # -------------------------------------------------------------------------
    # DATABASES — RELATIONAL
    # -------------------------------------------------------------------------
    "sql": [
        "sql", "structured query language"
    ],
    "mysql": [
        "mysql", "my sql"
    ],
    "postgresql": [
        "postgresql", "postgres", "psql", "pg", "postgre"
    ],
    "sqlite": [
        "sqlite", "sqlite3"
    ],
    "microsoft sql server": [
        "sql server", "mssql", "ms sql", "microsoft sql server", "t-sql", "tsql"
    ],
    "oracle database": [
        "oracle", "oracle db", "oracle database", "pl/sql", "plsql"
    ],
    "mariadb": [
        "mariadb", "maria db"
    ],

    # -------------------------------------------------------------------------
    # DATABASES — NOSQL
    # -------------------------------------------------------------------------
    "mongodb": [
        "mongodb", "mongo", "mongo db"
    ],
    "redis": [
        "redis", "redis cache"
    ],
    "cassandra": [
        "cassandra", "apache cassandra"
    ],
    "elasticsearch": [
        "elasticsearch", "elastic search", "elastic", "elk stack"
    ],
    "dynamodb": [
        "dynamodb", "dynamo db", "aws dynamodb"
    ],
    "firebase": [
        "firebase", "firestore", "firebase realtime database"
    ],
    "neo4j": [
        "neo4j", "graph database", "neo4j graph"
    ],
    "couchdb": [
        "couchdb", "couch db"
    ],

    # -------------------------------------------------------------------------
    # CLOUD PLATFORMS
    # -------------------------------------------------------------------------
    "amazon web services": [
        "aws", "amazon web services", "amazon aws"
    ],
    "google cloud platform": [
        "gcp", "google cloud", "google cloud platform"
    ],
    "microsoft azure": [
        "azure", "microsoft azure", "ms azure"
    ],
    "heroku": [
        "heroku"
    ],
    "digitalocean": [
        "digitalocean", "digital ocean"
    ],
    "vercel": [
        "vercel"
    ],
    "netlify": [
        "netlify"
    ],

    # -------------------------------------------------------------------------
    # CLOUD SERVICES (AWS SPECIFIC)
    # -------------------------------------------------------------------------
    "aws lambda": [
        "lambda", "aws lambda", "serverless lambda"
    ],
    "aws s3": [
        "s3", "aws s3", "amazon s3"
    ],
    "aws ec2": [
        "ec2", "aws ec2", "amazon ec2"
    ],
    "aws rds": [
        "rds", "aws rds", "amazon rds"
    ],
    "aws sagemaker": [
        "sagemaker", "aws sagemaker"
    ],

    # -------------------------------------------------------------------------
    # DEVOPS & CI/CD
    # -------------------------------------------------------------------------
    "docker": [
        "docker", "containerization", "containers", "dockerfile"
    ],
    "kubernetes": [
        "kubernetes", "k8s", "kube", "kubectl"
    ],
    "continuous integration": [
        "ci/cd", "ci cd", "cicd", "continuous integration",
        "continuous deployment", "continuous delivery"
    ],
    "jenkins": [
        "jenkins", "jenkins pipeline", "jenkins ci"
    ],
    "github actions": [
        "github actions", "gh actions"
    ],
    "gitlab ci": [
        "gitlab ci", "gitlab pipeline", "gitlab cd"
    ],
    "ansible": [
        "ansible", "ansible playbook"
    ],
    "terraform": [
        "terraform", "terraform iac", "infrastructure as code"
    ],
    "helm": [
        "helm", "helm charts"
    ],
    "prometheus": [
        "prometheus", "prometheus monitoring"
    ],
    "grafana": [
        "grafana", "grafana dashboard"
    ],
    "nginx": [
        "nginx", "nginx server"
    ],
    "apache": [
        "apache", "apache server", "apache http"
    ],

    # -------------------------------------------------------------------------
    # VERSION CONTROL
    # -------------------------------------------------------------------------
    "git": [
        "git", "git version control"
    ],
    "github": [
        "github", "git hub"
    ],
    "gitlab": [
        "gitlab", "git lab"
    ],
    "bitbucket": [
        "bitbucket", "bit bucket"
    ],

    # -------------------------------------------------------------------------
    # DATA SCIENCE & ANALYTICS
    # -------------------------------------------------------------------------
    "machine learning": [
        "machine learning", "ml", "supervised learning",
        "unsupervised learning", "predictive modeling"
    ],
    "deep learning": [
        "deep learning", "dl", "neural networks", "neural network", "nn"
    ],
    "natural language processing": [
        "nlp", "natural language processing", "text mining",
        "text analytics", "computational linguistics"
    ],
    "computer vision": [
        "computer vision", "cv", "image recognition",
        "image processing", "object detection"
    ],
    "data analysis": [
        "data analysis", "data analytics", "data analyst",
        "exploratory data analysis", "eda"
    ],
    "data visualization": [
        "data visualization", "data viz", "dashboarding"
    ],
    "statistics": [
        "statistics", "statistical analysis", "statistical modeling",
        "probability", "inferential statistics", "descriptive statistics"
    ],
    "feature engineering": [
        "feature engineering", "feature selection", "feature extraction"
    ],
    "model deployment": [
        "model deployment", "mlops", "model serving", "model productionization"
    ],
    "time series analysis": [
        "time series", "time series analysis", "forecasting", "arima"
    ],

    # -------------------------------------------------------------------------
    # ML FRAMEWORKS & LIBRARIES
    # -------------------------------------------------------------------------
    "tensorflow": [
        "tensorflow", "tf", "tensorflow 2"
    ],
    "pytorch": [
        "pytorch", "torch", "py torch"
    ],
    "scikit-learn": [
        "scikit-learn", "sklearn", "scikit learn"
    ],
    "keras": [
        "keras"
    ],
    "xgboost": [
        "xgboost", "xgb", "gradient boosting"
    ],
    "lightgbm": [
        "lightgbm", "lgbm", "light gbm"
    ],
    "hugging face": [
        "hugging face", "huggingface", "transformers library"
    ],
    "opencv": [
        "opencv", "open cv", "cv2"
    ],
    "spacy": [
        "spacy", "spaCy"
    ],
    "nltk": [
        "nltk", "natural language toolkit"
    ],

    # -------------------------------------------------------------------------
    # DATA TOOLS & LIBRARIES
    # -------------------------------------------------------------------------
    "pandas": [
        "pandas", "pd"
    ],
    "numpy": [
        "numpy", "np"
    ],
    "matplotlib": [
        "matplotlib", "pyplot"
    ],
    "seaborn": [
        "seaborn", "sns"
    ],
    "plotly": [
        "plotly", "plotly express"
    ],
    "scipy": [
        "scipy"
    ],
    "tableau": [
        "tableau", "tableau desktop", "tableau server"
    ],
    "power bi": [
        "power bi", "powerbi", "microsoft power bi"
    ],
    "excel": [
        "excel", "ms excel", "microsoft excel", "advanced excel", "spreadsheet"
    ],
    "jupyter": [
        "jupyter", "jupyter notebook", "jupyter lab", "ipynb"
    ],

    # -------------------------------------------------------------------------
    # BIG DATA
    # -------------------------------------------------------------------------
    "apache spark": [
        "spark", "apache spark", "pyspark", "spark streaming"
    ],
    "hadoop": [
        "hadoop", "apache hadoop", "hdfs", "mapreduce"
    ],
    "kafka": [
        "kafka", "apache kafka", "kafka streaming"
    ],
    "airflow": [
        "airflow", "apache airflow", "workflow orchestration"
    ],
    "hive": [
        "hive", "apache hive", "hiveql"
    ],
    "dbt": [
        "dbt", "data build tool"
    ],
    "snowflake": [
        "snowflake", "snowflake db"
    ],

    # -------------------------------------------------------------------------
    # APIs & ARCHITECTURE
    # -------------------------------------------------------------------------
    "rest api": [
        "rest", "rest api", "restful", "restful api", "rest apis",
        "restful services", "rest services"
    ],
    "graphql": [
        "graphql", "graph ql"
    ],
    "microservices": [
        "microservices", "micro services", "microservice architecture",
        "service oriented architecture", "soa"
    ],
    "grpc": [
        "grpc", "gRPC", "rpc"
    ],
    "websocket": [
        "websocket", "web socket", "ws"
    ],
    "api design": [
        "api design", "api development", "api integration"
    ],

    # -------------------------------------------------------------------------
    # MOBILE DEVELOPMENT
    # -------------------------------------------------------------------------
    "android development": [
        "android", "android development", "android sdk"
    ],
    "ios development": [
        "ios", "ios development", "xcode"
    ],
    "react native": [
        "react native", "rn", "react-native"
    ],
    "flutter": [
        "flutter", "dart flutter"
    ],

    # -------------------------------------------------------------------------
    # TESTING
    # -------------------------------------------------------------------------
    "unit testing": [
        "unit testing", "unit test", "tdd", "test driven development"
    ],
    "selenium": [
        "selenium", "selenium webdriver"
    ],
    "pytest": [
        "pytest", "py test"
    ],
    "junit": [
        "junit", "junit5"
    ],
    "jest": [
        "jest", "jest testing"
    ],
    "postman": [
        "postman", "api testing"
    ],

    # -------------------------------------------------------------------------
    # OPERATING SYSTEMS & NETWORKING
    # -------------------------------------------------------------------------
    "linux": [
        "linux", "ubuntu", "centos", "debian", "unix", "rhel", "fedora"
    ],
    "windows server": [
        "windows server", "windows admin"
    ],
    "networking": [
        "networking", "tcp/ip", "dns", "http", "https", "vpn", "firewall"
    ],

    # -------------------------------------------------------------------------
    # SECURITY
    # -------------------------------------------------------------------------
    "cybersecurity": [
        "cybersecurity", "cyber security", "information security",
        "infosec", "network security"
    ],
    "penetration testing": [
        "penetration testing", "pen testing", "pentesting", "ethical hacking"
    ],
    "oauth": [
        "oauth", "oauth2", "jwt", "json web token", "authentication"
    ],
    "encryption": [
        "encryption", "ssl", "tls", "ssl/tls", "cryptography"
    ],

    # -------------------------------------------------------------------------
    # PROJECT MANAGEMENT & METHODOLOGIES
    # -------------------------------------------------------------------------
    "agile": [
        "agile", "agile methodology", "agile development"
    ],
    "scrum": [
        "scrum", "scrum master", "sprint planning"
    ],
    "kanban": [
        "kanban", "kanban board"
    ],
    "jira": [
        "jira", "atlassian jira"
    ],
    "confluence": [
        "confluence", "atlassian confluence"
    ],

    # -------------------------------------------------------------------------
    # DATA ANALYST & BI TOOLS
    # -------------------------------------------------------------------------
    "data analysis": [
        "data analysis", "data analytics", "data analyst",
        "exploratory data analysis", "eda", "data exploration"
    ],
    "sql": [
        "sql", "structured query language", "sql queries", "sql programming"
    ],
    "microsoft excel": [
        "excel", "ms excel", "microsoft excel", "advanced excel",
        "excel macros", "pivot tables", "vlookup", "xlookup"
    ],
    "tableau": [
        "tableau", "tableau desktop", "tableau server", "tableau dashboards"
    ],
    "power bi": [
        "power bi", "powerbi", "microsoft power bi", "power bi desktop",
        "dax", "power query"
    ],
    "looker": [
        "looker", "looker studio", "google looker"
    ],
    "qlik": [
        "qlik", "qlik sense", "qlikview"
    ],
    "google analytics": [
        "google analytics", "ga4", "ga", "google analytics 4"
    ],
    "data warehousing": [
        "data warehousing", "data warehouse", "etl", "extract transform load",
        "data pipeline"
    ],
    "sas": [
        "sas", "sas programming", "sas analytics"
    ],
    "alteryx": [
        "alteryx", "alteryx designer"
    ],

    # -------------------------------------------------------------------------
    # CUSTOMER SERVICE & SUPPORT
    # -------------------------------------------------------------------------
    "customer service": [
        "customer service", "customer support", "customer care",
        "client support", "help desk"
    ],
    "crm": [
        "crm", "customer relationship management", "crm software"
    ],
    "salesforce": [
        "salesforce", "salesforce crm", "salesforce admin"
    ],
    "zendesk": [
        "zendesk", "zendesk support"
    ],
    "freshdesk": [
        "freshdesk", "freshdesk support"
    ],
    "intercom": [
        "intercom", "intercom support"
    ],
    "ticketing systems": [
        "ticketing system", "helpdesk ticketing", "support tickets"
    ],
    "live chat": [
        "live chat", "chat support", "online chat"
    ],
    "call center": [
        "call center", "contact center", "inbound calls", "outbound calls"
    ],

    # -------------------------------------------------------------------------
    # FINANCE & ACCOUNTING
    # -------------------------------------------------------------------------
    "financial analysis": [
        "financial analysis", "financial analyst", "financial modeling"
    ],
    "financial modeling": [
        "financial modeling", "financial models", "dcf", "valuation models"
    ],
    "accounting": [
        "accounting", "general accounting", "accounts payable",
        "accounts receivable", "bookkeeping"
    ],
    "quickbooks": [
        "quickbooks", "quickbooks online", "qbo"
    ],
    "sap": [
        "sap", "sap erp", "sap fico", "sap hana"
    ],
    "oracle financials": [
        "oracle financials", "oracle erp", "oracle netsuite"
    ],
    "gaap": [
        "gaap", "generally accepted accounting principles"
    ],
    "ifrs": [
        "ifrs", "international financial reporting standards"
    ],
    "budgeting": [
        "budgeting", "budget planning", "budget forecasting"
    ],
    "forecasting": [
        "forecasting", "financial forecasting", "revenue forecasting"
    ],
    "variance analysis": [
        "variance analysis", "budget variance"
    ],
    "taxation": [
        "taxation", "tax preparation", "tax compliance", "corporate tax"
    ],
    "audit": [
        "audit", "internal audit", "external audit", "auditing"
    ],
    "bloomberg terminal": [
        "bloomberg", "bloomberg terminal"
    ],

    # -------------------------------------------------------------------------
    # BUSINESS ANALYST
    # -------------------------------------------------------------------------
    "business analysis": [
        "business analysis", "business analyst", "ba"
    ],
    "requirements gathering": [
        "requirements gathering", "requirement analysis",
        "requirement elicitation", "stakeholder interviews"
    ],
    "process mapping": [
        "process mapping", "business process mapping", "process flow",
        "process documentation"
    ],
    "user stories": [
        "user stories", "user story", "acceptance criteria"
    ],
    "uml": [
        "uml", "unified modeling language", "use case diagrams"
    ],
    "visio": [
        "visio", "microsoft visio", "ms visio"
    ],
    "lucidchart": [
        "lucidchart", "lucid charts"
    ],
    "business intelligence": [
        "business intelligence", "bi", "bi tools"
    ],
    "kpis": [
        "kpi", "kpis", "key performance indicators", "metrics"
    ],
    "swot analysis": [
        "swot", "swot analysis"
    ],
    "gap analysis": [
        "gap analysis", "current state vs future state"
    ],
    "feasibility study": [
        "feasibility study", "feasibility analysis"
    ],
    "stakeholder management": [
        "stakeholder management", "stakeholder engagement"
    ],

    # -------------------------------------------------------------------------
    # UI/UX DESIGN
    # -------------------------------------------------------------------------
    "ui design": [
        "ui design", "user interface design", "ui", "interface design"
    ],
    "ux design": [
        "ux design", "user experience design", "ux", "ux research"
    ],
    "ui/ux": [
        "ui/ux", "ui ux", "ui and ux"
    ],
    "figma": [
        "figma", "figma design"
    ],
    "sketch": [
        "sketch", "sketch app"
    ],
    "adobe xd": [
        "adobe xd", "xd", "experience design"
    ],
    "wireframing": [
        "wireframing", "wireframes", "low fidelity wireframes"
    ],
    "prototyping": [
        "prototyping", "interactive prototypes", "clickable prototypes"
    ],
    "user research": [
        "user research", "user interviews", "usability testing"
    ],
    "personas": [
        "personas", "user personas", "buyer personas"
    ],
    "user journey": [
        "user journey", "customer journey", "journey mapping"
    ],
    "information architecture": [
        "information architecture", "ia", "site map"
    ],
    "design systems": [
        "design system", "design systems", "component library"
    ],
    "accessibility": [
        "accessibility", "a11y", "wcag", "ada compliance"
    ],
    "responsive design": [
        "responsive design", "mobile first", "adaptive design"
    ],
    "adobe photoshop": [
        "photoshop", "adobe photoshop", "ps"
    ],
    "adobe illustrator": [
        "illustrator", "adobe illustrator", "ai"
    ],
    "invision": [
        "invision", "invision studio"
    ],

    # -------------------------------------------------------------------------
    # SOFT SKILLS (extracted as keywords)
    # -------------------------------------------------------------------------
    "communication": [
        "communication", "communication skills", "verbal communication",
        "written communication"
    ],
    "teamwork": [
        "teamwork", "team player", "collaboration", "collaborative"
    ],
    "leadership": [
        "leadership", "team lead", "tech lead", "leading teams",
        "team management"
    ],
    "problem solving": [
        "problem solving", "problem-solving", "analytical thinking",
        "critical thinking"
    ],
    "time management": [
        "time management", "deadline management", "prioritization"
    ],
    "mentoring": [
        "mentoring", "mentorship", "coaching", "training junior"
    ],
    "attention to detail": [
        "attention to detail", "detail oriented", "meticulous"
    ],
    "adaptability": [
        "adaptability", "flexible", "quick learner", "fast learner"
    ],
}


# =============================================================================
# DOMAIN DETECTION KEYWORDS
# Use this to detect whether a JD is tech-related or not
# =============================================================================

TECH_DOMAIN_KEYWORDS = [
    "software", "developer", "engineer", "python", "java", "api",
    "database", "cloud", "backend", "frontend", "fullstack", "devops",
    "machine learning", "data science", "infrastructure", "deployment"
]


# =============================================================================
# QUICK STATS
# =============================================================================

if __name__ == "__main__":
    total_canonical = len(SKILL_LIBRARY)
    total_aliases = sum(len(v) for v in SKILL_LIBRARY.values())
    print(f"Total canonical skills : {total_canonical}")
    print(f"Total aliases          : {total_aliases}")
    print(f"Categories covered     : Programming, Web, Databases, Cloud,")
    print(f"                         DevOps, ML/AI, Data, Mobile, Testing,")
    print(f"                         Security, Architecture, Soft Skills")