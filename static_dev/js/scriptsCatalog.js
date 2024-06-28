const body = document.getElementById("bodyCat");
const popularButtCat = document.getElementById("popularityButCat");
const popularityBlockCat = document.getElementById("popularityBlockCat");
const categoryButtCat = document.getElementById("categoryButCat");
const categoryBlockCat = document.getElementById("categoryBlockCat");
const universeButtCat = document.getElementById("universeButCat");
const universeBlockCat = document.getElementById("universeBlockCat");
const sellerButtCat = document.getElementById("sellerButCat");
const sellerBlockCat = document.getElementById("sellerBlockCat");
const priceButtCat = document.getElementById("priceButCat");
const priceBlockCat = document.getElementById("priceBlockCat");
const deliveryButtCat = document.getElementById("deliveryButCat");
const deliveryBlockCat = document.getElementById("deliveryBlockCat");


popularButtCat.addEventListener("click", event => {
    var status = document.getElementById("popularityBlockCat").style.display;
    var statusBody = document.getElementById("bodyCat").style.overflow;
    console.log(status);
    if(status == "none"){
        popularityBlockCat.style.display = "flex";
        categoryBlockCat.style.display = "none";
        universeBlockCat.style.display = "none";
        sellerBlockCat.style.display = "none";
        priceBlockCat.style.display = "none";
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        popularityBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
categoryButtCat.addEventListener("click", event => {
    if(categoryBlockCat.style.display == "none"){
        popularityBlockCat.style.display = "none";
        categoryBlockCat.style.display = "flex";
        universeBlockCat.style.display = "none";
        sellerBlockCat.style.display = "none";
        priceBlockCat.style.display = "none";
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        categoryBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
universeButtCat.addEventListener("click", event => {
    if(universeBlockCat.style.display == "none"){
        popularityBlockCat.style.display = "none";
        categoryBlockCat.style.display = "none";
        universeBlockCat.style.display = "flex";
        sellerBlockCat.style.display = "none";
        priceBlockCat.style.display = "none";
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        universeBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
sellerButtCat.addEventListener("click", event => {
    if(sellerBlockCat.style.display == "none"){
        popularityBlockCat.style.display = "none";
        categoryBlockCat.style.display = "none";
        universeBlockCat.style.display = "none";
        sellerBlockCat.style.display = "flex";
        priceBlockCat.style.display = "none";
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        sellerBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
priceButtCat.addEventListener("click", event => {;
    if(priceBlockCat.style.display == "none"){
        popularityBlockCat.style.display = "none";
        categoryBlockCat.style.display = "none";
        universeBlockCat.style.display = "none";
        sellerBlockCat.style.display = "none";
        priceBlockCat.style.display = "flex";
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        priceBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 
deliveryButtCat.addEventListener("click", event => {
    if(deliveryBlockCat.style.display == "none"){
        deliveryBlockCat.style.display = "flex";
        categoryBlockCat.style.display = "none";
        universeBlockCat.style.display = "none";
        sellerBlockCat.style.display = "none";
        priceBlockCat.style.display = "none";
        popularityBlockCat.style.display = "none";
        body.style.overflow = "hidden";

    } else {
        deliveryBlockCat.style.display = "none";
        body.style.overflow = "scroll";
    }
}); 