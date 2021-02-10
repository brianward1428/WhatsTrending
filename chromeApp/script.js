
/*
Render Product Hunt Tending Data

Note:
This is not the best design as there is a lot of code repetition.
I chose to write separate functions for each table for readability and encapsulation purposes.
For example if the data displayed from productHunt were to change, I would only have to change
the renderPH function without having to worry about any of the other table renderings being compromised.
*/
function renderPH(streamIN) {

    $('tr.ph-added').remove();

    for (let row of streamIN) {
        // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.ph-template').clone();
        $newRow.removeClass('ph-template').removeClass('d-none').addClass('ph-added');
        // fill in our data
        $newRow.find('.ph-template-name').html("<a href='" + row.link +"'> " + row.name + "</a>");
        $newRow.find('.ph-template-description').html(row.description);
        $newRow.find('.ph-template-upvotes').html(row.upvotes);
        // append our new row
        $('tbody.ph-body').append($newRow);
    }
}

/*
Render Google Search Tending Data
*/
function renderGS(streamIN) {

    $('tr.gs-added').remove();

    for (let row of streamIN) {
      // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.gs-template').clone();
        $newRow.removeClass('gs-template').removeClass('d-none').addClass('gs-added');
        // fill in our data
        $newRow.find('.gs-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.gs-template-searchcount').html(row.searchCount);
        // append our new row
        $('tbody.gs-body').append($newRow);
    }
}

/*
Render YouTube Tending Data
*/
function renderYT(streamIN) {

    $('tr.yt-added').remove();

    for (let row of streamIN) {

      // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.yt-template').clone();
        $newRow.removeClass('yt-template').removeClass('d-none').addClass('yt-added');
        // fill in our data
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
        // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.ra-template').clone();
        $newRow.removeClass('ra-template').removeClass('d-none').addClass('ra-added');
        // fill in our data
        $newRow.find('.ra-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.ra-template-subscribers').html(row.subscribers);
        $('tbody.ra-body').append($newRow);
    }
}

function renderRG(streamIN) {

    $('tr.rg-added').remove();

    for (let row of streamIN) {

        // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.rg-template').clone();
        $newRow.removeClass('rg-template').removeClass('d-none').addClass('rg-added');
        // fill in our data
        $newRow.find('.rg-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.rg-template-growth').html(row.growth);
        $('tbody.rg-body').append($newRow);
    }
}

function renderSUB(streamIN) {

    $('tr.sub-added').remove();

    for (let row of streamIN) {

        // will need to make the first template row hidded (d-none) and then remove that class for our cloned rows.
        let $newRow = $('.sub-template').clone();
        $newRow.removeClass('sub-template').removeClass('d-none').addClass('sub-added');
        // fill in our data
        $newRow.find('.sub-template-title').html("<a href='" + row.link +"'> " + row.title + "</a>");
        $newRow.find('.sub-template-subs').html(row.subscribers);
        $('tbody.sub-body').append($newRow);
    }
}

/*
Make our API calls.

Note:
Again, all of these calls could have been simplfied by creating a function that makes the api request and then calls
the appropriate render function, but I chose to keep them all seperate for readability and simplicity.

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
};
