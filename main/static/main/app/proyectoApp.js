'use strict';

angular
	.module('alianzaTemplosApp', [
		'ngAnimate'
	])
	
	.controller('ProyectoCtrl', function ($scope) {

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
		
	});


