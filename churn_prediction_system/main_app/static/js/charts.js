// google.charts.load("current", {packages:["corechart"]});
// google.charts.setOnLoadCallback(drawChart);
// var month_to_month = 0;
// function drawChart() {
//     //Arrays
//   var contract_data = google.visualization.arrayToDataTable([
//     ['Response', 'Number of Response'],
//     ['Month to Month',     11],
//     ['One Year',      2],
//     ['Two Year',      2],
//   ]);
//   var device_protection_data = google.visualization.arrayToDataTable([
//     ['Response', 'Number of Response'],
//     ['Yes',     10],
//     ['No',      10],
//   ]);

//   //Options
//   var contract_options = {
//     title: 'Contract',
//     pieHole: 0.4,
//   };
//   var device_protecttio_options = {
//     title: 'Device Protection',
//     pieHole: 0.4,
//   };

//   //visual representation
//   var contract = new google.visualization.PieChart(document.getElementById('contract'));
//   contract.draw(contract_data, contract_options);

//   var device_protection = new google.visualization.PieChart(document.getElementById('device_protection'));
//   device_protection.draw(device_protection_data, device_protecttio_options);
// }

// function contract_data(variable){
//     if(variable == "month_to_month")
//         month_to_month += 1
//     else if(variable == "one_year")
// }