function goToConfirm(){
	if (window.confirm("Are you sure?")){
		window.location = 'generated_pur.html';
	}

	else{
		return false;
	}
}


$(document).ready(function() {
    $('input#input_text, textarea#textarea1').characterCounter();
  });

    $(document).ready(function() {
        $('input#input_text, textarea#textarea1').characterCounter();

      });
  <!-- google map script -->
  $(document).ready(function() {
      $('input#input_text, textarea#textarea1').characterCounter();

    });
<!-- google map script -->
function initMap() {
  var uluru = {lat: 26.9307921, lng: 75.7147893};
 var map = new google.maps.Map(document.getElementById('map'), {
   zoom: 12,
   center: uluru,

 });

 var contentString = '<h7 style="color: black"><b>Rajasthan Central Hospital</b><br>Nana Nager, 45/6 Lajpat Road <br> Jaipur <br> <i>Under Dr.R.Verma</i> </h7>';
 var infowindow = new google.maps.InfoWindow({
   content: contentString
 });

 var marker = new google.maps.Marker({
   position: uluru,
   map: map,
   title: 'Uluru (Ayers Rock)',
   icon:  'img/icon.png'
 });
 marker.addListener('click', function() {
   infowindow.open(map, marker);
 });      }
