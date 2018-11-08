$(document).ready(function(){
	if ($('body').height() < $(window).height()) {
		$('.footer').css({'position':'absolute', 'botton':'0px'});
	} else {
		$('.footer').css({"position":"relative"});
	}
});

$('.menu-bar').on('click', function() {
    $('.contendor-info').toggleClass('changes-info');
    $('.contenido').toggleClass('abrir');
});
