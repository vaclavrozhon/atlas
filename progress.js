/* Observations use the public solution date on each selected problem. */
(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('timeline-data').textContent);
  const formatDay = d3.utcFormat('%b %-d, %Y');
  const percent = d3.format('.1~%');
  const points = data.points.map(([day, count]) => ({
    day: d3.utcParse('%Y-%m-%d')(day),
    count,
    share: count / data.total,
  }));
  const first = points[0], last = points[points.length - 1];
  const fullEnd = new Date(Math.max(d3.utcYear.offset(first.day, 3), last.day));
  const chart = document.getElementById('progress-chart');
  const zoom = document.getElementById('zoom');
  const svg = d3.select(chart);
  const plot = svg.append('g');

  function draw() {
    const {width, height} = chart.getBoundingClientRect();
    if (!width || !height) return;
    svg.attr('viewBox', [0, 0, width, height]);
    plot.selectAll('*').remove();
    const left = 44, right = width - 12, top = 16, bottom = height - 34;
    const end = zoom.checked ? new Date(Math.max(+last.day, +d3.utcDay.offset(first.day, 1))) : fullEnd;
    const x = d3.scaleUtc([first.day, end], [left, right]);
    const y = d3.scaleLinear([0, 1], [bottom, top]);
    if (zoom.checked) y.domain([0, last.share || 1 / data.total]).nice(4);
    const yTicks = zoom.checked ? y.ticks(4) : [0, .25, .50, .75, 1];
    const grid = plot.selectAll('g.y-tick').data(yTicks).join('g').attr('class', 'y-tick')
      .attr('transform', value => 'translate(0,' + y(value) + ')');
    grid.append('line').attr('class', 'grid-line').attr('x1', left).attr('x2', right);
    grid.append('text').attr('x', left - 8).attr('dy', '0.32em').attr('text-anchor', 'end').text(percent);

    const xTicks = zoom.checked ? x.ticks(width < 500 ? 4 : 6) : x.ticks(d3.utcYear.every(1));
    const dateLabel = d3.utcFormat(zoom.checked && end - first.day < 60 * 86400000 ? '%b %-d' : '%b %Y');
    plot.selectAll('text.x-tick').data(xTicks).join('text').attr('class', 'x-tick')
      .attr('x', x).attr('y', bottom + 22)
      .attr('text-anchor', day => x(day) > right - 26 ? 'end' : 'middle')
      .text(dateLabel);

    const step = d3.line().x(point => x(point.day)).y(point => y(point.share)).curve(d3.curveStepAfter);
    plot.append('path').attr('class', 'series').attr('d', step(points));
    plot.append('circle').attr('class', 'endpoint').attr('r', 4.5).attr('cx', x(last.day)).attr('cy', y(last.share));
    const anchorLeft = x(last.day) > right - 70;
    plot.append('text').attr('class', 'endpoint-label').attr('text-anchor', anchorLeft ? 'end' : 'start')
      .attr('x', x(last.day) + (anchorLeft ? -7 : 7)).attr('y', Math.max(top + 4, y(last.share) - 9))
      .text(last.count + '/' + data.total);
    plot.selectAll('circle.observation').data(points).join('circle').attr('class', 'observation')
      .attr('cx', point => x(point.day)).attr('cy', point => y(point.share)).attr('r', 7).attr('fill', 'transparent')
      .append('title').text(point => formatDay(point.day) + ' · ' + point.count + ' of ' + data.total + ' (' + percent(point.share) + ')');
  }

  chart.removeAttribute('hidden');
  document.getElementById('zoom-control').hidden = false;
  zoom.addEventListener('change', draw);
  new ResizeObserver(draw).observe(chart);
  draw();
})();
