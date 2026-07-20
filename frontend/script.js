const predictBtn = document.getElementById("predictBtn");

predictBtn.addEventListener("click", async () => {

    const battingTeam = document.getElementById("batting_team").value;
    const bowlingTeam = document.getElementById("bowling_team").value;
    const city = document.getElementById("city").value;
    if (battingTeam === bowlingTeam) {
    alert("Batting Team and Bowling Team cannot be the same.");
    return;
}

    const target = parseInt(document.getElementById("target").value);
    const score = parseInt(document.getElementById("score").value);

    const oversInput = document.getElementById("overs").value;
    const wicketsLost = parseInt(document.getElementById("wickets").value);

    if (
        !target ||
        !score ||
        !oversInput
    ) {
        alert("Please fill all fields.");
        return;
    }

    // Overs -> Balls
    const overParts = oversInput.split(".");
    const overs = parseInt(overParts[0]);
    const balls = overParts.length > 1 ? parseInt(overParts[1]) : 0;

    if (balls > 5) {
        alert("Invalid over. Ball should be between 0 and 5.");
        return;
    }

    const ballsBowled = overs * 6 + balls;
    const ballsLeft = 120 - ballsBowled;

    if (ballsLeft <= 0) {
        alert("Match already completed.");
        return;
    }

    const runsLeft = target - score;

    const wicketsLeft = 10 - wicketsLost;

    const crr = (score * 6) / ballsBowled;

    const rrr = (runsLeft * 6) / ballsLeft;

    const response = await fetch("http://127.0.0.1:5000/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            batting_team: battingTeam,
            bowling_team: bowlingTeam,
            city: city,

            target: target,
            runs_left: runsLeft,
            balls_left: ballsLeft,
            wickets_left: wicketsLeft,

            crr: crr,
            rrr: rrr

        })

    });

    const data = await response.json();

    document.getElementById("resultCard").style.display = "block";

    document.getElementById("batTeamName").innerText = battingTeam;
    document.getElementById("bowlTeamName").innerText = bowlingTeam;

    document.getElementById("batPercent").innerText =
        data.batting_team_win + "%";

    document.getElementById("bowlPercent").innerText =
        data.bowling_team_win + "%";

    document.getElementById("batBar").style.width =
        data.batting_team_win + "%";

    document.getElementById("bowlBar").style.width =
        data.bowling_team_win + "%";

});