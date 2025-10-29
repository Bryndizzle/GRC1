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
