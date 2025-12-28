const bpmInput = document.getElementById("bpmInput");
const playBtn = document.getElementById("playBtn");
const pauseBtn = document.getElementById("pausepBtn");

const noteButtons = document.querySelectorAll("button.keywhite, button.keyblack");

let recordedNotes = [];
let isRecording = false;
let startTime = null;

// === BPM ===
function getSecondsPerBeat() {
    return 60 / Number(bpmInput.value || 120);
}

// === Нажатие на ноту ===
noteButtons.forEach(btn => {
    btn.addEventListener("mousedown", () => startNote(btn));
    btn.addEventListener("mouseup", () => endNote(btn));
    btn.addEventListener("mouseleave", () => endNote(btn));
});

const activeNotes = new Map();

function startNote(button) {
    const note = button.innerText.trim();

    if (!isRecording) {
        isRecording = true;
        startTime = performance.now();
    }

    const now = performance.now();
    const start = (now - startTime) / 1000;

    activeNotes.set(note, {
        note,
        start,
        velocity: 80
    });

    button.classList.add("active");
}

function endNote(button) {
    const note = button.innerText.trim();
    if (!activeNotes.has(note)) return;

    const now = performance.now();
    const noteData = activeNotes.get(note);
    noteData.duration = (now - (startTime + noteData.start * 1000)) / 1000;

    recordedNotes.push(noteData);
    activeNotes.delete(note);

    button.classList.remove("active");
}

// === Управление ===
playBtn.addEventListener("click", () => {
    recordedNotes = [];
    isRecording = true;
    startTime = performance.now();
    console.log("Recording started");
});

pauseBtn.addEventListener("click", () => {
    isRecording = false;
    console.log("Recording stopped");
    console.table(recordedNotes);
});

// === Экспорт для backend ===
window.getRecordedNotes = () => recordedNotes;