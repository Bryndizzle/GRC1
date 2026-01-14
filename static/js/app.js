// API Base URL
const API_BASE = window.location.origin;

// Tab switching
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.dataset.tab;

        // Update active tab button
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Update active tab content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabId).classList.add('active');
    });
});

// Loading overlay
function showLoading() {
    document.getElementById('loading').classList.add('show');
}

function hideLoading() {
    document.getElementById('loading').classList.remove('show');
}

// Chat functionality
const chatMessages = document.getElementById('chatMessages');
const chatInput = document.getElementById('chatInput');
const chatSend = document.getElementById('chatSend');
const chatAgeGroup = document.getElementById('chatAgeGroup');
const chatSkillLevel = document.getElementById('chatSkillLevel');

function addMessage(text, isBot = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;

    const p = document.createElement('p');
    p.textContent = text;
    messageDiv.appendChild(p);

    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendChatMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, false);
    chatInput.value = '';

    // Prepare context
    const context = {};
    if (chatAgeGroup.value) context.age_group = chatAgeGroup.value;
    if (chatSkillLevel.value) context.skill_level = chatSkillLevel.value;

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message, context })
        });

        const data = await response.json();

        if (response.ok) {
            addMessage(data.response, true);
        } else {
            addMessage(`Error: ${data.error}`, true);
        }
    } catch (error) {
        addMessage(`Error: ${error.message}`, true);
    } finally {
        hideLoading();
    }
}

chatSend.addEventListener('click', sendChatMessage);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendChatMessage();
    }
});

// Training Plan Form
const trainingForm = document.getElementById('trainingForm');
const trainingResult = document.getElementById('trainingResult');

trainingForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        age_group: document.getElementById('ageGroup').value,
        skill_level: document.getElementById('skillLevel').value,
        focus_area: document.getElementById('focusArea').value,
        duration: parseInt(document.getElementById('duration').value)
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/training-plan`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            trainingResult.textContent = result.plan;
            trainingResult.classList.add('show');
        } else {
            trainingResult.textContent = `Error: ${result.error}`;
            trainingResult.classList.add('show');
        }
    } catch (error) {
        trainingResult.textContent = `Error: ${error.message}`;
        trainingResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Drills Form
const drillsForm = document.getElementById('drillsForm');
const drillsResult = document.getElementById('drillsResult');

drillsForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const equipmentInput = document.getElementById('drillEquipment').value;
    const equipment = equipmentInput ? equipmentInput.split(',').map(item => item.trim()) : [];

    const data = {
        skill: document.getElementById('drillSkill').value,
        players: parseInt(document.getElementById('drillPlayers').value),
        equipment: equipment
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/drill-suggestion`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            drillsResult.textContent = result.drills;
            drillsResult.classList.add('show');
        } else {
            drillsResult.textContent = `Error: ${result.error}`;
            drillsResult.classList.add('show');
        }
    } catch (error) {
        drillsResult.textContent = `Error: ${error.message}`;
        drillsResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Tactics Form
const tacticsForm = document.getElementById('tacticsForm');
const tacticsResult = document.getElementById('tacticsResult');

tacticsForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        formation: document.getElementById('formation').value,
        situation: document.getElementById('situation').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/tactical-advice`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            tacticsResult.textContent = result.advice;
            tacticsResult.classList.add('show');
        } else {
            tacticsResult.textContent = `Error: ${result.error}`;
            tacticsResult.classList.add('show');
        }
    } catch (error) {
        tacticsResult.textContent = `Error: ${error.message}`;
        tacticsResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Add welcome animation
window.addEventListener('load', () => {
    console.log('Grassroots Coach loaded successfully!');
});

// ==================== SEO SPECIALIST AGENT ====================

// SEO Sub-tab switching
document.querySelectorAll('.seo-subtab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.dataset.seotab;

        // Update active sub-tab button
        document.querySelectorAll('.seo-subtab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Update active sub-tab content
        document.querySelectorAll('.seo-subtab-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabId).classList.add('active');
    });
});

// SEO Chat functionality
const seoChatMessages = document.getElementById('seoChatMessages');
const seoChatInput = document.getElementById('seoChatInput');
const seoChatSend = document.getElementById('seoChatSend');
const seoBusinessName = document.getElementById('seoBusinessName');
const seoIndustry = document.getElementById('seoIndustry');

function addSeoMessage(text, isBot = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isBot ? 'bot-message seo-bot' : 'user-message'}`;

    const p = document.createElement('p');
    p.textContent = text;
    messageDiv.appendChild(p);

    seoChatMessages.appendChild(messageDiv);
    seoChatMessages.scrollTop = seoChatMessages.scrollHeight;
}

