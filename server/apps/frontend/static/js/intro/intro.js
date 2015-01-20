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
  '$window',
  'member',
function (
  $scope, 
  $window,
  member
) {
  
  $scope.member = member.data;
  var start = moment($scope.member.organization.open_enroll_start),
      end = moment($scope.member.organization.open_enroll_end),
      eventList = [];
  for (var d = start; d <= end; d.add(1, 'days')) {
    eventList.push({
      title: 'Enroll!',
      allDay: true,
      start: d.calendar(),
      end: d.calendar(),
      url: $scope.member.organization.enroll_url
    });
  };

  $scope.events = eventList;

}])


.directive('introPres', [
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
      member: '=',
      events: '='
    }, 
    restrict: 'E', 
    templateUrl: '/static/js/intro/intro.pres.tpl.html',
    replace: true,
    link: function($scope, elem, atts) {
      $scope.introTrack = new Audio('/static/assets/audio/open_enrollment_intro.mp3');
      $scope.stateManager = stateManager;

      var openEnrollmentEventObject = {
        title: '',
        allDay: true,
        start: $scope.member.organization.open_enroll_start,
        end: $scope.member.organization.open_enroll_start,
        url: $scope.member.organization.enroll_url
      };

      $scope.start = function() {
        $scope.stateManager.isPresenting = true;
        $scope.introTrack.play();

        // Animate the logo into the center
        $timeout(function() {
          var $logo = $('.logo');
          $logo.show();
          $logo.animate({
            left: '50%'
          }, 800);
          $logo.effect('bounce', {}, 1000);
        }, 50);

        // Get rid of logo
        $timeout(function() {
          $('.logo').fadeOut(200);
        }, 2000);

        // Show name
        $timeout(function() {
          var $intro = $('.intro');
          $intro.show();
          $intro.textillate( {
            in: {
              effect: 'fadeInDown'
            }
          }, 600);
        }, 2500);

        // Move stuff over to the left
        $timeout(function() {
          $('.logo').fadeOut(200);
          $('.intro-wrapper').animate({
            left: '150px'
          }, 600);
        }, 3500);

        // Show the controls and welcome text
        $timeout(function() {
    
          $scope.stateManager.isPresenting = true;
          $('.controls').fadeIn(1000);
        }, 4000);

        // Show the calendar
        $timeout(function() {
          $('#calendar').fadeIn(1000);
          $('#calendar').fullCalendar({
            defaultDate: $scope.member.organization.open_enroll_start,
            height: 400,
            header: {
              left: 'title',
              center: '',
              right: ''
            },
            eventClick: function(event) {
              if (event.url) {
                $window.open(event.url);
                return false;
              }
            }
          });
          // cycle through events and show them one at a time
          var dateInterval = 200;
          angular.forEach($scope.events, function(e, index) {
            $timeout(function() {
              $('#calendar').fullCalendar('renderEvent', e, []);
            }, dateInterval);
            dateInterval += 500;
          });
          $timeout(function() {
            console.log('showing sub');
            $('.sub').fadeIn(1000);
            $('.start').fadeIn(1000);
            $end = $('.end');
            $end.fadeIn(100);
            $end.textillate( {
              in: {
                effect: 'pulse'
              }
            }, 3000);
          }, 3000);
        }, 6000);

      };
      // If we are already presenting lets get this show on the road
      if ($scope.stateManager.isPresenting) {
        $scope.start();
      }

      // Go to the next section
      $scope.$on('nextEvent', function (event, data) {
        console.log(data);
        $scope.introTrack.pause();
        $scope.stateManager.firstLoad = false;
        $('.intro').fadeOut(500);
        $('#calendar').fadeOut(500);
        $timeout(function() {
          $state.go('medical', {member_id: $stateParams.member_id});
        }, 500);
      });
    }
  };
}]);


