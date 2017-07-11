'use strict';

angular
	.module('informePublicoApp', [
		'ngAnimate',
		'ui.bootstrap'
	])
	
	.controller('InformePublicoCtrl',['$scope', '$window', '$anchorScroll', function ($scope, $window,  $anchorScroll) {

        $scope.enviandoForm = false;
        $scope.plantacionDefault1 = '';
        $scope.plantacionDefault2 = '';
        $scope.plantacionDefault3 = '';
        $scope.plantacionDefault4 = '';
        $scope.plantacionDefault5 = '';

        $scope.alClickEnviar = function(e) {
            $scope.enviandoForm = true;
        };

        $scope.alClickNinguno = function(e) {
            if (e.target.id == 'ninguno-btn-1') 
                $scope.plantacionDefault1 = 'NINGUNO';
            
            if (e.target.id == 'ninguno-btn-2') 
                $scope.plantacionDefault2 = 'NINGUNO';
            
            if (e.target.id == 'ninguno-btn-3') 
                $scope.plantacionDefault3 = 'NINGUNO';
            
            if (e.target.id == 'ninguno-btn-4') 
                $scope.plantacionDefault4 = 'NINGUNO';

            if (e.target.id == 'ninguno-btn-5') 
                $scope.plantacionDefault5 = 'NINGUNO';
            
        }
	     

		
	}]);


