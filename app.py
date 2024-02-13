from flask import Flask, request, jsonify
from rf_pred_sleep import train_and_predict

app = Flask(__name__)

@app.route('/')
def index():
    return "hello flask!"

# stress input


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # get average stress
        # on start, ask for sleep duration, physical activity, and stress

        input_data = request.json

        prediction_result = train_and_predict(input_data)

        return jsonify({'result': prediction_result})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)