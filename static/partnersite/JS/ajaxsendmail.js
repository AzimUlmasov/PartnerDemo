;(function($) {
    $.fn.ajaxsendmail = function() {
        var b = $(this)
          , value = b.serializeArray()
          , request = {
            'option': 'com_ajax',
            'module': 'tm_ajax_contact_form',
            'data': value,
            'format': 'raw'
        };
        $.ajax({
            type: 'POST',
            data: request,
            beforeSend: function() {
                b.find("div[id*=message]").addClass("l").removeClass("e").removeClass("c").removeClass("s")
            },
            success: function(a) {
                switch (a) {
                case 's':
                    b.find("div[id*=message]").removeClass("l").removeClass("e").removeClass("c").addClass("s").delay(2000).queue(function(n) {
                        $(this).removeClass("s");
                        n()
                    });
                    b.trigger('reset');
                    if (!$.support.placeholder) {
                        b.find('*[placeholder]').each(function(n) {
                            $(this).parent().find('>.form_placeholder').show()
                        })
                    }
                    break;
                default:
                    b.find("div[id*=message]").removeClass("l").removeClass("s").removeClass("c").addClass("e").find('span.e').append(a).delay(2000).queue(function(n) {
                        b.find("div[id*=message]").removeClass("e").find('span.e span').remove();
                        n()
                    });
                    break
                }
            }
        })
    }
}
)(jQuery);
