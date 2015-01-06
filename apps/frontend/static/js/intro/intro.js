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


.directive('introPres', [
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
    templateUrl: '/static/js/intro/intro.pres.tpl.html',
    replace: true,
    link: function($scope, elem, atts) {
      $scope.introTrack = new Audio('/static/assets/audio/Intro.m4a');
      $scope.stateManager = stateManager;

      var openEnrollmentEventObject = {
        title: 'Open Enrollment',
        allDay: true,
        start: $scope.member.organization.open_enroll_start,
        end: $scope.member.organization.open_enroll_end,
        url: $scope.member.organization.enroll_url
      };

      $scope.start = function() {
        $scope.stateManager.isPresenting = true;
        $scope.introTrack.play();

        // Show the controls and welcome text
        $timeout(function() {
          var $intro = $('.intro');
          $intro.show();
          $intro.textillate( {
            in: {
              effect: 'fadeInDown'
            }
          });
          $scope.stateManager.isPresenting = true;
          $('.controls').fadeIn(1000);
        }, 2000);

        // Show the calendar
        $timeout(function() {
          $('#calendar').fadeIn(1000);
          $('#calendar').fullCalendar({
            defaultDate: $scope.member.organization.open_enroll_start,
            height: 450,
            header: {
              left: 'title',
              center: '',
              right: 'prev,next'
            },
            eventClick: function(event) {
              if (event.url) {
                $window.open(event.url);
                return false;
              }
            }
          });
          $('#calendar').fullCalendar('renderEvent', openEnrollmentEventObject, []);
          $('.intro').textillate( {
            out: {
              effect: 'hinge',
              delayScale: 1.5,
              delay: 50,
              sync: false,
              shuffle: false,
              reverse: false,
              callback: function () {}
            },
          });
          // Transition the welcome text to the calendar header
          $('.intro').textillate('out');
          $timeout(function() {
            $('.intro').hide();
            $('.intro').html('Open Enrollment Dates');
            $('.intro').fadeIn(1000);
          }, 3000);
        }, 4000);

      };

      // Go to the next section
      $scope.$on('nextEvent', function (event, data) {
        console.log(data);
        $scope.introTrack.pause();
        $scope.stateManager.firstLoad = false;
        $('.intro').fadeOut(500);
        $('#calendar').fadeOut(500);
        $timeout(function() {
          $state.go('medical', {member_id: 1});
        }, 500);
      });
    }
  };
}]);


