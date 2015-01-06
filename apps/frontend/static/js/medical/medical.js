angular.module( 'lk.medical', [
    'ui.router.state'
])


.config(['$stateProvider', function ($stateProvider) {
  $stateProvider.state( 'medical', {
    url: '/medical?member_id',
    views: {
      "main": {
        controller: 'MedicalCtrl',
        templateUrl: '/static/js/medical/medical.tpl.html'
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


.controller( 'MedicalCtrl', [
  '$scope', 
  'member',
function (
  $scope, 
  member
) {
  
  $scope.member = member.data;

}])


.directive('medicalPres', [
  '$timeout',
  '$state',
  '$window',
  'stateManager',
function(
  $timeout,
  $state,
  $window,
  stateManager
){
  return {
    scope: {
      member: '='
    }, 
    restrict: 'E', 
    templateUrl: '/static/js/medical/medical.pres.tpl.html',
    replace: true,
    link: function($scope, elem, atts) {
      $scope.introTrack = new Audio('/static/assets/audio/Intro.m4a');
      $scope.stateManager = stateManager;
      $scope.plans = $scope.member.medical_plans;

      $scope.start = function() {
        $scope.stateManager.isPresenting = true;
        $scope.introTrack.play();
        $timeout(function() {
          $scope.showTable = true;
          $('#medical-table').fadeIn(500);
        }, 2000);
      };

      if ($scope.stateManager.isPresenting) {
        $scope.start();
      }

      // Go to the next section
      $scope.$on('nextEvent', function (event, data) {
        console.log(data);
        $timeout(function() {

        });
      });
    }
  };
}]);


