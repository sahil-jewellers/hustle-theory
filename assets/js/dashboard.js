/* Dashboard - Connected to Database */

const API_URL = "http://localhost:5000/api";
let userId = localStorage.getItem("userId");
let user = localStorage.getItem("loggedInUser");
let completedModules = 0;

// Check if user is logged in
if (!user || !userId) {
  window.location.href = "auth.html";
}

// Display welcome message
if (user) {
  document.getElementById("welcomeUser").innerText = "Welcome, " + user + " 👋";
}

function logout() {
  localStorage.removeItem("loggedInUser");
  localStorage.removeItem("userId");
  window.location.href = "auth.html";
}

// Load user progress from database
async function loadProgress() {
  try {
    const response = await fetch(`${API_URL}/progress/${userId}`);
    const progressData = await response.json();

    // Calculate completed modules
    completedModules = progressData.filter((p) => p.completed).length;

    // Update progress bar
    let progress = completedModules * 20;
    document.querySelector(".progress-fill").style.width = progress + "%";
    document.getElementById("progressText").innerText =
      "Progress: " + progress + "% Completed";

    // Unlock modules
    for (let i = 2; i <= 5; i++) {
      if (i <= completedModules + 1) {
        document.getElementById("status" + i).innerText = "Unlocked ✅";
      }
    }

    // Load badges
    await loadBadges();
  } catch (error) {
    console.error("Error loading progress:", error);
    // Fallback to local mode if server is down
    completedModules = parseInt(localStorage.getItem("modulesCompleted") || 0);
  }
}

// Load badges from database
async function loadBadges() {
  try {
    const response = await fetch(`${API_URL}/badges/${userId}`);
    const badges = await response.json();

    let badgeContainer = document.getElementById("badgeContainer");

    if (badges.length === 0) {
      badgeContainer.innerHTML =
        "<p>No badges yet. Complete modules to unlock rewards!</p>";
    } else {
      badgeContainer.innerHTML = "";
      badges.forEach((badge) => {
        badgeContainer.innerHTML += `<div class="dashboard-badge">${badge.badge_name}</div>`;
      });
    }
  } catch (error) {
    console.error("Error loading badges:", error);
    // Fallback to local display
    let badgeContainer = document.getElementById("badgeContainer");
    if (completedModules >= 1) {
      badgeContainer.innerHTML +=
        '<div class="dashboard-badge">🏆 Budget Boss</div>';
    }
    if (completedModules >= 3) {
      badgeContainer.innerHTML +=
        '<div class="dashboard-badge">💰 Smart Investor</div>';
    }
    if (completedModules == 5) {
      badgeContainer.innerHTML +=
        '<div class="dashboard-badge">🛡 Scam Shield</div>';
    }
  }
}

function startModule(moduleNumber) {
  if (moduleNumber <= completedModules + 1) {
    window.location.href = "modules/module" + moduleNumber + ".html";
  } else {
    alert("Complete previous module first!");
  }
}

/* Finance Tracker */
function openTracker() {
  window.location.href = "tracker.html";
}

// Load progress when page loads
loadProgress();
