function upvote(div) {
  title = $(div).find("h3").text();
  $.post("/upvote", data={ "title": title },
    function(d) {
        window.location.reload();
      });
}
