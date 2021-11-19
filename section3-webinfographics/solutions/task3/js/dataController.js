export async function getDataForTask1() {

    console.log("wait")

    let url = 'http://localhost:5000/task1'
    let options = {
        mode: 'no-cors',
        method: 'post',
        credentials: 'include'
    }
    let headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    let r = await fetch(url, {
        headers: headers
    }, options);

    let response = await r.json().then(data => data);
    console.log('done')

    let result = [];
    for (let iter in response) {
        let e = response[iter];
        let line = {
            name: e.name,
            x: e.visualFeedback / e.totalAmount,
            y: e.impressionTotal / e.totalAmount
        }
        result.push(line)
    }

    return result;
}
export async function getDataForTask2() {


    console.log("wait")

    let url = 'http://localhost:5000/task2'
    let options = {
        mode: 'no-cors',
        method: 'post',
        credentials: 'include'
    }
    let headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    let r = await fetch(url, {
        headers: headers
    }, options);

    let response = await r.json().then(data => data);
    console.log('done')

    let result = {
        labels: ['Other'],
        values: [0],
    };

    for (let iter in response) {
        let e = response[iter];
        if (e.totalAmount >= 15) {
            result.labels.push(e.name);
            result.values.push(e.totalAmount);
        } else {
            result.values[0] += e.totalAmount;
        }
    }

    return result;
}

export async function getDataForTask3() {

    console.log("wait")

    let url = 'http://localhost:5000/task3'
    let options = {
        mode: 'no-cors',
        method: 'post',
        credentials: 'include'
    }
    let headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    let r = await fetch(url, {
        headers: headers
    }, options);

    let response = await r.json().then(data => data);
    console.log('done')


    let datasets = {
        years: [],
        avgSumImpressionTotal: [],
        avgSumDescriptionInformative: [],
        avgSumVisualFeedback: [],
    }

    for (let iter in response) {
        let e = response[iter];

        datasets.years.push(iter);
        datasets.avgSumImpressionTotal.push(e.sumImpressionTotal / e.totalAmount);
        datasets.avgSumDescriptionInformative.push(e.sumDescriptionInformative / e.totalAmount);
        datasets.avgSumVisualFeedback.push(e.sumVisualFeedback / e.totalAmount);
    }

    return datasets;
}


