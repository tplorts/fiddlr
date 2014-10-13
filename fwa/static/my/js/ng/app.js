(function(){
    'use strict';

    var fiddlrApp = angular.module('fiddlrApp', [
        'ngRoute',
        'fiddlrApp.controllers'
    ]);

    fiddlrApp.config(
        ['$interpolateProvider', function($interpolateProvider) {
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
        }]
    );

}());
