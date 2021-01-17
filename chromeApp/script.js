
/*
Render Product Hunt Tending Data
*/
function renderPH(streamIN) {

    $('tr.ph-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.ph-template').clone();
        $newRow.removeClass('ph-template').removeClass('d-none').addClass('ph-added');
		// $newRow.attr('href', row.link)
        $newRow.find('.ph-template-name').html("<a href='" + row.link +"'> " + row.name + "</a>");
        $newRow.find('.ph-template-description').html(row.description);
        $newRow.find('.ph-template-upvotes').html(row.upvotes);
        $('tbody.ph-body').append($newRow);
    }
}

/*
Render Google Search Tending Data
*/
function renderGS(streamIN) {

    $('tr.gs-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.gs-template').clone();
        $newRow.removeClass('gs-template').removeClass('d-none').addClass('gs-added');
		// $newRow.attr('data-href', row.link)
        $newRow.find('.gs-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.gs-template-searchcount').html(row.searchCount);
        $('tbody.gs-body').append($newRow);
    }
}

/*
Render YouTube Tending Data
*/
function renderYT(streamIN) {

    $('tr.yt-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.yt-template').clone();
        $newRow.removeClass('yt-template').removeClass('d-none').addClass('yt-added');
		// $newRow.attr('data-href', row.link)
        $newRow.find('.yt-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.yt-template-info').html(row.info);
        $('tbody.yt-body').append($newRow);
    }
}

/*
Render Product Hunt Tending Data
*/
function renderRA(streamIN) {

    $('tr.ra-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.ra-template').clone();
        $newRow.removeClass('ra-template').removeClass('d-none').addClass('ra-added');
		// $newRow.attr('data-href', row.link)
        $newRow.find('.ra-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.ra-template-subscribers').html(row.subscribers);
        $('tbody.ra-body').append($newRow);
    }
}

function renderRG(streamIN) {

    $('tr.rg-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.rg-template').clone();
        $newRow.removeClass('rg-template').removeClass('d-none').addClass('rg-added');
		// $newRow.attr('data-href', row.link)
        $newRow.find('.rg-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.rg-template-growth').html(row.growth);
        $('tbody.rg-body').append($newRow);
    }
}

function renderSUB(streamIN) {

    $('tr.sub-added').remove();

    for (let row of streamIN) {
        // dataHtml += `<tr class="table-row"> <td> ${user.username} </td> <td> ****** </td> <td> ${user.firstname} </td> <td> ${user.lastname} </td> <td> ${user.role} </td> </tr>`;
        // TODO: we might not be cloning event listeners!!!
        //TODO will need to make the first template one hidded and then remove that class
        let $newRow = $('.sub-template').clone();
        $newRow.removeClass('sub-template').removeClass('d-none').addClass('sub-added');
		// $newRow.attr('data-href', row.link)
        $newRow.find('.sub-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.sub-template-subs').html(row.subscribers);
        $('tbody.sub-body').append($newRow);
    }
}
/*
LETS SEE IF WE CAN access our api
*/

window.onload = () => {

	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/ProductHuntElement/ProductHuntElement/?format=json",
		dataType: "json",
		success : function (dataPH) {

			renderPH(dataPH)
		}
	});



	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/GoogleSearchElement/GoogleSearchElement/?format=json",
		dataType: "json",
		success : function (dataGS) {

			renderGS(dataGS)

		}
	});

	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/YouTubeElement/YouTubeElement/?format=json",
		dataType: "json",
		success : function (dataYT) {

			renderYT(dataYT)

		}
	});

	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/RedditActivityElement/RedditActivityElement/?format=json",
		dataType: "json",
		success : function (dataRA) {

			renderRA(dataRA)

		}
	});

	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/RedditGrowthElement/RedditGrowthElement/?format=json",
		dataType: "json",
		success : function (dataRG) {

			renderRG(dataRG)

		}
	});

	$.ajax({
		url : "https://calm-dusk-59271.herokuapp.com/api/RedditSubscribersElement/RedditSubscribersElement/?format=json",
		dataType: "json",
		success : function (dataSUB) {

			renderSUB(dataSUB)

		}
	});


	$(".clickable-row").click(function() {
			console.log("at least im trying..")
	        window.location = $(this).data("href");
	    });

};
