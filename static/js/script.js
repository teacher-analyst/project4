//get input from html
//call api which returns list of lga names
//load output to html

function selectionSubmitted() {
    let day_of_week = d3.select('#day_of_week').node().value;
    let accident_type = d3.select('#accident_type').node().value;
    let light_condition = d3.select('#light_condition').node().value;
    let road_geometry = d3.select('#road_geom').node().value;
    let speed_zone = d3.select('#speed_zone').node().value;
    let road_type = d3.select('#road_type').node().value;
    let severity = d3.select('#severity').node().value;
    let region_name = d3.select('#region').node().value;

    const prediction = `http://127.0.0.1:5000/api/v1.0/${day_of_week}/${accident_type}/${light_condition}/${road_geometry}/${speed_zone}/${road_type}/${severity}/${region_name}`
    const predictionPromise = d3.json(prediction);
    console.log("Prediction Promise: ", predictionPromise)
    console.log(prediction)

    
}