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

// Stopwatch functionality
let stopwatchInterval = null;
let stopwatchTime = 0;
let isStopwatchRunning = false;
let lapTimes = [];
let lapCounter = 1;

const stopwatchDisplay = document.getElementById('stopwatchTime');
const startBtn = document.getElementById('startBtn');
const lapBtn = document.getElementById('lapBtn');
const resetBtn = document.getElementById('resetBtn');
const lapsList = document.getElementById('lapsList');

function formatTime(milliseconds) {
    const totalSeconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    const centiseconds = Math.floor((milliseconds % 1000) / 10);

    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}.${String(centiseconds).padStart(2, '0')}`;
}

function updateStopwatchDisplay() {
    stopwatchDisplay.textContent = formatTime(stopwatchTime);
}

function startStopwatch() {
    if (!isStopwatchRunning) {
        isStopwatchRunning = true;
        const startTime = Date.now() - stopwatchTime;

        stopwatchInterval = setInterval(() => {
            stopwatchTime = Date.now() - startTime;
            updateStopwatchDisplay();
        }, 10);

        startBtn.textContent = 'Stop';
        startBtn.classList.remove('btn-start');
        startBtn.classList.add('btn-stop');
        lapBtn.disabled = false;
    } else {
        isStopwatchRunning = false;
        clearInterval(stopwatchInterval);
        startBtn.textContent = 'Start';
        startBtn.classList.remove('btn-stop');
        startBtn.classList.add('btn-start');
    }
}

function recordLap() {
    if (isStopwatchRunning && stopwatchTime > 0) {
        const lapTime = stopwatchTime;
        const previousLapTime = lapTimes.length > 0 ? lapTimes[lapTimes.length - 1].time : 0;
        const splitTime = lapTime - previousLapTime;

        lapTimes.push({ time: lapTime, split: splitTime });

        // Remove "no laps" message if it exists
        const noLapsMessage = lapsList.querySelector('.no-laps');
        if (noLapsMessage) {
            noLapsMessage.remove();
        }

        // Add new lap to the list (at the beginning)
        const lapItem = document.createElement('div');
        lapItem.className = 'lap-item';
        lapItem.innerHTML = `
            <span class="lap-number">Lap ${lapCounter}</span>
            <span class="lap-split">${formatTime(splitTime)}</span>
            <span class="lap-total">${formatTime(lapTime)}</span>
        `;

        lapsList.insertBefore(lapItem, lapsList.firstChild);
        lapCounter++;
    }
}

function resetStopwatch() {
    clearInterval(stopwatchInterval);
    stopwatchTime = 0;
    isStopwatchRunning = false;
    lapTimes = [];
    lapCounter = 1;

    updateStopwatchDisplay();
    startBtn.textContent = 'Start';
    startBtn.classList.remove('btn-stop');
    startBtn.classList.add('btn-start');
    lapBtn.disabled = true;

    // Clear laps list
    lapsList.innerHTML = '<p class="no-laps">No lap times recorded yet</p>';
}

startBtn.addEventListener('click', startStopwatch);
lapBtn.addEventListener('click', recordLap);
resetBtn.addEventListener('click', resetStopwatch);

// Add welcome animation
window.addEventListener('load', () => {
    console.log('Grassroots Coach loaded successfully!');
});
