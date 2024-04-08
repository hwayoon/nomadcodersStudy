const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
canvas.width = 600;
canvas.height = 600;

ctx.fillRect(150, 200, 15, 100);
ctx.fillRect(300, 200, 15, 100);
ctx.fillRect(200, 200, 60, 200);

ctx.arc(230, 150, 50, 0, 2 * Math.PI);
ctx.fill();

ctx.beginPath();
ctx.fillStyle = "white";
ctx.arc(250, 140, 8, Math.PI, 2 * Math.PI);
ctx.arc(210, 140, 8, Math.PI, 2 * Math.PI);
ctx.fill();
