let saveEl = document.getElementById("save-el");
let countEl = document.getElementById("count-el");
let count = 0;
let counterText = document.getElementById("count-el");
let changes = document.querySelector("body");
let lis = ["green", "blue"];
//------------------------

function increment() {
  count += 1;
  countEl.textContent = count;
}

function save() {
  let countStr = count + " - ";
  if (parseInt(countEl.innerText) > 0) {
    console.log("bigger than 0");
  } else if (parseInt(countEl.innerText) == 0) {
    console.log("is zero");
  } else {
    console.log("less than 0");
  }
  saveEl.textContent += countStr;
  countEl.textContent = 0;
  count = 0;
}

function decrement() {
  count -= 1;
  countEl.textContent = count;
}



function randomColor() {
  let lll = lis[Math.floor(Math.random() * lis.length)];
  console.log(Math.random() * lis.length);
  return lis[Math.floor(Math.random() * lis.length)];
}

function lol() {
  console.log(randomColor());
  changes.style.backgroundColor = randomColor();
  count++;
  counterText.innerText = count;
  console.log(count);
}

if (typeof countEl.innerText === "string") {
  console.log("The variable is a string.");
} else {
  console.log("The variable is not a string.");
}
