var coke = (function($) {
	var control = {
		error: function() {
			console.log("try again later message");
			// $('#messages').html('<div class="alert"><script type="text/javascript">document.write(\'<button type="button" class="close" data-dismiss="alert">&times;</button>\')</script><p>OOPS! We failed to get messages<br/>Please try again later.</p></div>');
		},
		fetch: function() {
			var jqxhr = $.getJSON( "/api/messages/", function(data, textStatus, jqXHR ) {
	                console.debug( "success: "+data.length );
	                if(data.length > 0)
	                {
	                	var messages = "";
	                	for(x in data)
	                	{
	                		messages += "<dl>";
	                		messages += "    <dt>" + data[x]['user_handle'] + " (" + data[x]['sentiment'] + "):</dt>";
	                		messages += "    <dd>" + data[x]['message'] + " <strong>" + data[x]['occurances'] + " occurances</strong></dd>";
	                		messages += "</dl>";
	                	}
	                	$('#messages').replaceWith(messages);
	                }
	                else
	                {
	                	control.error();
	                }
	                
              	})
                .done(function() {
                	console.log( "second success" );
                })
                .fail(function( jqxhr, textStatus, error ) {
	                var err = textStatus + ", " + error;
	                console.log( "Request Failed: " + err );
	                control.error();
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