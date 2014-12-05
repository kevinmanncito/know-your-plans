angular.module( 'knowYourPlans', [
  'lk.intro',
  'lk.controls',
  'lk.data',
  'ui.router.state',
  'ui.router'
])


.config([
  '$urlRouterProvider',
function (
  $urlRouterProvider
) {
  $urlRouterProvider.otherwise( '/intro' );
}])


.run([function () {
}])


.controller('AppCtrl', [function () {
}]);
