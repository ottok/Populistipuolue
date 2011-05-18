function float2procent(value){
	return Math.round(value*100);
}

function svg_circle(radius){
	radius = radius*50+2;
	return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="80" height="80"><desc>Created by Otto</desc><defs></defs> \
<circle cx="40" cy="40" r="' + radius + '" fill="#1751a7" stroke="none" style="fill-opacity:0.8;" fill-opacity="1"></circle> \
</svg> \
';
}

function svg_importance(yes, na, no){
	yes = yes*200; // e.g. 0.33 becomes 33px*3 = 99px
	na = na*200;
	no = no*200;
	return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="200" height="55"><desc>SVG image</desc><defs></defs> \
<rect x="0" y="45" width="' + yes + '" height="10" r="0" rx="0" ry="0" fill="#000000" stroke="none" style="fill-opacity: 1; " fill-opacity="1"></rect> \
<rect x="' + yes + '" y="45" width="' + na + '" height="10" r="0" rx="0" ry="0" fill="#888" stroke="none" style="fill-opacity: 1; " fill-opacity="1"></rect> \
<rect x="' + (yes + na) + '" y="45" width="' + no + '" height="10" r="0" rx="0" ry="0" fill="#cccccc" stroke="none" style="fill-opacity: 1; " fill-opacity="1"></rect> \
</svg> \
';
}



/*
	return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100"><desc>Created by Otto</desc><defs></defs> \
	<path fill="#000000" stroke="none" d="M71.196,42.691C65.5685298,42.691,61.004999999999995,38.1274702,61.004999999999995,32.5C61.004999999999995,26.8725298,65.5685298,22.309,71.196,22.309C76.8234702,22.309,81.387,26.8725298,81.387,32.5C81.387,38.1274702,76.8234702,42.691,71.196,42.691M79.79846947102982,22.5A13.191,13.191,0,1,0,79.79846947102982,42.5L108.58299914550781,42.5L108.58299914550781,22.5L79.79846947102982,22.5" transform="" style="display: normal;"></path> \
<text x="93.4849995727539" y="36.5" text-anchor="middle" style="text-anchor: middle; font: normal normal normal 11px/normal sans-serif; display: normal;" font="11px sans-serif" stroke="none" fill="#ffffff" transform=""><tspan>263</tspan></text> \
<circle cx="71.19565217391305" cy="32.5" r="10" fill="#000000" stroke="none" style="fill-opacity: 0; " fill-opacity="0"></circle> \
</svg> \
';
*/

$(document).ready(function(){
    $.getJSON("index.json",function(data){ /* Django running, dynamic: /index.json OR Django not running, static: /index.json */
    
    // optional: sort questions by importance
    // data.sort(function(b,a) { return parseFloat(a.painoarvo.iso) - parseFloat(b.painoarvo.iso)});
    
		var items = [];

		for (i in data) {
			items.push('\
<a name="' + data[i]["nro"] + '"><h3> \
	' + data[i]["nro"] + '. ' + data[i]["kysymys"] + ' \
	<small>(n=' + data[i]["vastauksia"] + ')</small> \
</h3></a> \
<table> \
<tr> \
');

			for (x in data[i]["vastausvaihtoehdot"]) {
				items.push('\
	<td> \
	' + svg_circle(data[i]["vastausvaihtoehdot"][x][3]) + ' \
	</td> \
');
			}

			items.push('\
</tr> \
<tr> \
');

			for (x in data[i]["vastausvaihtoehdot"]) {
				items.push('\
	<td> \
	' + data[i]["vastausvaihtoehdot"][x][0] + '. ' + data[i]["vastausvaihtoehdot"][x][1] + '<br/> \
	<small>' + float2procent(data[i]["vastausvaihtoehdot"][x][3]) + '% (' + data[i]["vastausvaihtoehdot"][x][2] + ')</small><br/> \
	</td> \
');
			}

			items.push('\
</tr> \
</table> \
');

/*
<tr> \
	<td> \
	<small>Painoarvo: ' + svg_importance(data[i]["painoarvo"]["iso"][1], data[i]["painoarvo"]["normaali"][1], data[i]["painoarvo"]["pieni"][1]) + '<br/> \
	iso ' + float2procent(data[i]["painoarvo"]["iso"][1]) + '% (' + data[i]["painoarvo"]["iso"][0] + ') / \
	normaali ' + float2procent(data[i]["painoarvo"]["normaali"][1]) + '% (' + data[i]["painoarvo"]["normaali"][0] + ') / \
	pieni ' + float2procent(data[i]["painoarvo"]["pieni"][1]) + '% (' + data[i]["painoarvo"]["pieni"][0] + ') \
	</small> \
	</td> \
');
*/

		};

		$('<div/>', {
			'class': 'questions',
			html: items.join("\n")
		}).appendTo('#data');  
	});   
});
