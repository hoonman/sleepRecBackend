# sleepRecBackend
backend service for the sleeprec application responsible for connecting machine learning with the React Native app

use this command below to test the API call. This command makes a POST request to http://127.0.0.1:5000/predict with the JSON data in the request body.
```curl -X POST -H "Content-Type: application/json" -d '{"Age": 30, "Sleep Duration": 7, "Physical Activity Level": 3, "Stress Level": 5, "Heart Rate": 70, "Daily Steps": 8000}' http://127.0.0.1:5000/predict```

