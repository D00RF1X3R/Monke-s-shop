function favoriteColor(button){
    var svg = document.getElementsByClassName("main_products_card_favorite__image")[0];
    console.log(svg);
    if (document.svg == "black"){
        svg.fill  = "red";
    } else {
        svg.fill = "black";
    }
    return false;
}