async function sendSeoChatMessage() {
    const message = seoChatInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addSeoMessage(message, false);
    seoChatInput.value = '';

    // Prepare context
    const context = {};
    if (seoBusinessName.value) context.business_name = seoBusinessName.value;
    if (seoIndustry.value) context.industry = seoIndustry.value;

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message, context })
        });

        const data = await response.json();

        if (response.ok) {
            addSeoMessage(data.response, true);
        } else {
            addSeoMessage(`Error: ${data.error}`, true);
        }
    } catch (error) {
        addSeoMessage(`Error: ${error.message}`, true);
    } finally {
        hideLoading();
    }
}

seoChatSend.addEventListener('click', sendSeoChatMessage);
seoChatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendSeoChatMessage();
    }
});

// Helper function to parse textarea lines into array
function parseTextareaToArray(text) {
    if (!text) return [];
    return text.split('\n').map(line => line.trim()).filter(line => line.length > 0);
}

// Link Building Strategy Form
const linkBuildingForm = document.getElementById('linkBuildingForm');
const linkBuildingResult = document.getElementById('linkBuildingResult');

linkBuildingForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        business_name: document.getElementById('lbBusinessName').value,
        industry: document.getElementById('lbIndustry').value,
        target_pages: parseTextareaToArray(document.getElementById('lbTargetPages').value),
        competitors: parseTextareaToArray(document.getElementById('lbCompetitors').value)
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/link-building-strategy`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            linkBuildingResult.textContent = result.strategy;
            linkBuildingResult.classList.add('show');
        } else {
            linkBuildingResult.textContent = `Error: ${result.error}`;
            linkBuildingResult.classList.add('show');
        }
    } catch (error) {
        linkBuildingResult.textContent = `Error: ${error.message}`;
        linkBuildingResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Digital PR Campaign Form
const digitalPrForm = document.getElementById('digitalPrForm');
const digitalPrResult = document.getElementById('digitalPrResult');

digitalPrForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        business_name: document.getElementById('prBusinessName').value,
        industry: document.getElementById('prIndustry').value,
        unique_angle: document.getElementById('prUniqueAngle').value,
        target_audience: document.getElementById('prTargetAudience').value,
        budget_level: document.getElementById('prBudget').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/digital-pr-campaign`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            digitalPrResult.textContent = result.campaign;
            digitalPrResult.classList.add('show');
        } else {
            digitalPrResult.textContent = `Error: ${result.error}`;
            digitalPrResult.classList.add('show');
        }
    } catch (error) {
        digitalPrResult.textContent = `Error: ${error.message}`;
        digitalPrResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Community Strategy Form
const communityForm = document.getElementById('communityForm');
const communityResult = document.getElementById('communityResult');

communityForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get selected platforms
    const platforms = [];
    if (document.getElementById('platformReddit').checked) platforms.push('Reddit');
    if (document.getElementById('platformQuora').checked) platforms.push('Quora');
    if (document.getElementById('platformYouTube').checked) platforms.push('YouTube');
    if (document.getElementById('platformDiscord').checked) platforms.push('Discord');
    if (document.getElementById('platformLinkedIn').checked) platforms.push('LinkedIn');
    if (document.getElementById('platformFacebook').checked) platforms.push('Facebook');

    const data = {
        business_name: document.getElementById('commBusinessName').value,
        industry: document.getElementById('commIndustry').value,
        target_platforms: platforms,
        products_services: document.getElementById('commProducts').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/community-strategy`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            communityResult.textContent = result.strategy;
            communityResult.classList.add('show');
        } else {
            communityResult.textContent = `Error: ${result.error}`;
            communityResult.classList.add('show');
        }
    } catch (error) {
        communityResult.textContent = `Error: ${error.message}`;
        communityResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// AEO Strategy Form
const aeoForm = document.getElementById('aeoForm');
const aeoResult = document.getElementById('aeoResult');

aeoForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        business_name: document.getElementById('aeoBusinessName').value,
        industry: document.getElementById('aeoIndustry').value,
        key_topics: parseTextareaToArray(document.getElementById('aeoTopics').value),
        target_queries: parseTextareaToArray(document.getElementById('aeoQueries').value)
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/aeo-strategy`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            aeoResult.textContent = result.strategy;
            aeoResult.classList.add('show');
        } else {
            aeoResult.textContent = `Error: ${result.error}`;
            aeoResult.classList.add('show');
        }
    } catch (error) {
        aeoResult.textContent = `Error: ${error.message}`;
        aeoResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Reputation Audit Form
const reputationForm = document.getElementById('reputationForm');
const reputationResult = document.getElementById('reputationResult');

reputationForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        business_name: document.getElementById('repBusinessName').value,
        industry: document.getElementById('repIndustry').value,
        known_issues: document.getElementById('repKnownIssues').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/reputation-audit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            reputationResult.textContent = result.audit;
            reputationResult.classList.add('show');
        } else {
            reputationResult.textContent = `Error: ${result.error}`;
            reputationResult.classList.add('show');
        }
    } catch (error) {
        reputationResult.textContent = `Error: ${error.message}`;
        reputationResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Listicle Strategy Form
const listicleForm = document.getElementById('listicleForm');
const listicleResult = document.getElementById('listicleResult');

listicleForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        business_name: document.getElementById('listBusinessName').value,
        industry: document.getElementById('listIndustry').value,
        product_category: document.getElementById('listProductCategory').value,
        key_differentiators: document.getElementById('listDifferentiators').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/listicle-strategy`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            listicleResult.textContent = result.strategy;
            listicleResult.classList.add('show');
        } else {
            listicleResult.textContent = `Error: ${result.error}`;
            listicleResult.classList.add('show');
        }
    } catch (error) {
        listicleResult.textContent = `Error: ${error.message}`;
        listicleResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// Outreach Templates Form
const outreachForm = document.getElementById('outreachForm');
const outreachResult = document.getElementById('outreachResult');

outreachForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        outreach_type: document.getElementById('outreachType').value,
        business_name: document.getElementById('outBusinessName').value,
        industry: document.getElementById('outIndustry').value,
        context: document.getElementById('outContext').value
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/outreach-templates`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            outreachResult.textContent = result.templates;
            outreachResult.classList.add('show');
        } else {
            outreachResult.textContent = `Error: ${result.error}`;
            outreachResult.classList.add('show');
        }
    } catch (error) {
        outreachResult.textContent = `Error: ${error.message}`;
        outreachResult.classList.add('show');
    } finally {
        hideLoading();
    }
});

