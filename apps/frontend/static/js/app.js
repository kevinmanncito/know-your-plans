angular.module( 'knowYourPlans', [
  'lk.intro',
  'lk.landing',
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
  $urlRouterProvider.otherwise( '/landing' );
}])


.run([function () {
}])


.controller('AppCtrl', [function () {
}]);
