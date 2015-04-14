(function($){
	
	$.fn.slideBox = function(params){
	
		var content0 = $(this).html();
		var defaults = {
			width: "526px",
			height: "200px",
			position: "bottom"			// Possible values : "top", "bottom"
		}
		
		// extending the fuction
		if(params) $.extend(defaults, params);
		
		var divPanel = $("<div class='slide-panel'>");
		var divContent = $("<div class='content0'>");
	
		$(divContent).html(content0);
		$(divPanel).addClass(defaults.position);
		$(divPanel).css("width", (526) + "px");
		
		// centering the slide panel
		$(divPanel).css("left", (100 - parseInt(defaults.width))/2 + "%");
	
		// if position is top we're adding 
		if(defaults.position == "top")
			$(divPanel).append($(divContent));
		
		// adding buttons
		$(divPanel).append("<div class='slide-button'><span class='open'><b>ОТКРЫТЬ</b></span></div>");
		$(divPanel).append("<div style='display: none' id='close-button' class='slide-button'><span class='open'><b>ЗАКРЫТЬ</b></span></div>");
		
		if(defaults.position == "bottom")
			$(divPanel).append($(divContent));
		
		$(this).replaceWith($(divPanel));
		
		// Buttons action
		$(".slide-button").click(function(){
			if($(this).attr("id") == "close-button")
				$(divContent).animate({height: "0px"}, 500);
			else
				$(divContent).animate({height: defaults.height}, 500);
			
			$(".slide-button").toggle();
		});
	};
	
})(jQuery);