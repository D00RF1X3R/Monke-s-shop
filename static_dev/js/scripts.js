var checkboxesU = document.getElementById("checkboxesU");
checkboxesU.style.display = "none";
var checkboxesC = document.getElementById("checkboxesC");
checkboxesC.style.display = "none";
var checkboxesS = document.getElementById("checkboxesS");
checkboxesS.style.display = "none";
var checkboxesP = document.getElementById("price-filter");
checkboxesP.style.display = "none";
var checkboxesPop = document.getElementById("populate-filter");
checkboxesPop.style.display = "none";

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
var buttonU = document.getElementById("btn-u");
buttonU.style['border-radius'] = '10px 10px 10px 10px';
function showCheckboxesU() {
    var checkboxes = document.getElementById("checkboxesU");
    if (!expandedU) {
        buttonU.style['border-radius'] = '10px 10px 0 0';
        checkboxes.style.display = "block";
        expandedU = true;
    } else {
        buttonU.style['border-radius'] = '10px 10px 10px 10px';
        checkboxes.style.display = "none";
        expandedU = false;
    }
}
var expandedC = false;
var buttonC = document.getElementById("btn-c");
buttonC.style['border-radius'] = '10px 10px 10px 10px';
function showCheckboxesC() {
    var checkboxes = document.getElementById("checkboxesC");
    if (!expandedC) {
        buttonC.style['border-radius'] = '10px 10px 0 0';
        checkboxes.style.display = "block";
        expandedC = true;
    } else {
        buttonC.style['border-radius'] = '10px 10px 10px 10px';
        checkboxes.style.display = "none";
        expandedC = false;
    }
}

var expandedS = false;
var buttonS = document.getElementById("btn-s");
buttonS.style['border-radius'] = '10px 10px 10px 10px';
function showCheckboxesS() {
    var checkboxes = document.getElementById("checkboxesS");
    if (!expandedS) {
        buttonS.style['border-radius'] = '10px 10px 0 0';
        checkboxes.style.display = "block";
        expandedS = true;
    } else {
        buttonS.style['border-radius'] = '10px 10px 10px 10px';
        checkboxes.style.display = "none";
        expandedS = false;
    }
}
var expandedP = false;
var buttonP = document.getElementById("btn-price");
buttonP.style['border-radius'] = '10px 10px 10px 10px';
function showBlockPrice() {
    var checkboxes = document.getElementById("price-filter");
    if (!expandedP) {
        buttonP.style['border-radius'] = '10px 10px 0 0';
        checkboxes.style.display = "block";
        expandedP = true;
    } else {
        buttonP.style['border-radius'] = '10px 10px 10px 10px';
        checkboxes.style.display = "none";
        expandedP = false;
    }
}

var expandedPopulate = false;
var buttonPopulate = document.getElementById("btn-populate");
buttonPopulate.style['border-radius'] = '10px 10px 10px 10px';
function showBlockPopulate() {
    var checkboxes = document.getElementById("populate-filter");
    if (!expandedPopulate) {
        buttonPopulate.style['border-radius'] = '10px 10px 0 0';
        checkboxes.style.display = "block";
        expandedPopulate = true;
    } else {
        buttonPopulate.style['border-radius'] = '10px 10px 10px 10px';
        checkboxes.style.display = "none";
        expandedPopulate = false;
    }
}

