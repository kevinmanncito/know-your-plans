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
  'member',
function (
  $scope, 
  member
) {
  
  $scope.member = member.data;

}])


.directive('introPres', ['$timeout', function($timeout){
  return {
    scope: {
      member: '='
    }, 
    restrict: 'E', 
    templateUrl: '/static/js/intro/intro.pres.tpl.html',
    replace: true,
    link: function($scope, elem, atts) {
      $scope.introTrack = new Audio('/static/assets/audio/Intro.m4a');
      $scope.start = function() {

        $('.play').hide();
        $scope.introTrack.play();

        $timeout(function() {
          var $intro = $('.intro');
          $intro.show();
          $intro.textillate( {
            in: {
              effect: 'fadeInDown'
            }
          });
        }, 2000);

        $timeout(function() {
          $('.controls').fadeIn(1000);
        }, 2000);

      };
    }
  };
}]);


