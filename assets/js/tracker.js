/* Savings files javascript file - Connected to Database */

const API_URL = "http://localhost:5000/api";

function calculate() {
  let item = document.getElementById("item").value;
  let price = parseFloat(document.getElementById("price").value);
  let allowance = parseFloat(document.getElementById("allowance").value);
  let allowanceType = document.getElementById("allowanceType").value;
  let time = parseFloat(document.getElementById("time").value);
  let timeType = document.getElementById("timeType").value;

  if (!item || !price || !allowance || !time) {
    alert("Please fill all fields");
    return;
  }

  let days = time;
  if (timeType == "weeks") days = time * 7;
  if (timeType == "months") days = time * 30;
  let perDay = price / days;
  let perWeek = perDay * 7;

  document.getElementById("display").innerText = "₹" + price;
  document.getElementById("summary").innerHTML =
    "<b>Goal:</b> " + item + "<br><b>Price:</b> ₹" + price;
  document.getElementById("saveDaily").innerText =
    "You must save ₹" + perDay.toFixed(2) + " per day";
  document.getElementById("saveWeekly").innerText =
    "or ₹" + perWeek.toFixed(2) + " per week";
  document.getElementById("result").style.display = "block";
  document.getElementById("bar").style.width = "100%";

  // Save to database
  const userId = localStorage.getItem("userId");
  if (userId) {
    saveSavingsGoal(
      userId,
      item,
      price,
      allowance,
      allowanceType,
      time,
      timeType,
    );
  }
}

async function saveSavingsGoal(
  userId,
  item,
  price,
  allowance,
  allowanceType,
  timeValue,
  timeType,
) {
  try {
    const response = await fetch(`${API_URL}/savings`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: parseInt(userId),
        item_name: item,
        target_price: price,
        allowance: allowance,
        allowance_type: allowanceType,
        time_value: timeValue,
        time_type: timeType,
      }),
    });

    const data = await response.json();
    console.log("Savings goal saved:", data);
  } catch (error) {
    console.error("Error saving goal:", error);
    // Continue even if database save fails
  }
}
