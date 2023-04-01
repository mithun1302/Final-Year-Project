// Age Group Chart
var ageData = {
    labels: ["65-75", "75-85", "85-95"],
    datasets: [{
      label: "Age Groups",
      backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
      data: [21.4, 32, 40]
    }]
  };
  
  var ageChart = new Chart(document.getElementById('ageChart'), {
    type: 'doughnut',
    data: ageData,
    options: {
      title: {
        display: true,
        text: 'Age Groups'
      }
    }
  });

  // Disease Attack Chart
  var diseaseData = {
    labels: ["Preclinical", "Mild cognitive impairment", "Mild dementia", "Moderate dementia","Severe dementia"],
    datasets: [{
      label: "Disease Attack",
      backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9","#000000"],
      data: [20, 50, 40, 30,5]
    }]
  };
  
  var diseaseChart = new Chart(document.getElementById('diseaseChart'), {
    type: 'bar',
    data: diseaseData,
    options: {
      title: {
        display: true,
        text: 'Disease Attack'
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            min:0,
            max:100
          }
        }]
      }
    }
  });
  