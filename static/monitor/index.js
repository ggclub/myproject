<script type="text/javascript">
	$('.page_index').on('click', function() {
		var clicked = this.id;
		if(clicked === "prev"){

		}
		else if(clicked === "next"){

		}
		$.ajax({
			url: "/monitor/ajax_page_request/",
			type: "POST",
			// dataType: "json",
			data: {
				'csrfmiddlewaretoken': '{{ csrf_token }}',
				'page_no': {{ page_no }},
				'page_index': clicked,
			},
			success: function(data) {
				$("#right-log").html(data);
			}
		});
		return false;
	});

	// var reloadVar;
	// var reloadTime = 10000;
	// window.onload = $.fn.reloadFunc = function(){
	// 	reloadVar = setTimeout(reload, reloadTime);
	// }
	// function reload(){
	// 	$.ajax({
	// 		url: "/monitor/ajax_index_reload/",
	// 		type: "POST",
	// 		data : {
	// 			'csrfmiddlewaretoken': '{{ csrf_token }}',
	// 		},
	// 		success: function(data){
	// 			$("#left").html(data);
	// 			$.fn.reloadFunc();
	// 		}
	// 	});
	// 	return false;
	// }

	$('.btn-opMode').on('click', function setMode(){
		var opMode = this.innerText;
		$.ajax({
			url: "/monitor/ajax_set_operation_mode/",
			type: "POST",
			data: {
				'csrfmiddlewaretoken': '{{ csrf_token }}',
				'opMode': opMode,
			},
			success: function(data){
				$('.opMode').text('Mode: ' + data.opMode);
			}
		});
		return false;
	});







	
</script>

