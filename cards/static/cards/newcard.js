var s,
NewCard = {

  settings: {
  	example : 5,
    jNewCardSubmit : $("#new-card-submit"),
    jNewCardForm : $("#new-card-form"),
    jNewCardDialog : $("#new-card-modal"),
    jNewSourcePopover : $("#new-source-popover"),
    jNewSourceSubmit : $("#new-source-submit"),
    jNewSourceForm : $("#new-source-form"),
    jNewSourceTitle : $("#title-input"),
  },

  init: function() {
    s = this.settings;    
    this.bindUIActions();
  },

  bindUIActions: function() {
	s.jNewCardSubmit.on("click", function() {
		s.jNewCardForm.submit();
	});
	s.jNewCardForm.on("submit", function() {
		event.preventDefault();
		NewCard.sendCardData($(this));
		return false;
	});
	s.jNewSourceSubmit.on("click", function() {
		s.jNewSourceForm.submit();
	});
	s.jNewSourceForm.on("submit", function() {
		event.preventDefault();
		NewCard.sendSourceData($(this));
		return false;
	});
	popover_options = {
		html : true,
		content: function() {
        	return $('#new-source-popover-content').html();
        },
        container: '#new-source-container'
	};
	s.jNewSourcePopover.popover(popover_options);
	s.jNewSourcePopover.on('shown.bs.popover', function () {
  		s.jNewSourceTitle.focus();
	});
  },

  sendCardData: function(form) {
  	// TODO: Loading Indicator
  	s.jNewCardSubmit.button('loading');
  	data = form.serialize();  	
    url = form.attr( "action" ); 

  	$.post(url, data, function(res){
  		s.jNewCardSubmit.button('reset');
  		if (!!res) {
  			NewCard.processCardResponse(res);
  		} else {
  			NewCard.processFailure(res);
  		}        
        // TODO: Don't forget to hide the loading indicator!
    });
  },

  processCardResponse: function(res) {
  	s.jNewCardDialog.modal('hide');
  	s.jNewCardForm.trigger('reset');
  },

  sendSourceData: function(form) {
  	// TODO: Loading Indicator
  	s.jNewSourceSubmit.button('loading');
  	data = form.serialize();  	
    url = form.attr( "action" ); 

  	$.post(url, data, function(res){
  		s.jNewSourceSubmit.button('reset');
  		if (!!res) {
  			NewCard.processSourceResponse(res);
  		} else {
  			NewCard.processFailure(res);
  		}        
        // TODO: Don't forget to hide the loading indicator!
    });
  },

  processSourceResponse: function(res) {
  	s.jNewSourcePopover.popover('hide')
  	s.jNewSourceForm.trigger('reset');
  },

  processFailure: function(res) {  }

};