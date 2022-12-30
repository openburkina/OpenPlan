export function pieStatAdapter(input_data) {
    let labels = ["Identification", "Implementation", "Finalisation", "Closed", "Cancelled", "Suspended"]
    let data = [
        input_data['Identification'],
        input_data['Implementation'],
        input_data['Finalisation'],
        input_data['Closed'],
        input_data['Cancelled'],
        input_data['Suspended'],
    ]
    return {labels: labels, data: data} 
}

export function lineStatAdapter(input_data, start_year, end_year) {
    let labels = []
    let data = []
    for (let i = 0; i <= parseInt(end_year) - parseInt(start_year); i++) {
        labels.push(i + parseInt(start_year))
    }
    let a = input_data.reduce(function (r, a) {
        r[a.name] = r[a.name] || {};
        r[a.name][a.planned_start] = a.value;
        return r;
    }, Object.create(null));
    for (let [k, v] of Object.entries(a)) {
        let new_data = labels.map((year_value, i) => v[parseInt(start_year)+i] || 0 )
        data.push({name: k, data: new_data})
    }
    return {labels, data} 
}

export function barStatAdapter(input_data) {
    let labels = []
    let data = []
    for (let o of input_data) {
        labels.push(o.name)
        data.push(o.value)
    }
    return {labels, data} 
}