angular.module('lk.controls', [])

.directive('controls', [function() {
  return {
    templateUrl: 'controls/controls.tpl.html',
    replace: true,
    restrict: 'E',
    link: function($scope, elem, attrs) {
      
    }
  };
}])

.directive('playButton', [function() {
  return {
    templateUrl: 'controls/playButton.tpl.html',
    replace: true,
    restrict: 'E',
    link: function($scope, elem, attrs) {
      
    }
  };
}]);