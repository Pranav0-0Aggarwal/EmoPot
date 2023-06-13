def webpage(name, temperature, moisture, sunlight, humidity, health):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plant Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
              body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 20px;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.plant {
  max-width: 600px;
  margin: 0 auto;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

h2 {
  color: #333;
  margin-top: 0;
}

.values {
  margin-top: 20px;
}

.values p {
  margin: 5px 0;
  color: #555;
}

hr {
  border: none;
  height: 2px;
  background-color: #ccc;
  margin-top: 20px;
}

.health-line {
  height: 20px;
  background-color: #f4f4f4;
  border-radius: 10px;
  position: relative;
  margin-top: 20px;
}

.health-line-progress {
  height: 100%;
  background-color: #ffd700;
  border-radius: 10px;
  transition: width 0.3s ease-in-out;
}

.health-line-text {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 10px;
  color: #333;
  font-weight: bold;
  font-size: 14px;
}

/* Chart.js custom colors */
.chart-color-1 {
  background-color: #007bff;
}

.chart-color-2 {
  background-color: #6c757d;
}

.chart-color-3 {
  background-color: #17a2b8;
}

.chart-color-4 {
  background-color: #ffc107;
}

/* Media queries for mobile responsiveness */
@media only screen and (max-width: 600px) {
  .plant {
    max-width: 100%;
    padding: 10px;
  }

  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }

  h2 {
    font-size: 20px;
  }

  .values p {
    font-size: 14px;
  }

  .health-line-text {
    font-size: 12px;
  }
}

            """
    html += f"""
        </style>
    </head>
    <body>
        <h1>Plant Dashboard</h1>

        <div id="plants">
            <div class="plant">
                <h2 id="plant_name_1">{name} <i class="fas fa-seedling"></i></h2>
                <div>
                    <canvas id="chart_1"></canvas>
                </div>
                <div id="values_1" class="values">
                    <p>Temperature: {temperature}</p>
                    <p>Moisture: {moisture}</p>
                    <p>Sunlight: {sunlight}</p>
                    <p>Humidity: {humidity}</p>
                </div>
                <hr>
                <div class="health-line">
                    <div id="health_line_progress_1" class="health-line-progress"></div>
                    <div id="health_line_text_1" class="health-line-text"></div>
                </div>
            </div>
            <!-- Add more plant sections dynamically -->
        </div>

        <script>
            // Sample data for the chart
            const variables = ['Temperature', 'Moisture', 'Sunlight', 'Humidity'];
            const values = [{temperature}, {moisture}, {sunlight}, {humidity}];
            const thresholds = [20, 40, 60, 80, 100, 120, 140, 160];
            const health = {health}; // Health percentage value

            // Generate random colors for the chart bars
            const colors = variables.map(() => '#' + Math.floor(Math.random() * 16777215).toString(16));
            """
    html += """
            // Create the chart
            const ctx = document.getElementById('chart_1').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: variables,
                    datasets: [{
                        data: values,
                        backgroundColor: colors,
                        borderWidth: 1
                    }]
                },
                options: {
                    legend: { display: false },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });

            // Display values below the chart
            const valuesContainer = document.getElementById('values_1');
            for (let i = 0; i < variables.length; i++) {
                const valueElement = document.createElement('p');
                valueElement.textContent = `${variables[i]}: ${values[i]}`;
                valuesContainer.appendChild(valueElement);
            }

            // Update health line progress and text
            const healthLineProgress = document.getElementById('health_line_progress_1');
            const healthLineText = document.getElementById('health_line_text_1');
            healthLineProgress.style.width = `${health}%`;
            healthLineText.textContent = `${health}%`;
        </script>
    </body>
    </html>
    """
    return html


html = webpage("Emopot", 30, 90, 70, 30, 95)
print(html)