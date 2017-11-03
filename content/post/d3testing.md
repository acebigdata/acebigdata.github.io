
---
title: "Visualization"
date: 2017-11-02
tags: ["", ""]
categories: ["Visualization"]
menu:
  main:
    parent: Javascript
---


---
title: "Start Writing"
date: 2017-11-03
tags: ["", ""]
categories: ["python"]
menu:
  main:
    parent: Python
---

Start writing...


Try to embed d3 into the md

<body>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script>

var data = d3.range(40).map(function(i) {
  return i % 5 ? {x: i / 39, y: (Math.sin(i / 3) + 2) / 4} : null;
});

var margin = {top: 40, right: 40, bottom: 40, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scaleLinear()
    .range([0, width]);

var y = d3.scaleLinear()
    .range([height, 0]);

var line = d3.line()
    .defined(function(d) { return d; })
    .x(function(d) { return x(d.x); })
    .y(function(d) { return y(d.y); });

var svg = d3.select("body").append("svg")
    .datum(data)
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.append("g")
    .attr("class", "axis axis--x")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

svg.append("g")
    .attr("class", "axis axis--y")
    .call(d3.axisLeft(y));

svg.append("path")
    .attr("class", "line")
    .attr("d", line);

svg.selectAll(".dot")
  .data(data.filter(function(d) { return d; }))
  .enter().append("circle")
    .attr("class", "dot")
    .attr("cx", line.x())
    .attr("cy", line.y())
    .attr("r", 3.5);

</script>
