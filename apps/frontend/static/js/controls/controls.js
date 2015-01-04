angular.module('lk.controls', [])

.directive('controls', [function() {
  return {
    templateUrl: '/static/js/controls/controls.tpl.html',
    replace: true,
    restrict: 'E',
    link: function($scope, elem, attrs) {
      
    }
  };
}]);