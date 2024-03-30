const images=[
    '01.jpg',
    '02.jpg',
    '03.jpg',
    '04.jpg',
    '05.jpg',
]
const chosenImage=images[Math.floor(Math.random()*images.length)];
// const bgImage=document.createElement('img');

// bgImage.src=`img/${chosenImage}`;

// document.body.appendChild(bgImage);

document.body.style.backgroundImage = `url(img/${chosenImage})`;
// document.body.style.backgroundPosition = "top";
document.body.style.backgroundRepeat = "no-repeat"; 
document.body.style.backgroundSize = "cover"; 
