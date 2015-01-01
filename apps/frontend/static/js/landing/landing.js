angular.module( 'lk.landing', [
    'ui.router.state'
])


.config(['$stateProvider', function ($stateProvider) {
  $stateProvider.state( 'landing', {
    url: '/landing',
    views: {
      "main": {
        controller: 'LandingCtrl',
        templateUrl: '/static/js/landing/landing.tpl.html'
      }
    }
  });
}])


.controller( 'LandingCtrl', [
  '$scope',
function (
  $scope 
) {

}]);