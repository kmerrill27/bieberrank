function upvote(div) {
  title = $(div).find("h3").text();
  $.post("/upvote", data={ "title": title },
    function(d) {
        // Since Datastore has some latency registering
        // the update, artificially increase the vote
        // count on the frontend. When the user next
        // refreshes the page, the actual count - as
        // read from Datastore - will appear.
        vote_text = $(div).find(".upvotes").text();
        vote_components = vote_text.split(" ");
        votes = parseInt(vote_components[1]) + 1;
        $(div).find(".upvotes").text(vote_components[0] + " " + votes);
      });
}
