let map;              
function initMap() {
    var coord = { lat: -33.4428779, lng: -70.6538932 };
    var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: coord
  });
  var marker = new google.maps.Marker({
    position: coord, 
    map: map
  })
}