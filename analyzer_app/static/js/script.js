// ============================================
// TAB SWITCHING
// ============================================
function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(tabId).classList.add('active');
    event.target.classList.add('active');
}

// ============================================
// FILE UPLOAD HANDLING
// ============================================
const fileInput = document.getElementById('resumeFile');
const uploadArea = document.getElementById('uploadArea');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');

fileInput.addEventListener('change', handleFileSelect);

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#667eea';
    uploadArea.style.background = '#f8f9ff';
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.borderColor = '#dee2e6';
    uploadArea.style.background = '#f8f9fa';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#dee2e6';
    uploadArea.style.background = '#f8f9fa';
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
});

function handleFileSelect() {
    const file = fileInput.files[0];
    if (file) {
        if (file.size > 5 * 1024 * 1024) {
            alert('File size must be less than 5MB');
            clearFile();
            return;
        }
        
        const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
        if (!validTypes.includes(file.type) && !file.name.match(/\.(pdf|docx|txt)$/i)) {
            alert('Please upload PDF, DOCX, or TXT file');
            clearFile();
            return;
        }
        
        fileName.textContent = `📎 ${file.name}`;
        document.querySelector('.upload-placeholder').style.display = 'none';
        fileInfo.style.display = 'flex';
    }
}

function clearFile() {
    fileInput.value = '';
    document.querySelector('.upload-placeholder').style.display = 'block';
    fileInfo.style.display = 'none';
}

// ============================================
// ANALYZE RESUME
// ============================================
async function analyzeResume() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');
    const btnLoader = document.getElementById('btnLoader');
    
    const resumeText = document.getElementById('resumeText').value.trim();
    const resumeFile = fileInput.files[0];
    const jdText = document.getElementById('jdText').value.trim();

    if (!jdText) {
        alert('Please enter job description');
        return;
    }
    
    if (!resumeText && !resumeFile) {
        alert('Please enter resume text or upload a file');
        return;
    }
    
    const formData = new FormData();
    formData.append('jd_text', jdText);
    
    if (resumeFile) {
        formData.append('resume_file', resumeFile);
    } else {
        formData.append('resume_text', resumeText);
    }
    
    // Show loading
    analyzeBtn.disabled = true;
    btnText.textContent = 'Analyzing...';
    btnLoader.style.display = 'inline-block';
    
    try {
        const response = await fetch('/analyze/', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayResults(data);
        } else {
            alert(data.error || 'Analysis failed');
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        analyzeBtn.disabled = false;
        btnText.textContent = 'Analyze Resume';
        btnLoader.style.display = 'none';
    }
}

// ============================================
// DISPLAY RESULTS
// ============================================
function displayResults(data) {
    const placeholder = document.getElementById('resultsPlaceholder');
    const resultsContent = document.getElementById('resultsContent');
    
    // Hide placeholder, show results
    placeholder.style.display = 'none';
    resultsContent.style.display = 'block';
    
    // Build results HTML
    const html = `
        <div class="score-card">
            <div class="score-label">Overall Match Score</div>
            <div class="score-value">${data.final_score}%</div>
            <div class="score-label">Skills · Education · Similarity</div>
        </div>
        
        <div class="component-scores">
            <h3>Score Breakdown</h3>
            <div class="score-item">
                <span class="score-item-label">📊 Skills Match</span>
                <span class="score-item-value">${data.skill_score}%</span>
            </div>
            <div class="score-item">
                <span class="score-item-label">🎓 Education Match</span>
                <span class="score-item-value">${data.education_score}%</span>
            </div>
            <div class="score-item">
                <span class="score-item-label">🔍 Semantic Similarity</span>
                <span class="score-item-value">${data.similarity_score}%</span>
            </div>
        </div>
        
        ${renderSkillsSection(data.skill_details)}
        ${renderEducationSection(data.education_details)}
        ${renderSimilaritySection(data.similarity_details)}
    `;
    
    resultsContent.innerHTML = html;
    
    // Scroll results panel to top
    document.getElementById('rightPanel').querySelector('.panel-content').scrollTop = 0;
}

function renderSkillsSection(details) {
    const matched = Array.from(details.Matched_skills || []);
    const missing = Array.from(details.Missing_skills || []);
    const extra = Array.from(details.Extra_skills || []);
    
    return `
        <div class="skills-section">
            <h3>✅ Matched Skills (${matched.length})</h3>
            ${matched.length > 0 
                ? matched.map(s => `<span class="skill-tag matched">${s}</span>`).join('') 
                : '<p style="color: #868e96; font-size: 0.85rem;">No matched skills found</p>'}
        </div>
        
        <div class="skills-section">
            <h3>❌ Missing Skills (${missing.length})</h3>
            ${missing.length > 0 
                ? missing.map(s => `<span class="skill-tag missing">${s}</span>`).join('') 
                : '<p style="color: #868e96; font-size: 0.85rem;">You have all required skills!</p>'}
        </div>
        
        ${extra.length > 0 ? `
        <div class="skills-section">
            <h3>➕ Additional Skills (${extra.length})</h3>
            ${extra.map(s => `<span class="skill-tag">${s}</span>`).join('')}
        </div>
        ` : ''}
    `;
}

function renderEducationSection(details) {
    return `
        <div class="detail-section">
            <h3>🎓 Education Details</h3>
            <div class="detail-row">
                <span class="detail-label">Your Degree:</span>
                <span class="detail-value">${details.resume_degree || 'Not detected'}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Required Degree:</span>
                <span class="detail-value">${details.jd_degree || 'Not specified'}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Your Field:</span>
                <span class="detail-value">${details.resume_field || 'Not detected'}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Required Field:</span>
                <span class="detail-value">${details.jd_field || 'Not specified'}</span>
            </div>
            ${details.degree_score ? `
            <div class="detail-row">
                <span class="detail-label">Degree Match:</span>
                <span class="detail-value">${details.degree_score}%</span>
            </div>` : ''}
            ${details.field_score ? `
            <div class="detail-row">
                <span class="detail-label">Field Match:</span>
                <span class="detail-value">${details.field_score}%</span>
            </div>` : ''}
        </div>
    `;
}

function renderSimilaritySection(details) {
    return `
        <div class="detail-section">
            <h3>🔍 Similarity Breakdown</h3>
            <div class="detail-row">
                <span class="detail-label">Semantic (SBERT):</span>
                <span class="detail-value">${details.sbert}%</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Keyword (TF-IDF):</span>
                <span class="detail-value">${details.tfidf}%</span>
            </div>
            <p style="color: #868e96; font-size: 0.8rem; margin-top: 8px; line-height: 1.4;">
                Semantic matching understands meaning, while keyword matching finds exact terms.
            </p>
        </div>
    `;
}