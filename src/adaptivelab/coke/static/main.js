var coke = (function($) {
	var control = {
		error: function() {
			console.log("try again later message");
			$('#messages').replaceWith('<div class="span12" id="messages"><div class="alert span6"><p>OOPS! We failed to get messages<br/>Please try again later.</p></div></div>');
		},
		fetch: function() {
			var jqxhr = $.getJSON( "/api/messages/", function(data, textStatus, jqXHR ) {
	                console.debug( "success: "+data.length );
	                if(data.length > 0)
	                {
	                	var messages = '<div class="span12" id="messages">';
	                	for(x in data)
	                	{
	                		var sentiment = (data[x]['sentiment'] == 0 ? 'neutral' : (data[x]['sentiment'] > 0 ? 'positive' : 'negative'))
	                		messages += '<dl>';
	                		messages += '    <dt>' + data[x]['user_handle'] + ' <img src="http://adaptive-test-api.herokuapp.com/images/' + sentiment + '.png" /></dt>';
	                		messages += '    <dd>' + data[x]['message'] + ' <strong>' + data[x]['occurances'] + ' occurances</strong></dd>';
	                		messages += '</dl>';
	                	}
	                	messages += '</div>' 
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