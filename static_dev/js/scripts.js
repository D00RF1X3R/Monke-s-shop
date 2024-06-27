const MyButton = document.getElementById("cardOne");

MyButton.addEventListener("click", event => {
    event.target.style.fill = "red";
}); 
const popularButt = document.getElementById("popularityBut");
const popularityBlock = document.getElementById("popularityBlock");
const body = document.getElementById("body");

// popularButt.addEventListener("click", event => {
//     popularityBlock.style.display = "flex";
// }); 

popularButt.addEventListener("click", event => {
    var status = document.getElementById("popularityBlock").style.display;
    var statusBody = document.getElementById("body").style.overflow;
    console.log(status);
    console.log(statusBody);
    if(status == "none"){
        popularityBlock.style.display = "flex";
        body.style.overfolw = "hidden";

    } else {
        popularityBlock.style.display = "none";
        body.style.overfolw = "scroll";
    }
}); 