// SEO Report Form
const reportForm = document.getElementById('reportForm');
const reportResult = document.getElementById('reportResult');

reportForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Try to parse metrics as JSON, otherwise use as string
    let currentMetrics = null;
    const metricsText = document.getElementById('reportMetrics').value;
    if (metricsText) {
        try {
            currentMetrics = JSON.parse(metricsText);
        } catch {
            currentMetrics = { description: metricsText };
        }
    }

    // Try to parse goals as JSON, otherwise use as string
    let goals = null;
    const goalsText = document.getElementById('reportGoals').value;
    if (goalsText) {
        try {
            goals = JSON.parse(goalsText);
        } catch {
            goals = { description: goalsText };
        }
    }

    const data = {
        business_name: document.getElementById('reportBusinessName').value,
        current_metrics: currentMetrics,
        goals: goals
    };

    showLoading();

    try {
        const response = await fetch(`${API_BASE}/api/seo/report`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            reportResult.textContent = result.report;
            reportResult.classList.add('show');
        } else {
            reportResult.textContent = `Error: ${result.error}`;
            reportResult.classList.add('show');
        }
    } catch (error) {
        reportResult.textContent = `Error: ${error.message}`;
        reportResult.classList.add('show');
    } finally {
        hideLoading();
    }
});
