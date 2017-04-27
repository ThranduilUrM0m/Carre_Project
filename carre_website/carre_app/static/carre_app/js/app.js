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
	if(categorie_name === 'Sanitaire'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"1"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Vasque</li>');
		$('.overlay_nav ul').append('<li>Lavabo</li>');
		$('.overlay_nav ul').append('<li>Bloc</li>');
		$('.overlay_nav ul').append('<li>Bidet</li>');
	}
	else if(categorie_name === 'Baignoires &amp; Receveurs'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"2"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Baignoires</li>');
		$('.overlay_nav ul').append('<li>Receveurs</li>');
	}
	else if(categorie_name === 'Miroirs'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"3"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Standard</li>');
		$('.overlay_nav ul').append('<li>Avec Lampe</li>');
		$('.overlay_nav ul').append('<li>Avec LED</li>');
		$('.overlay_nav ul').append('<li>Ovale</li>');
		$('.overlay_nav ul').append('<li>Carré</li>');
	}
	else if(categorie_name === 'Meubles S.D.B.'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"4"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>DINAR</li>');
		$('.overlay_nav ul').append('<li>LUNA</li>');
		$('.overlay_nav ul').append('<li>MARMARA</li>');
		$('.overlay_nav ul').append('<li>MARS</li>');
		$('.overlay_nav ul').append('<li>MILAS</li>');
		$('.overlay_nav ul').append('<li>SAMBA</li>');
		$('.overlay_nav ul').append('<li>SOMA</li>');
		$('.overlay_nav ul').append('<li>VALS</li>');
	}
	else if(categorie_name === 'Eviers en Inox'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"5"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Simple</li>');
		$('.overlay_nav ul').append('<li>Double</li>');
		$('.overlay_nav ul').append('<li>Circulaire</li>');
	}
	else if(categorie_name === 'Robinetterie'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"6"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Mitigeur</li>');
		$('.overlay_nav ul').append('<li>Robinet</li>');
		$('.overlay_nav ul').append('<li>Poussoir</li>');
		$('.overlay_nav ul').append('<li>Siphon</li>');
		$('.overlay_nav ul').append('<li>Colonne</li>');
		$('.overlay_nav ul').append('<li>Pomme</li>');
	}
	else if(categorie_name === 'Accessoires S.D.B.'){
		$('.overlay_nav img').attr('src', $('.overlay_nav img').attr('src').replaceAt(26,"7"));
		$('.overlay_nav ul').empty();
		$('.overlay_nav ul').append('<li><h2>Collection</h2></li>');
		$('.overlay_nav ul').append('<li>Titanic</li>');
		$('.overlay_nav ul').append('<li>Flora</li>');
		$('.overlay_nav ul').append('<li>DE LUXE</li>');
		$('.overlay_nav ul').append('<li>ELEGANCE</li>');
		$('.overlay_nav ul').append('<li>KUMRU</li>');
		$('.overlay_nav ul').append('<li>TEGRA</li>');
		$('.overlay_nav ul').append('<li>Autre</li>');
	}
	$('.overlay_nav').show();
  }, function() {
	$('.overlay_nav').hide();
  }
);

$('.overlay_nav').hover(
  function() {
	$(this).show();
  }, function() {
	$(this).hide();
  }
);