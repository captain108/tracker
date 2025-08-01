document.querySelectorAll("table tr").forEach(row => {
  let cell = row.cells[1];
  if (!cell) return;
  if (cell.innerText.includes("online")) cell.style.color = "green";
  if (cell.innerText.includes("offline")) cell.style.color = "red";
});
