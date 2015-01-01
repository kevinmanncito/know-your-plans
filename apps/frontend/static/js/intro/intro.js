angular.module( 'lk.intro', [
    'ui.router.state'
])


.config(['$stateProvider', function ($stateProvider) {
  $stateProvider.state( 'intro', {
    url: '/intro?member_id',
    views: {
      "main": {
        controller: 'IntroCtrl',
        templateUrl: '/static/js/intro/intro.tpl.html'
      }
    },
    resolve: {
      'member': ['Data', '$stateParams', function (Data, $stateParams) {
        if (angular.isDefined($stateParams.member_id)) {
          return Data.getName($stateParams.member_id);
        } else {
          $stateParams.member_id = 1;
          return Data.getName($stateParams.member_id);
        }
      }]
    }
  });
}])


.controller( 'IntroCtrl', [
  '$scope', 
  '$stateParams',
  '$timeout', 
  'member',
function (
  $scope, 
  $stateParams,
  $timeout,
  member
) {
  $scope.introTrack = new Audio('/static/assets/audio/Intro.m4a');

  $scope.member = member.data;

  $scope.start = function() {
    $('.play').hide();
    $scope.introTrack.play();
    $timeout(function() {
      $('.intro').fadeIn(1000);
    }, 2000);
  };

}]);