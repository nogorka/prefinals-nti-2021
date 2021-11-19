import { getDataForTask1 } from '../js/dataController.js';

const ctx = document.getElementById('placeholder1');

const data = {
    datasets: [
        {
            label: 'Экспонаты',
            data: await getDataForTask1(),
            borderColor: 'hsla(340, 80%, 50%, 1)',
            backgroundColor: 'hsla(340, 80%, 60%, .5)',
        }
    ]
};
const config = {
    type: 'scatter',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
            },
            title: {
                display: true,
                align: 'center',
                text: 'Распределение экспонатов по среднему общему впечатлению и средней визуальной оценке'
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'average visualFeedback'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'average impressionTotal'
                }
            }
        }
    },
};

const scatterChart = new Chart(ctx, config);