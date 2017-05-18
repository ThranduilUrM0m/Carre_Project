var total_height = document.documentElement.clientHeight - ($('.header').height());
$('.first_section').height(total_height);

function doSomething() {
    $('.s_x').html($('.carousel-item.active img').attr('alt')+' 2017');
}

setInterval(doSomething, 1); // Time in milliseconds

String.prototype.replaceAt=function(index, replacement) {
    return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
}

$('#nav1').hide();
$('#nav2').hide();
$('#nav3').hide();
$('#nav4').hide();
$('#nav5').hide();
$('#nav6').hide();
$('#nav7').hide();
$('#nav8').hide();

$('.header #products_menu .nav-item').hover(
  function() {
	var categorie_name = $(this).find("span").html();
	if(categorie_name === 'Collection S. Bains'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').show();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Sanitaire'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').show();
	}
	else if(categorie_name === 'Baignoires &amp; Receveurs'){
		$('#nav1').hide();
		$('#nav2').show();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Miroirs'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').show();
		$('#nav7').hide();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Meubles S.D.B.'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').show();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Eviers en Inox'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').show();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Robinetterie'){
		$('#nav1').hide();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').show();
		$('#nav8').hide();
	}
	else if(categorie_name === 'Accessoires S.D.B.'){
		$('#nav1').show();
		$('#nav2').hide();
		$('#nav3').hide();
		$('#nav4').hide();
		$('#nav5').hide();
		$('#nav6').hide();
		$('#nav7').hide();
		$('#nav8').hide();
	}
  }, function() {
	$('#nav1').hide();
	$('#nav2').hide();
	$('#nav3').hide();
	$('#nav4').hide();
	$('#nav5').hide();
	$('#nav6').hide();
	$('#nav7').hide();
	$('#nav8').hide();
  }
);

/*$('.list_subcategories').hide();*/

/*$(document).on("mouseenter", ".sanitaire_item", function() {
    var sub_categorie_name = $(this).find('span').html();
	if(sub_categorie_name == "Vasque"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Metal-Line">Metal-Line</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="A Encastrer">A Encastrer</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Sous-Plan">Sous-Plan</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Semi-Encastrées">Semi-Encastrées</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="A Poser">A Poser</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="A Poser sur Meuble">A Poser sur Meuble</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Lave-Mains">Lave-Mains</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Muraux">Muraux</span></a></li>');
	}
	else if(sub_categorie_name == "Bloc WC"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Arq">Arq</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Noble">Noble</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Eos">Eos</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Universal">Universal</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Klea">Klea</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Emma Square">Emma Square</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Emma">Emma</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Mid">Mid</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Smart">Smart</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Jazz">Jazz</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Street Square">Street Square</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Street">Street</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Elia">Elia</span></a></li>');
	}
	else if(sub_categorie_name == "Bidet"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Arq">Arq</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Noble">Noble</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Eos">Eos</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Universal">Universal</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Klea">Klea</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Emma Square">Emma Square</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Emma">Emma</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Mid">Mid</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Smart">Smart</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Jazz">Jazz</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Street Square">Street Square</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Street">Street</span></a></li>');
		$('.list_subcategories').append('<li class="sanitaire link link--kumya"><a href="#"><span data-letters="Elia">Elia</span></a></li>');
	}
	$('.list_subcategories').show();
});*/


$('.overlay_nav').hover(
  function() {
	$(this).show();
  }, function() {
	$(this).hide();
  }
);

$('.second_section_column_article').hover(
  function() {
	$(this).find('.overlay').css('height', '100%');
  }, function() {
	$(this).find('.overlay').css('height', '0');
  }
);

var one = $('.carousel-control-next').css('width');
var two = $('#carouselExampleControls').css('width');
var three = two - one;
$('.overlay').css('right', one);

//<![CDATA[
$(window).on('load', function() { // makes sure the whole site is loaded
    $('.demo-1').delay(2000).fadeOut('slow'); // will fade out the white DIV that covers the website.
    if(window.location.href.search('#') != -1){
    	var anchor = window.location.href.split('#').pop();
    	var element_anchor = $('#'+anchor);
    	if(element_anchor.parent().parent().attr('class').search('sublinks') !=-1){
    		$('html, body').animate({
		        scrollTop: element_anchor.parent().parent().prev().find('h4').offset().top
		    }, 100);
    		element_anchor.parent().parent().addClass('show');
    		element_anchor.parent().next().addClass('show');
    	}
    }
})
//]]>

var temp = '';
$('#contactSubmit input, #contactSubmit textarea').focusout(function(event) {
    if(!$(this).val()){
    	temp = '';
    }else{
    	temp = $(this).parent().find('label').find('span').html();
    	$(this).parent().find('label').find('span').html($(this).val());
    }
});
$('#contactSubmit input, #contactSubmit textarea').focusin(function(event) {
    if(!$(this).val()){
    	temp = '';
    }else{
    	$(this).parent().find('label').find('span').html(temp);
    }
});

$('.list-group-item').click(function(){
	var its = $($(this).attr("data-target"));
	var its_parent = $($(this).attr("data-target")).parent();
	if(its.attr('class').search('show') == -1){
		if(its_parent.attr('class').search('show') == -1){
			$('.sublinks').not(its).removeClass('show', 5000);
		}else{
			$('.sublinks').not(its_parent, its).removeClass('show', 5000);
		}
	}
});

$(".list-group-item").click(function() {
	var its = $($(this).attr("data-target"));
	var its_parent = $($(this).attr("data-target")).parent();
	if(its_parent.attr('class').search('show') != -1){
		$('html, body').animate({
	        scrollTop: its_parent.prev().offset().top
	    }, 100);
	}else{
		$('html, body').animate({
	        scrollTop: $(this).offset().top
	    }, 100);
	}
});