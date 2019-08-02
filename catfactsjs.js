var cat;
var fact;
var view;

function init(){
  fact = ol.proj.fromLonLat;

  view = new ol.View({
    center: ourLoc,
    zoom: 6
  });
  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}



function makeCatRequest(){

  var breed = document.getElementById("cat-name");

  if(breed ===""){
    alert("You didn't enter a cat breed!");
  }

  var query = "https://catfact.ninja/breeds?limit=100";
  //query = query.replace(/ /g, "%20");

  breedRequest = new XMLHttpRequest();
  breedRequest.open('GET', query, true);
  breedRequest.onload = processCatRequest();
  breedRequest.send();
}

function processCatRequest(){

  var breed = document.getElementById("cat-name");
  alert(breedRequest.readyState);

  if(breed ===""){
    alert("You didn't enter a cat breed!");
  }
  if(breedRequest.readyState != 4){
    return;
  }
  if(breedRequest.status != 200 || breedRequest.responseText === ""){
    alert("We couldn't find your cat breed!");
    return;
  }
    alert("hi");
  var catInfo = JSON.parse(breedRequest.responseText);
  for (i = 0; i < catInfo.length; i++) {
    currCat = catInfo[i].breed;
    if (currCat === breed){
      alert("Found your cat!");
      alert(currCat);
    }
  }
  //var lon = countryInfo[0].latlng[1];
//  var location = ol.proj.fromLonLat([lon, lat]);

  //view.animate({
  //  center: location,
  //  duration: 2000
//  });
}

window.onload = init;
