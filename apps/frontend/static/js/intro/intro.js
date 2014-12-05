angular.module( 'lk.intro', [
    'ui.router.state'
])


.config(['$stateProvider', function ($stateProvider) {
  $stateProvider.state( 'intro', {
    url: '/intro?name',
    views: {
      "main": {
        controller: 'IntroCtrl',
        templateUrl: '/static/js/intro/intro.tpl.html'
      }
    }
    // resolve: {
    //   'name': ['Data', function(Data) {
    //     return Data.getName();
    //   }]
    // }
  });
}])


.controller( 'IntroCtrl', [
  '$scope', 
  '$stateParams',
  '$timeout', 
function (
  $scope, 
  $stateParams,
  $timeout
) {
  $scope.name = $stateParams.name;
  $scope.introTrack = new Audio('/static/assets/audio/Intro.m4a');

  $scope.start = function() {
    $('.play').hide();
    $scope.introTrack.play();
    $timeout(function() {
      $('.intro').fadeIn(1000);
    }, 2000);
  };

  
}]);