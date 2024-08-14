# Docker-Compose Task

## To build Docker-compose for this task
docker-compose up --build

Once the build is completed, Flask app will start serving content on **/metrics** for second container - http:localhost:5000/metrics and all the request made to first web container - http://localhost:80 will function as expected (displays - it works! solved by Anshul Gupta)

## Important -- All the request made to first web container at /metrics endpoint, i.e https://localhost:80/metrics will also be redirected to show the metrics of the second container - http:localhost:5000/metrics.
