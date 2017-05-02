var total_height = document.documentElement.clientHeight - ($('.header').height());
$('.first_section').height(total_height);

function doSomething() {
    $('.s_x').html($('.carousel-item.active img').attr('alt')+' 2017');
}

setInterval(doSomething, 1); // Time in milliseconds

String.prototype.replaceAt=function(index, replacement) {
    return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
}
$('.overlay_nav').hide();
$('.header #products_menu .nav-item').hover(
  function() {
	var categorie_name = $(this).find("span").html();
	if(categorie_name === 'Collection S. Bains'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"8"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"j"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Arq">Arq</span></span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Noble">Noble</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Eos">Eos</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Universal">Universal</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Klea">Klea</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Emma Square">Emma Square</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Emma">Emma</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Mid">Mid</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Smart">Smart</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Jazz">Jazz</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Street Square">Street Square</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Street">Street</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Elia">Elia</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Sanitaire'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"1"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a class="sanitaire_item" href="#"><span data-letters="Vasque">Vasque</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a class="sanitaire_item" href="#"><span data-letters="Bloc">Bloc</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a class="sanitaire_item" href="#"><span data-letters="Bidet">Bidet</span></a></li>');
	}
	else if(categorie_name === 'Baignoires &amp; Receveurs'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"2"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Baignoires">Baignoires</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Receveurs">Receveurs</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Miroirs'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"3"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Standard">Standard</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Avec Lampe">Avec Lampe</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Avec LED">Avec LED</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Ovale">Ovale</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Carré">Carré</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Meubles S.D.B.'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"4"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="DINAR">DINAR</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="LUNA">LUNA</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="MARMARA">MARMARA</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="MARS">MARS</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="MILAS">MILAS</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="SAMBA">SAMBA</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="SOMA">SOMA</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="VALS">VALS</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Eviers en Inox'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"5"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Simple">Simple</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Double">Double</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Circulaire">Circulaire</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Robinetterie'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"6"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Mitigeur">Mitigeur</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Robinet">Robinet</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Poussoir">Poussoir</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Siphon">Siphon</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Colonne">Colonne</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Pomme">Pomme</span></a></li>');
		$('.list_subcategories').hide();
	}
	else if(categorie_name === 'Accessoires S.D.B.'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"7"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(28,"p"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(29,"n"));
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(30,"g"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Titanic">Titanic</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Flora">Flora</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="DE LUXE">DE LUXE</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="ELEGANCE">ELEGANCE</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="KUMRU">KUMRU</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="TEGRA">TEGRA</span></a></li>');
		$('.overlay_nav ul').append('<li class="link link--kumya"><a href="#"><span data-letters="Autre">Autre</span></a></li>');
		$('.list_subcategories').hide();
	}
	$('.overlay_nav').show();
  }, function() {
	$('.overlay_nav').hide();
	$('.list_subcategories').hide();
  }
);

$('.list_subcategories').hide();

$(document).on("mouseenter", ".sanitaire_item", function() {
    var sub_categorie_name = $(this).html();
	if(sub_categorie_name == "Vasque"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Metal-Line</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">A Encastrer</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Sous-Plan</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Semi-Encastrées</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">A Poser</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">A Poser sur Meuble</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Lave-Mains</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Muraux</span></a></li>');
	}
	else if(sub_categorie_name == "Bloc"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Arq</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Noble</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Eos</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Universal</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Klea</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Emma Square</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Emma</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Mid</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Smart</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Jazz</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Street Square</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Street</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Elia</span></a></li>');
	}
	else if(sub_categorie_name == "Bidet"){
		$('.list_subcategories').empty();
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Arq</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Noble</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Eos</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Universal</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Klea</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Emma Square</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Emma</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Mid</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Smart</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Jazz</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Street Square</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Street</span></a></li>');
		$('.list_subcategories').append('<li class="link link--kumya"><a href="#"><span data-letters="Kumya">Elia</span></a></li>');
	}
	$('.list_subcategories').show();
});

/*$(document).on("mouseenter", ".overlay_nav li", function() {
    $(this).css('background-color', 'red');
});
$(document).on("mouseenter", ".overlay_nav li", function() {
    $(this).css('background-color', 'red');
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