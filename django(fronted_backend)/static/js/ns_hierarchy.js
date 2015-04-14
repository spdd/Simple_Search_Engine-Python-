$(document).ready(function()
{
	$("ul.ns_hierarchy li:has(ul)").prepend("<span>+<em><!----></em></span>");
	$("ul.ns_hierarchy li:has(ul)").addClass("nsh_closed");
	$("ul.ns_hierarchy li > ul").hide();
	$("ul.ns_hierarchy li > span").click(function()
	{
		if( $(this).parent("li").attr("class") == "nsh_closed" )
		{
			$(this).parent("li").attr("class", "nsh_opened");
			$(this).html("&minus;<em><!----></em>");
			$(this).next("ul").show();
		}
		else if( $(this).parent("li").attr("class") == "nsh_opened" )
		{
			$(this).parent("li").attr("class", "nsh_closed");
			$(this).html("+<em><!----></em>");
			$(this).next("ul").hide();
		}
	});	
});