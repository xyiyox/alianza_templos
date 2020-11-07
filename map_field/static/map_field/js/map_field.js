
/*

This script expects:

<input type="text" name="address" id="id_address" />
<input type="text" class="geolocation_field" />

*/

function leafletMap() {

    var map;
    var marker = L.marker();

 
    var self = {
        initialize: function() {
            var lat = 4.520855;
            var lng = -74.098308;
            var zoom = 6;

            existinglocation = self.getExistingLocation();
            if (existinglocation) {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 16;
            }

            // existingZoom = self.getExistingZoom();
            // if (existingZoom) zoom = existingZoom;

            var latlng = L.latLng(lat, lng);

            /* var mqUrl      = 'http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.jpg',
                osmAttrib  = 'Map data &copy; <a target="_blank" href="http://openstreetmap.org">OpenStreetMap</a> contributors',
                mqAttrib   = 'Tiles Courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png">';

            var capaBase = L.tileLayer(mqUrl, {
                attribution: osmAttrib+' | '+mqAttrib,
                subdomains: ['otile1','otile2','otile3','otile4']
            }); */

            var mapUrl = "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"; 
            var osmAttribution = '©<a href="http://openstreetmap.org" target="_blank">OpenStreetMap</a> contributors'; 
            var capaBase = L.tileLayer(mapUrl, {maxZoom: 19, attribution: osmAttribution}); 
        
            if (map != undefined) { map.remove(); }  //para quitar erro de mapa previamente inicializado

            map = L.map('map_canvas', {
                center: latlng,
                zoom: zoom
            });
            map.addLayer(capaBase);
            

            if (existinglocation) {          
                self.setMarker(latlng);
            };

            map.on('click', self.onClick);
        },



        getExistingLocation: function() {
            var geolocation = $(".geolocation_field").val();
            if (geolocation) {
                return geolocation.split(',');
            }
        },

        // getExistingZoom: function() {
        //     var zoom = $("#id_zoom").val();
        //     if (zoom) return parseInt(zoom);
        // },

        onClick: function(e) {
            self.setMarker(e.latlng)
        },

 
        setMarker: function(latlng) {
            if (map.hasLayer( marker)) {
                marker.setLatLng(latlng);
            } else {
                self.addMarker(latlng);
            }
            map.setView(latlng);
            self.updateGeolocation(latlng);
        },

        addMarker: function(latlng) {
            marker.setLatLng(latlng);
            marker.addTo(map);
        },


        updateGeolocation: function(latlng) {
            var point = latlng.lat + "," + latlng.lng;
            $('.geolocation_field').val(point);
        },

        updateZoom: function(latlng) {
            $("#id_zoom").val(map.getZoom());
        },

    }

    return self;
}

$(document).ready(function() {
    var leafletmap = leafletMap();
    leafletmap.initialize();
});