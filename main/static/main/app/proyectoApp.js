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



	    $scope.showForm = function(comentId, event) {

	    	// pregunto si existe el form
	    	var btn  = angular.element(event.currentTarget);

	    	if (!btn.next("#nested-comentario-form").length) {

		    	var nestedForm = angular.element('#comentario-form').clone();
		    	nestedForm.attr("id","nested-comentario-form");
		    	nestedForm.find('#id_comentario_padre').val(comentId);
		    	nestedForm.insertAfter(event.currentTarget);
		    	nestedForm.find('#submit-id-submit').addClass('show');//.css( "display", "block !important");

		    };

	    }
		
	}]);


