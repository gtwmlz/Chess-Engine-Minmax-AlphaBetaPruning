// Minimal frontend that calls backend best-move endpoint.
// This file does not render a fancy chessboard; it focuses on FEN input and results.

document.addEventListener("DOMContentLoaded", function () {
  const fenInput = document.getElementById("fen");
  const depthInput = document.getElementById("depth");
  const setFenBtn = document.getElementById("setFen");
  const askBtn = document.getElementById("askMove");
  const output = document.getElementById("output");

  // default starting position
  fenInput.value = "rn1qkbnr/ppp1pppp/3p4/8/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq - 0 3";

  setFenBtn.addEventListener("click", () => {
    output.innerText = "FEN set.";
  });

  askBtn.addEventListener("click", async () => {
    const fen = fenInput.value.trim();
    const depth = parseInt(depthInput.value, 10) || 3;
    output.innerText = "Requesting best move...";
    try {
      const resp = await fetch("/best-move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fen, depth }),
      });
      const data = await resp.json();
      output.innerText = JSON.stringify(data, null, 2);
    } catch (err) {
      output.innerText = "Error: " + err;
    }
  });
});
