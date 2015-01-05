angular.module('lk.controls', [])


// .factory('currentAudio', [function(){
//   return function name(){
    
//   };
// }])


.directive('controls', [function() {
  return {
    templateUrl: '/static/js/controls/controls.tpl.html',
    replace: true,
    restrict: 'E',
    link: function($scope, elem, attrs) {
      
      $scope.next = function() {
        $scope.$emit('nextEvent', 'next section please!');
      }

    }
  };
}]);