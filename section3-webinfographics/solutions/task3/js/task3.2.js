import { getDataForTask2 } from '../js/dataController.js';

const ctx = document.getElementById('placeholder2');

const hsl = (amount) => {
    let colors = [];
    for (let j = 0; j < amount; j++) {
        let hue = Math.floor(Math.random() * 360)
        colors.push(`hsl(${hue}, 80%, 70%)`);
    }
    return colors;
}

const dataset = await getDataForTask2();

const data = {
    labels: dataset.labels,
    datasets: [
        {
            data: dataset.values,
            backgroundColor: hsl(dataset.values.length),
        }
    ]
};
const config = {
    type: 'pie',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'right',
            },
            title: {
                display: true,
                align: 'center',
                text: 'Распределение экспонатов по стране происхождения'
            }
        },
    },
};

const pieChart = new Chart(ctx, config);
