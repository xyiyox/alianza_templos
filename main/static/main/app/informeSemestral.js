'use strict';

angular
	.module('informePublicoApp', [
		'ngAnimate',
		'ui.bootstrap'
	])
	
	.controller('InformePublicoCtrl',['$scope', '$window', '$anchorScroll', function ($scope, $window,  $anchorScroll) {

        $scope.enviandoForm = false;

        $scope.alClickEnviar = function(e) {
            $scope.enviandoForm = true;
            console.log('hola soy informe semestral');
            console.log(e);
        };
	     

		
	}]);


