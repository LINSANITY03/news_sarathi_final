
var x1Values = ["Yogi. I love it 1.", "Yogi. I love it 2.", "Yogi. I love it 3.", "Yogi. I love it4."];
var y1Values = [50, 30, 15, 5];
var barColors = [
    "#b91d47",
    "#00aba9",
    "#2b5797",
    "#e8c3b9",

];

new Chart("myChart1", {
    type: "doughnut",
    data: {
        labels: x1Values,
        datasets: [{
            backgroundColor: barColors,
            data: y1Values
        }]
    },
    options: {
        title: {
            display: true,
            text: "World Wide Wine Production 2018"
        }
    }
});

var x2Values = ["Yogi. I love it 1.", "Yogi. I love it 2.", "Yogi. I love it 3.", "Yogi. I love it4."];
var y2Values = [5, 15, 50, 30];
var barColors = [
    "#b91d47",
    "#00aba9",
    "#2b5797",
    "#e8c3b9",

];

new Chart("myChart2", {
    type: "horizontalBar",
    data: {
      labels: x2Values,
      datasets: [{
        backgroundColor: barColors,
        data: y2Values
      }]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "What is your name? Why are you gay?"
      }
    }
  });


