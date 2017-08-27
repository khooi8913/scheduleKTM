  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 3, // Creates a dropdown of 15 years to control year
    format: 'dd-mmm-yyyy',
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
  });

$(document).ready(function() {
	$(".button-collapse").sideNav();
	$('select').material_select();
});


