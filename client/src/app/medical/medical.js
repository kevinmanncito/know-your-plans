angular.module( 'lk.medical', [
    'ui.router.state'
])


.config(['$stateProvider', function ($stateProvider) {
  $stateProvider.state( 'medical', {
    url: '/medical?member_id',
    views: {
      "main": {
        controller: 'MedicalCtrl',
        templateUrl: 'medical/medical.tpl.html'
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
  '$sce',
  'member',
function (
  $scope, 
  $sce,
  member
) {

  // Replace the copay pipes with line breaks
  for (var i in member.data.medical_plans) {
      member.data.medical_plans[i].copays = $sce.trustAsHtml(member.data.medical_plans[i].copays.replace(/\|/g, '<br>'));
  }
  
  $scope.member = member.data;

}])


.directive('medicalPres', [
  '$timeout',
  '$state',
  '$window',
  '$stateParams',
  'stateManager',
function(
  $timeout,
  $state,
  $window,
  $stateParams,
  stateManager
){
  return {
    scope: {
      member: '='
    }, 
    restrict: 'E', 
    templateUrl: 'medical/medical.pres.tpl.html',
    replace: true,
    link: function($scope, elem, atts) {
      $scope.track = new Audio('/static/assets/audio/open_enrollment_intro.mp3');
      $scope.stateManager = stateManager;
      $scope.plans = $scope.member.medical_plans;

      $scope.firstPlan = $scope.plans.shift();

      $scope.start = function() {
        $scope.stateManager.isPresenting = true;
        $scope.track.play();

        // Display header
        $timeout(function() {
          var $intro = $('.med-title');
          $intro.show();
          $intro.textillate( {
            in: {
              effect: 'bounceIn'
            }
          });
        }, 500);

        // Display table
        $timeout(function() {
          $scope.showTable = true;
          $('#medical-table').fadeIn(500);
        }, 2000);
      };

      // If we are already presenting lets get this show on the road
      if ($scope.stateManager.isPresenting) {
        $scope.start();
      }

      // Go to the next section
      $scope.$on('nextEvent', function (event, data) {
        $timeout(function() {

        });
      });

      // Go to the previous section
      $scope.$on('prevEvent', function (event, data) {
        $('#medical-table').fadeOut(500);
        $('.med-title').fadeOut(500);
        $scope.track.pause();
        $timeout(function() {
          $state.go('intro', {member_id: $stateParams.member_id});
        }, 500);
      });
    }
  };
}]);


