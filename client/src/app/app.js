angular.module( 'knowYourPlans', [
  'templates-app',
  'templates-common',
  'lk.intro',
  'lk.medical',
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
  $urlRouterProvider.otherwise( '/intro?member_id=1' );
}])


.run([function () {
}])


.controller('AppCtrl', [function () {
}]);
