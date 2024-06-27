var checkboxesU = document.getElementById("checkboxesU");
checkboxesU.style.display = "none";
var checkboxesC = document.getElementById("checkboxesC");
checkboxesC.style.display = "none";
var checkboxesS = document.getElementById("checkboxesS");
checkboxesS.style.display = "none";
var checkboxesP = document.getElementById("price-filter");
checkboxesP.style.display = "none";

function addFavorite(clickedElement){
    var frm = $(clickedElement).parent();
    var button = $(clickedElement);
    var data = $(frm).serialize() + '&' + 'type=favorite';
    var svg = document.getElementById("favorite_image");
    console.log(svg);
    if (svg.style == "black"){
        svg.style.fill  = "red";
    } else {
        svg.style.fill = "black";
    }
    $.ajax({
        type: 'POST',
        data: data,
        url: '',
        success:  function (data) {
            console.log("OK Adding");
        },
        error: function () {
            console.log('I want to die');
        }
    });
    return false;
}

function addCart(clickedElement){
    var frm = $(clickedElement).parent();
    var button = $(clickedElement);
    var data = $(frm).serialize() + '&' + 'type=to_cart';
    console.log("Data object is:", data);
    $.ajax({
        type: 'POST',
        data: data,
        url: '',
        success:  function (data) {
            console.log("OK Adding");
        },
        error: function () {
            console.log('I want to die');
        }
    });
    return false;
}

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

