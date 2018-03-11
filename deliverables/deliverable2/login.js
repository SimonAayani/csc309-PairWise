function show_login(){

    if($(".container").is(":hidden")){
   		$(".container").fadeIn(300);
    	$(".login_info_div").show();
    }
    if($(".login_info_div").is(":hidden")){
    	$(".logindiv").fadeOut(300, function(){
    		$(".registerdiv").hide();
		    $(".login_info_div").show();
		    $(".logindiv").fadeIn(300);
    	});
    }
    
}
function login_goback(){
    $(".container").fadeOut(300, function(){
        $(".registerdiv").hide();
        $(".login_info_div").hide();
    });
    }

function show_register(){
	if($(".container").is(":hidden")){
		$(".container").fadeIn(300);
		$(".registerdiv").show();
    }
    if($(".registerdiv").is(":hidden")){
	    $(".logindiv").fadeOut(300, function(){
	    	$(".login_info_div").hide();
		    $(".registerdiv").show();
		    $(".logindiv").fadeIn(300);
	    });
    }

	
}