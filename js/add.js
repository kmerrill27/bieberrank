$(document).ready(function() {
  // Display a preview of the GIF when a URL is pasted in the text box.
  $("#gif").bind('paste', function(e) {
    if ($("#preview").length) {
      // If a preview already exists, clear it first.
      $("#preview").remove()
    }
    url = e.originalEvent.clipboardData.getData('Text');
    $("#gifcontainer").append("<img id='preview' src='" + url + "'</>");
  });
});
