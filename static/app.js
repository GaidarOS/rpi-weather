socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {
    socket.emit('client_connected', {
        data: 'New client!'
    });
});

socket.on('json', function (jsn) {
    console.log("And yet it runs!");
    console.log(jsn);
    dt=jsn;
});

var dt;
socket.on('alert', function (data) {
    // alert('Alert Message!! ' + data);
    console.log(data);
    dt = data;
});

function json_button() {
    socket.emit('json');
}

function alert_button() {
    setInterval(function () {
        socket.emit('alert_button', 'A very bad message!')
    }, 5000)
}

var dps = []
dps.shift()

// ###################################################################
// ###################################################################

window.onload = function () {

    socket.emit('json');

    setInterval(function () {
        socket.emit('alert_button', 'A very bad message!')
    }, 5000);

    var dps = []; // dataPoints
    var lbls = []; // labelsArray
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: lbls,
            datasets: [{
                label: 'Temp1',
                data: dps,
                backgroundColor: [
                    'rgba(255, 159, 64, 0)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        display: false //this will remove only the label
                    },
                    gridLines : {
                        display : false
                    }
                }],
                yAxes:[{
                    display:true,
                    ticks:{
                        padding: 5
                    }
                }]
            },
            legend: {
                display: false,
                position: 'bottom'
            },
            elements: {
                point: {
                    radius: 0
                }
            },
            title: {
                display: true,
                text: 'Raspberry Temp readings'
            }
        }
    });

    var xVal = 0;
    var yVal = 100;
    var updateInterval = 1000; // Time in ms to update the graph
    var dataLength = 200; // number of dataPoints visible at any point

    var updateChart = function (count) {

        count = count || 1;
        dtOld = 0;
        if (typeof dt !== "undefined") {
            if (dt != dtOld) {
                for (var j = 0; j < count; j++) {
                    dps.push(dt);
                    lbls.push(xVal)
                    dtOld = dt;
                    xVal++;
                }

                if (dps.length > dataLength) {
                    dps.shift();
                    lbls.shift();
                }

                myChart.update();
            }
        }
    };

    updateChart(dataLength);
    setInterval(function () {
        updateChart()
    }, updateInterval);

}

// ###################################################################
// ###################################################################