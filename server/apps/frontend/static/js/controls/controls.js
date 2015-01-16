angular.module('lk.controls', [])


.factory('stateManager', ['$state', function($state){
  return {
    firstLoad: true,
    currentState: $state.get(),
    isPresenting: false
  };
}])


.directive('controls', [function() {
  return {
    templateUrl: '/static/js/controls/controls.tpl.html',
    replace: true,
    restrict: 'E',
    link: function($scope, elem, attrs) {
      
      $scope.next = function() {
        $scope.$emit('nextEvent', 'next section please!');
      };

      $scope.prev = function() {
        $scope.$emit('prevEvent', 'prev section please!');
      };

    }
  };
}]);