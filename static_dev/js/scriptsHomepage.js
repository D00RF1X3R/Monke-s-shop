
const popularButt = document.getElementById("popularityBut");
const popularityBlock = document.getElementById("popularityBlock");
const categoryButt = document.getElementById("categoryBut");
const categoryBlock = document.getElementById("categoryBlock");
const universeButt = document.getElementById("universeBut");
const universeBlock = document.getElementById("universeBlock");
const sellerButt = document.getElementById("sellerBut");
const sellerBlock = document.getElementById("sellerBlock");
const priceButt = document.getElementById("priceBut");
const priceBlock = document.getElementById("priceBlock");
const deliveryButt = document.getElementById("deliveryBut");
const deliveryBlock = document.getElementById("deliveryBlock");
const body = document.getElementById("bodyHome");

popularButt.addEventListener("click", event => {
    var status = document.getElementById("popularityBlock").style.display;
    var statusBody = document.getElementById("bodyHome").style.overflow;
    console.log(status);
    if(status == "none"){
        popularityBlock.style.display = "flex";
        categoryBlock.style.display = "none";
        universeBlock.style.display = "none";
        sellerBlock.style.display = "none";
        priceBlock.style.display = "none";
        deliveryBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        popularityBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
categoryButt.addEventListener("click", event => {
    if(categoryBlock.style.display == "none"){
        popularityBlock.style.display = "none";
        categoryBlock.style.display = "flex";
        universeBlock.style.display = "none";
        sellerBlock.style.display = "none";
        priceBlock.style.display = "none";
        deliveryBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        categoryBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
universeButt.addEventListener("click", event => {
    if(universeBlock.style.display == "none"){
        popularityBlock.style.display = "none";
        categoryBlock.style.display = "none";
        universeBlock.style.display = "flex";
        sellerBlock.style.display = "none";
        priceBlock.style.display = "none";
        deliveryBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        universeBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
sellerButt.addEventListener("click", event => {
    if(sellerBlock.style.display == "none"){
        popularityBlock.style.display = "none";
        categoryBlock.style.display = "none";
        universeBlock.style.display = "none";
        sellerBlock.style.display = "flex";
        priceBlock.style.display = "none";
        deliveryBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        sellerBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
priceButt.addEventListener("click", event => {;
    if(priceBlock.style.display == "none"){
        popularityBlock.style.display = "none";
        categoryBlock.style.display = "none";
        universeBlock.style.display = "none";
        sellerBlock.style.display = "none";
        priceBlock.style.display = "flex";
        deliveryBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        priceBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
deliveryButt.addEventListener("click", event => {
    if(deliveryBlock.style.display == "none"){
        deliveryBlock.style.display = "flex";
        categoryBlock.style.display = "none";
        universeBlock.style.display = "none";
        sellerBlock.style.display = "none";
        priceBlock.style.display = "none";
        popularityBlock.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        deliveryBlock.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 


