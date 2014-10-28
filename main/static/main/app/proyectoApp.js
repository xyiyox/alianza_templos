'use strict';

angular
	.module('alianzaTemplosApp', [
		'ngAnimate',
		'ui.bootstrap',
		'leaflet-directive'
	])
	
	.controller('ProyectoCtrl',['$scope', '$window', function ($scope, $window) {

		$scope.lat = $window.latitud;
		$scope.lng = $window.longitud;

		$scope.proyectCenter= {
            lat: $scope.lat,
            lng: $scope.lng,
            zoom: 16
        };
        $scope.markers= {
            proyectMarker: {
                lat: $scope.lat,
                lng: $scope.lng,
                //message: "I want to travel here!",
                focus: true,
                draggable: false
            }
        };
        $scope.defaults={
            scrollWheelZoom: false
        };
        	
       

		$scope.verSubmit = false;

		$scope.procesarFoco = function(event) {

	  		if (event.type == 'focus') {
	  			event.target.rows = 2;
	  			$scope.verSubmit = true;
	  		}
	  		
	  		if (event.type == 'blur') {
	  			
				if (/^\s+$/.test(event.target.value) || event.target.value == '') {
					event.target.rows = 1;
					$scope.verSubmit = false;
				}	  			
	  		}
	    };
		
	}]);


