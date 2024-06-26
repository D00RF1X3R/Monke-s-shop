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
var checkboxesU = document.getElementById("checkboxesU");
checkboxesU.style.display = "none";
var checkboxesC = document.getElementById("checkboxesC");
checkboxesC.style.display = "none";
var checkboxesS = document.getElementById("checkboxesS");
checkboxesS.style.display = "none";
var checkboxesP = document.getElementById("price-filter");
checkboxesP.style.display = "none";

var expandedU = false;
function showCheckboxesU() {
    var checkboxes = document.getElementById("checkboxesU");
    if (!expandedU) {
        checkboxes.style.display = "block";
        expandedU = true;
    } else {
        checkboxesU.style.display = "none";
        expandedU = false;
    }
}
var expandedC = false;
function showCheckboxesC() {
    var checkboxes = document.getElementById("checkboxesC");
    if (!expandedC) {
        checkboxes.style.display = "block";
        expandedC = true;
    } else {
        checkboxes.style.display = "none";
        expandedC = false;
    }
}
var expandedS = false;
function showCheckboxesS() {
    var checkboxes = document.getElementById("checkboxesS");
    if (!expandedS) {
        checkboxes.style.display = "block";
        expandedS = true;
    } else {
        checkboxes.style.display = "none";
        expandedS = false;
    }
}
var expandedP = false;
function showPriceFilter() {
    var checkboxes = document.getElementById("price-filter");
    if (!expandedP) {
        checkboxes.style.display = "block";
        expandedP = true;
    } else {
        checkboxes.style.display = "none";
        expandedP = false;
    }
}

