
// =====================================
// 1. Dashboard Navigation
// =====================================

const navButtons = document.querySelectorAll(".nav-btn");
const sections = document.querySelectorAll(".content-section");

navButtons.forEach(button => {

    button.addEventListener("click", () => {

        const targetSection = button.dataset.section;

        navButtons.forEach(btn => btn.classList.remove("active"));
        sections.forEach(section => section.classList.remove("active"));

        button.classList.add("active");

        document.getElementById(targetSection).classList.add("active");
    });

});


// =====================================
// 2. AI Agent Integration
// =====================================

const agentButton = document.getElementById("agent-btn");

agentButton.addEventListener("click", async () => {

    const instruction = document.getElementById("instruction").value.trim();

    const resultBox = document.getElementById("agent-result");
    const output = document.getElementById("agent-output");

    if (!instruction) {
        alert("Please enter a DevOps instruction.");
        return;
    }

    agentButton.disabled = true;
    agentButton.textContent = "Generating AI Plan...";

    resultBox.classList.remove("hidden");
    output.textContent = "AI Agent is analyzing your request...";

    try {

        const response = await fetch("/agent/plan", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                instruction: instruction
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Unable to generate AI plan.");
        }

        output.textContent = JSON.stringify(data, null, 2);

    } catch (error) {

        output.textContent = "Error: " + error.message;

    } finally {

        agentButton.disabled = false;
        agentButton.textContent = "Generate AI Plan →";

    }

});


// =====================================
// 3. GitHub Code Analysis Integration
// =====================================

const githubButton = document.getElementById("github-btn");

githubButton.addEventListener("click", async () => {

    const owner = document.getElementById("owner").value.trim();
    const repo = document.getElementById("repo").value.trim();
    const path = document.getElementById("path").value.trim();

    const resultBox = document.getElementById("github-result");
    const output = document.getElementById("github-output");

    if (!owner || !repo || !path) {
        alert("Please fill all GitHub fields.");
        return;
    }

    githubButton.disabled = true;
    githubButton.textContent = "Analyzing Code...";

    resultBox.classList.remove("hidden");
    output.textContent = "Fetching GitHub source code...";

    try {

        const response = await fetch("/github/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                owner: owner,
                repo: repo,
                path: path
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "GitHub analysis failed.");
        }

        output.textContent = JSON.stringify(data, null, 2);

    } catch (error) {

        output.textContent = "Error: " + error.message;

    } finally {

        githubButton.disabled = false;
        githubButton.textContent = "Analyze Code →";

    }

});
