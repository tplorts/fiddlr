(function(){
    'use strict';

    var cmod = angular.module('fiddlrApp.controllers', []);

    function readScopeInitials(scope) {
        if (angular.isUndefined(ngScopeInitials))
            return;
        for (var k in ngScopeInitials) {
            if (ngScopeInitials.hasOwnProperty(k)) {
                scope[k] = ngScopeInitials[k];
            }
        }
    }        

    function PortalPicCtlr($scope) {
        readScopeInitials($scope);
        $scope.menu = {
            isHidden: true
        };
    }
    cmod.controller('PortalPicCtlr', ['$scope', PortalPicCtlr]);

}());