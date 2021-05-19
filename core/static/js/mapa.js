function onEachFeature(feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
}

var myIcon = L.icon({
    iconUrl: '../../static/img/wifi-user.png',
    iconSize: [20, 20],
    iconAnchor: [10, 10]
});

function myPoint(){
    if ("geolocation" in navigator) {
        /* geolocation is available */
        navigator.geolocation.getCurrentPosition(function(position){
            console.log(position);
            var posicaoUsuario = L.marker([position.coords.latitude, position.coords.longitude], {icon: myIcon})
                .bindPopup('<span>Estou aqui!</span>')
                .openPopup()
                .addTo(map);
        }, function(error){
            console.log(error)
        });
        
    } else {
        console.log("Não tem geolocation");
        // alert("Não foi possível identificar sua localização através do seu navegador");
    } 
}

var gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var areas  = L.geoJson([], {
    onEachFeature: onEachFeature,
});

var areasUrl = $("#areas_geojson").val();

$.getJSON(areasUrl, function(data){
    areas.addData(data);
})

var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

var grayscale   = L.tileLayer(mbUrl, {id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
streets  = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});


var map = L.map('map', {
center: [-25.436090, -54.595616],
zoom: 17,
layers: [satellite, areas]
});


var baseLayers = {
    "Google Satélite": satellite,
    "Google Streets": gstreets,
    
};
// "Grayscale": grayscale,
// "Streets": streets

var overlays = {
    "Areas": areas
};

L.control.layers(baseLayers, overlays).addTo(map);
myPoint();