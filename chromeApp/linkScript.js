$(".clickable-row").click(function() {
		console.log("at least im trying..")
		window.location = $(this).data("href");
	});
