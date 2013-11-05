var coke = (function($) {
	var control = {
		fetch: function() {
			var jqxhr = $.getJSON( "/api/messages/", function(data, textStatus, jqXHR ) {
	                console.log( "success" );
              	})
                .done(function() {
                	console.log( "second success" );
                })
                .fail(function( jqxhr, textStatus, error ) {
	                var err = textStatus + ", " + error;
	                console.log( "Request Failed: " + err );
	                // TODO Failure message to screen
                })
                .always(function() {
                	console.log( "complete" );
                });
		}
	};
	return {
        execute: function() {
            console.debug("setting up");
            $("button").click(function(e) {
                control.fetch();
            });
        }
	};
})(jQuery)