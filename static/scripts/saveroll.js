const saveBtn = document.getElementById("save-track");
const csrfToken = document.getElementById("csrfToken").value;
const trackNameInput = document.getElementById("trackNameInput");

saveBtn.addEventListener("click", async () => {
    const notes = window.getRecordedNotes();
    const bpm = Number(document.getElementById("bpmInput").value);
    const trackName = trackNameInput.value;

    if (!trackName || notes.length === 0) {
        alert("Track name or notes missing");
        return;
    }

    const res = await fetch("/save-track/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({
            name: trackName,
            bpm,
            notes
        })
    });

    if (res.ok) {
        alert("Track saved");
    } else {
        alert("Error saving track");
    }
});