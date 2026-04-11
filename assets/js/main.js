//this is for checking and stuff
const defaultUser = {
  progress: 0,
  badges: [],
  completedModules: [],
  scoresOfQuiz: {
    income: 0,
    investment: 0,
    insurance: 0,
    tax: 0,
    scams: 0,
  },
};

// Periodic mascot animation (blink + wing flap every 7 seconds)
document.addEventListener("DOMContentLoaded", function () {
  const mascotIcon = document.querySelector(".mascot-icon");

  if (mascotIcon) {
    setInterval(() => {
      // Wing flap animation
      mascotIcon.style.animation = "mascotWing 0.8s ease-in-out 3";

      // Blink animation
      setTimeout(() => {
        mascotIcon.style.animation = "mascotBlink 1s ease-in-out 2";
      }, 400);

      // Reset after animations complete
      setTimeout(() => {
        mascotIcon.style.animation = "mascotIdle 0.2s ease-in-out 1";
      }, 2400);
    }, 7000); // Every 7 seconds
  }
});
