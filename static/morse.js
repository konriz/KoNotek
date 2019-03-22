$(document).ready(function(){
    $("#to_code").parent().button('toggle');
});

$("#to_code").click(function(){
    $("#to_code").parent().button('toggle');
    $("#to_letters").parent().button('toggle');
});

$("#to_letters").click(function(){
    $("#to_letters").parent().button('toggle');
    $("#to_code").parent().button('toggle');
});