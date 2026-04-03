/* Auth Page javascript - Connected to Database */

const API_URL = "http://localhost:5000/api";

function showLogin() {
  document.getElementById("loginView").classList.add("active");
  document.getElementById("signupView").classList.remove("active");
}

function showSignup() {
  document.getElementById("signupView").classList.add("active");
  document.getElementById("loginView").classList.remove("active");
}

async function login() {
  let username = document.getElementById("loginUser").value;
  let password = document.getElementById("loginPass").value;

  if (!username || !password) {
    alert("Please fill all fields");
    return;
  }

  try {
    const response = await fetch(`${API_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.ok) {
      // Store user session
      localStorage.setItem("loggedInUser", data.username);
      localStorage.setItem("userId", data.user_id);
      alert("Login successful!");
      window.location.href = "index.html";
    } else {
      alert(data.error || "Invalid username or password");
    }
  } catch (error) {
    console.error("Login error:", error);
    alert(
      "Cannot connect to server. Make sure Flask is running (python app.py)",
    );
  }
}

async function createAccount() {
  let username = document.getElementById("signupUser").value;
  let password = document.getElementById("signupPass").value;

  if (!username || !password) {
    alert("Please fill all fields");
    return;
  }

  if (password.length < 4) {
    alert("Password must be at least 4 characters");
    return;
  }

  try {
    const response = await fetch(`${API_URL}/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.ok) {
      alert("Account created successfully! Please login.");
      showLogin();
    } else {
      alert(data.error || "Registration failed");
    }
  } catch (error) {
    console.error("Registration error:", error);
    alert(
      "Cannot connect to server. Make sure Flask is running (python app.py)",
    );
  }
}

if (window.location.hash === "#signup") {
  showSignup();
} else {
  showLogin();
}
