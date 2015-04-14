[head]
<style type="text/css"> 
		
			ul.ns_hierarchy li{
				clear: both;
			}
			ul.ns_hierarchy, ul.ns_hierarchy ul{
				list-style-type: none;
				margin: 0;
				padding-top: 5px;
				padding-bottom: 5px;	
				padding-left: 0px;
			}
			ul.ns_hierarchy{
				padding-left: 22px;
			}
			ul.ns_hierarchy ul{
				padding-left: 22px;
			}
			li.nsh_closed span, li.nsh_opened span{
				float: left;
				position: absolute;
				width: 13px;
				height: 13px;
				margin: 0px 3px 3px -17px;	
				cursor: pointer;
				overflow: hidden;
				font: normal 0.8em/0.8em sans-serif;	
			}
			li.nsh_closed span em, li.nsh_opened span em{
				position: absolute;
				width: 13px;
				height: 13px;
				top: 0;
				left: 0;
				background: url({THEME}/images/plus.png) no-repeat;
			}
			li.nsh_closed span em{
				background-position: bottom;
			}
	  		.ns_hierarchy span{
			 cursor: pointer;
			}
			.ns_hierarchy span:hover{
			 text-decoration:underline;
			}
</style> 
<table width="100%" align="left" varign="top" border="0" cellspacing="0" cellpadding="0">
	<tr>
		<td id="one" align="left" style="padding:0px 2px 8px 38px;"><a href="http://irkonline.info"><img src="{THEME}/images/irkonline_m.png" border="0" title="Перейти на главную страницу irkonline.info | Цены в Иркутске" alt="irkonline.info | Цены в Иркутске"></a>
		</td>
		<td id="two" align="left" valign="middle" style="padding:2px 5px 10px 0px">
			<script type="text/javascript" src="{THEME}/catalogue/js/ajax_search.js"></script>
				<form action="http://irkonline.info" method="post" id="sformLSxHuhuOeg">
				<input type="hidden" name="do"  value="catalogue">
				<input type="hidden" name="act"  value="search">
				<input type="hidden" name="show"  value="offer">
				<input type="search" autofocus size="64" style="font-size:18px; padding: 2px 0 2px 3px; maxlength="150; font-family: Tahoma; width: 200px"; maxlength="200" name="search_title" id="search_title" value="" onkeyup = "autoquerylist(this.value)" onfocus="if(this.value==''){this.value='';}" onblur="if(this.value==''){this.value='';}"/>
				<input type="submit" name="searchbottom" title="Поиск" value="Поиск" />
				</form>
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td align="left">
			[sort_head]
			[not-view_full]
			<span class="c_grey">Результатов поиска: {search_count}</span> 
[/not-view_full]
[/sort_head]
</td>
</tr>
<tr>
<td align="right">
</td>
<div class="top10px">
<div class="mh1bg_cat">
[search]
[/search]
<td align="right" class="phed1">
[sort_head]
[not-view_full]
Сортировать по: 
<select onchange="document.location=this.options[this.selectedIndex].value">
<option value="{sort_views} {sort_views_active}">Релевантности</option>
<option value="{sort_price}">Цене (по убыванию)</option>
<option value="{sort_name} {sort_name_active}">Названию</option>
</select>
&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
[/not-view_full]
[/sort_head]
</td>
 </div> 
	</td>
</div>
</div>
</tr>
<br />
<tr>
<td valign="top">
</td>
<td valign="top">
<div class="menubg_cat">
<table width="100%" cellspacing="0" cellpadding="0" border="0"> 
<tr>
<td>&nbsp</td>
<td>
<table width="90%" cellspacing="0" cellpadding="0" border="0" class="tabimg"> 
</search>
[/head]
[products]
[view_all]
<tr>
	<td valign="top" class="pcheck"></td>
	<td valign="top" class="pimage"><a href="{obzor_url}"><img src="{img}" alt="" title="" target="_blank" border="0" width="150" height="150"></a></td>
	<td width="100%" class="pdescr"><strong class="pname"><a href="{obzor_url}" target="_blank">{title_product}</a></strong><div>{snippet}</div>
	{descr2}
	<div class="prate"><strong>Магазин:</strong> <span class="vend_green">{vendor}</span></ br>
</div>

</td>
	<td class="poffers">
	[prices]
	<div class="pprice">{g_price}p.</div><input type="button" value="Показать" onclick="window.location.href='{obzor_url}'";></br>
	[/prices]
	[noprices]
	[/noprices]
	</td>
<td>&nbsp&nbsp</td>
</tr>
<tr>
	<td valign="top" class="pline" colspan="4"><img src="{THEME}/catalogue/files/s.gif" alt="" width="1" height="1" border="0"></td>
</tr>
[/view_all]
[view_list]
<td valign="top" width="25%" align="center"><a href="{good_url}" title="{title_product}"><img src="{img}" border="0" alt="{title_product}"></a><br /><a href="{good_url}" title="{title_product}">{title_product}</a><br />{rating}<br />{compare_price_list}</td>
{newline}
[/view_list]
[view_full]
{brand_name}
<tr>
<td valign="top" style="padding-left: 15px;"><a href="{good_url}" title="{title_product}">{title_product}</a></td>
</tr>
[/view_full]
[/products]
[noproducts]
<p><strong>Извините, мы не можем найти модели соответствующие вашему запросу.</strong></p>
<p>Скорее всего вы задали слишком жёсткие условия поиска. Попробуйте убрать или изменить один или несколько параметров подбора.</p>
<p><br>Если вы уверены, что в каталоге есть модели соответствующие вашему запросу, но они не выводятся - <a href="{site_url}index.php?do=feedback">сообщите</a> нам об этом. Спасибо!</p>
[/noproducts]
[footer]
</table>
</td>
</tr>
</table>
</div>
</td>
<td valign="top">
<div class="menubg_cat">
<table width="100%" cellspacing="0" cellpadding="0" class="pstable">
<tr>
<td>
<script type="text/javascript"><!--
google_ad_client = "ca-pub-9692610173697432";
/* 120x600_2 */
google_ad_slot = "2965399328";
google_ad_width = 120;
google_ad_height = 600;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
</td>
</tr>
</table>
</div>
</td>
</tr>
<tr>
<td>
</td>
<td>
[not-view_full]
<table width="90%" cellspacing="0" cellpadding="0" border="0" class="phed">
<tr>
	<td><strong>Страницы:{pages}</strong></td>
	<td align="right"><strong>{prev_page} {next_page}</strong></td>
</tr>
</table>
[/not-view_full]
</div>

	</td>
</tr>
</table>
            <script>
function par(par_id){
    window.open('{site_url}index.php?do=good&param='+par_id+'','','width=450,height=350,resizable');
}
            </script>
[/footer]
