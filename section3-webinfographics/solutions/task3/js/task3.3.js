import { getDataForTask3 } from '../js/dataController.js';

const ctx = document.getElementById('placeholder3');

const dataset = await getDataForTask3();
console.log(dataset)
const data = {
    labels: dataset.years,
    datasets: [
        {
            label: 'avgSumImpressionTotal',
            data: dataset.avgSumImpressionTotal,
            fill: true,
            borderColor: 'hsl(190, 70%, 60%)',
            backgroundColor: 'hsla(190, 70%, 80%, .2)',
            tension: 0.2
        },
        {
            label: "avgSumVisualFeedback",
            data: dataset.avgSumVisualFeedback,
            fill: true,
            borderColor: 'hsl(330, 70%, 60%)',
            backgroundColor: 'hsl(330, 70%, 80%, .2)',
            tension: 0.2
        },
    ]
};
const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        plugins: {

            legend: {
                position: 'top',
            },
            title: {
                display: true,
                align: 'center',
                text: 'Распределение зависимости общего впечатления и описания'
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'visualFeedback'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'impressionTotal'
                    }
                }
            }
        },
    },
};

const lineChart = new Chart(ctx, config);
