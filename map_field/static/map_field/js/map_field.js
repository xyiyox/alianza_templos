
/*
Integration for Google Maps in the django admin.

How it works:

You have an address field on the page.
Enter an address and an on change event will update the map
with the address. A marker will be placed at the address.
If the user needs to move the marker, they can and the geolocation
field will be updated.

Only one marker will remain present on the map at a time.

This script expects:

<input type="text" name="address" id="id_address" />
<input type="text" name="geolocation" id="id_geolocation" />

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

*/

function leafletMap() {

    var map;
    var marker = L.marker();

 
    var self = {
        initialize: function() {
            var lat = 4.520855;
            var lng = -74.098308;
            var zoom = 6;

            // set up initial map to be world view. also, add change
            // event so changing address will update the map
            existinglocation = self.getExistingLocation();
            if (existinglocation) {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 16;
            }

            existingZoom = self.getExistingZoom();
            if (existingZoom) zoom = existingZoom;

            var latlng = L.latLng(lat, lng);

            

            //google.maps.event.addListener(map, 'zoom_changed', self.updateZoom);

            var mqUrl      = 'http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.jpg',
                osmAttrib  = 'Map data &copy; <a target="_blank" href="http://openstreetmap.org">OpenStreetMap</a> contributors',
                mqAttrib   = 'Tiles Courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png">';

            var capaBase = L.tileLayer(mqUrl, {
                attribution: osmAttrib+' | '+mqAttrib,
                subdomains: ['otile1','otile2','otile3','otile4']
            });

            map = L.map('map_canvas', {
                center: latlng,
                zoom: zoom
            });
            map.addLayer(capaBase);


            if (existinglocation) {          
                self.setMarker(latlng);
            };

            map.on('click', function(e) {
                
                marker.setLatLng(e.latlng);
                if (! map.hasLayer( marker)) {
                   marker.addTo(map); 
                };

                var point = e.latlng.lat + "," + e.latlng.lng;
                $('.geolocation_field').val(point);
            });


        },

        getExistingLocation: function() {
            var geolocation = $(".geolocation_field").val();
            if (geolocation) {
                return geolocation.split(',');
            }
        },

        getExistingZoom: function() {
            var zoom = $("#id_zoom").val();
            if (zoom) return parseInt(zoom);
        },

 

        setMarker: function(latlng) {
            if (map.hasLayer( marker)) {
                marker.setLatLng(latlng);
            } else {
                self.addMarker(latlng);
            }
            map.setView(latlng);
        },

        addMarker: function(latlng) {
            marker.setLatLng(latlng);
            marker.addTo(map);
        },


        updateMarker: function(latlng) {
            marker.setPosition(latlng);
        },

        updateGeolocation: function(latlng) {
            $("#id_geolocation").val(latlng.lat() + "," + latlng.lng());
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