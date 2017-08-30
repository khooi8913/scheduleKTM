(function(){
'use strict';

var app = angular.module('KTMSchedule', []);
app.controller('KTMScheduleController', KTMScheduleController);
app.service('KTMScheduleService', KTMScheduleService);

KTMScheduleController.$inject = ['KTMScheduleService'];
function KTMScheduleController(KTMScheduleService){
	var KTM = this;
	
	KTM.origin = "";
	KTM.destination = "";
	KTM.date = "";

	KTM.list = KTMScheduleService.getList();

	KTM.search = function(origin,destination,date){
		$("#error").addClass('hide');
		$("#loader").removeClass('hide');
		KTMScheduleService.callAPI(origin,destination,date);
	}

	KTM.predicate = "-Availability";

	KTM.sort = function(predicate){
		if(KTM.predicate==predicate)
			KTM.predicate = "-" + KTM.predicate;
		else
			KTM.predicate = predicate;
	}

}

KTMScheduleService.$inject = ['$http'];
function KTMScheduleService($http){
	var service = this;

	var list = [];

	service.getList = function(){
		return list;
	}

	service.callAPI = function(origin1,destination1,date1){
		list.length = 0;
		$http({
			url: "https://traineer-178315.appspot.com",
			method: "GET",
			params: {origin: origin1, destination: destination1, date: date1}
		}).then(function (response){
			for(var item of response.data){
				list.push(item);
			}
			if(list.length==0){$("#error").removeClass('hide');}
			$("#loader").addClass('hide');
		}).catch(function(){
			$("#loader").addClass('hide');
			$("#error").removeClass('hide');
		});
	}
}

})();
