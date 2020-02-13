var dataArray = [5,11,18];

var svg = d3.select("body").append("svg")
    .attr("height","100%")
    .attr("width","100%");

svg.selectAll("rect")
  .data(dataArray)
  .enter().append("rect")
            .attr("height", function(data, index) { return data*15; })
            .attr("width", "50")
            .attr("x", function(data, index) { return 60*index; })
            .attr("y", function(data, index) { return 300-(data*15); })
            .attr("fill", "pink")

