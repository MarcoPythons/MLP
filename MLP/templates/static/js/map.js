let map;              
function initMap() {
  var coord = { lat: 38.8976513 , lng: -77.0365294  };
    var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: coord
  });
  var marker = new google.maps.Marker({
    position: coord, 
    map: map
  })
}

//var coord = { lat: 38.8976513 , lng: -77.0365294  }; casa blanca

//var coord = { lat: -33.4428779 , lng: -70.6538932  }; la moneda

//var coord = { lat: 48.8583721 , lng: 2.2943675  }; torre ifel

//var coord = { lat: 37.241904 , lng: -115.817594  }; area 51


