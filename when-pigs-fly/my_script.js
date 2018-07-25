function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}


function right(){

$("#pig").animate({left: '550px'});

}

function left(){

$("#pig").animate({right: '550px'});

}




function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flypig").click(right);
    $("#flpig").click(left);
}

$(document).ready(setup);
