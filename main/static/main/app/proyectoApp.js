'use strict';

angular
	.module('alianzaTemplosApp', [
		'ngAnimate',
		'ui.bootstrap',
		'leaflet-directive'
	])
	
	.controller('ProyectoCtrl',['$scope', '$window', '$location', '$anchorScroll', function ($scope, $window, $location, $anchorScroll) {

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

        /* -----------------------------------------*/  

        $scope.scrollTo = function(destino) {
        	$location.hash(destino);
      		$anchorScroll();
        };
        	
       
       /* -----------------------------------------*/    
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

	    $scope.alClickComentario = function(event) {
	    	var btn  = angular.element(event.currentTarget);
	    	btn.button('loading');  
	    };

	    /* -----------------------------------------*/  

	    $scope.showForm = function(comentId, event) {

	    	// pregunto si existe el form
	    	var btn  = angular.element(event.currentTarget);

	    	if (!btn.next("#nested-comentario-form").length) {

		    	var nestedForm = angular.element('#comentario-form').clone();
		    	nestedForm.attr("id","nested-comentario-form");
		    	nestedForm.find('#id_comentario_padre').val(comentId);
		    	nestedForm.insertAfter(event.currentTarget);
		    	var btn = nestedForm.find('.btn');
		    	btn.addClass('show'); 

		    	btn.one('click', function () {
			    	btn.button('loading'); 
			    });

		    };

	    }

	    /* ------------------  VISIBILIDAD DE ELEMENTOS DEL SIDEBAR  -----------------------*/ 
	    $scope.verAprobacion       = false;
	    $scope.verAquitectoEditForm     = false;
	    $scope.verIngenieroEditForm     = false;
	    $scope.verTesoreroEditForm     = false;
	    $scope.verFormAutorizacion = false;


	    $scope.openPanel = function(event) {    		 		
    		$scope.verAprobacion = event.type == 'mouseenter';
	    }

	    $scope.openOtherPanel = function(event) {    		 		
    		$scope.verAquitectoEditForm = event.type == 'mouseenter' && event.currentTarget.id == 'panel-arquitecto' ? true : false;
    		$scope.verIngenieroEditForm = event.type == 'mouseenter' && event.currentTarget.id == 'panel-ingeniero' ? true : false;
    		$scope.verTesoreroEditForm = event.type == 'mouseenter' && event.currentTarget.id == 'panel-tesorero' ? true : false;
	    }


	    /* ------------------  AUTORIZACIONES  -----------------------*/ 

	    $scope.alClickAprobacion = function() {
	    	angular.element('#submit-aprobacion-btn').button('loading');
	    	angular.element('#revisar-aprobacion-btn').attr('disabled', 'disabled');
	    }

	    $scope.alClickAprobarUsuarios = function() {
			angular.element('#msg-default').addClass('hidden');
			angular.element('#msg-usuarios').removeClass('hidden').addClass('show');
	    }
		
	}]);


