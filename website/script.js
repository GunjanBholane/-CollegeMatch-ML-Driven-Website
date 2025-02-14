document.getElementById("check-eligibility").addEventListener("click", function () {
    const marks = parseFloat(document.getElementById("marks").value);
    const caste = document.getElementById("caste").value;
    const branch = document.getElementById("branch").value;
    const resultDiv = document.getElementById("result");

    if (!marks || !caste || !branch) {
        resultDiv.textContent = "Please fill all the fields!";
        resultDiv.style.color = "red";
        return;
    }

    if (marks >= 90 && marks <= 99 && caste === "OBC" && branch === "Computer") {
        resultDiv.textContent = "You are eligible for admission to COEP Pune (Computer Branch).";
        resultDiv.style.color = "green";
    } else if (marks >= 80 && marks <= 89 && caste === "Open" && branch === "Mechanical") {
        resultDiv.textContent = "You are eligible for admission to COEP Pune (Mechanical Branch).";
        resultDiv.style.color = "green";
    } else {
        resultDiv.textContent = "No college available.";
        resultDiv.style.color = "red";
    }
});
