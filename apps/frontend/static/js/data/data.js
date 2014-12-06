angular.module('lk.data', [])


.provider('Data', [function () {

  this.$get = ['$http', function ($http) {
    return {
      getName: function(id) {
        return $http.get('/rest/members/'+id);
      }
    };
  }];
  
}]);
