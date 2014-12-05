angular.module('lk.data', [])


.provider('Data', [function () {

  this.$get = ['$timeout', '$q', function ($timeout, $q) {
    return {
      getName: function() {
        var deferred = $q.defer();
        $timeout(function() {
          deferred.resolve("Kevin");
        }, 200);
        return deferred.promise;
      }
    };
  }];
  
}]);
