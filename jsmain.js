
function greeting(){
var userName = $('#username').val();
$("#greetings").append("welcome " + userName + " ! <br> "  );

}

function setup()
{
$("#ok_button").click(greeting);



}
$(document).ready(setup);
