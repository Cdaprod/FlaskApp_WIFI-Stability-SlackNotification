# Wi-Fi Connection Monitor

This repository contains a Python Flask API and a monitoring script that checks the status of a machine's Wi-Fi connection and sends a Slack notification when the connection is lost and then restored.

## Structure

- `app.py` - This is the Flask API that runs on the machine being monitored. It has a single endpoint (`/status`) that returns a JSON object indicating that the machine is online.
- `monitor.py` - This script periodically checks the machine's status by sending a request to the Flask API. If the connection to the machine is lost and then restored, it sends a Slack notification.

## Usage

1. Clone this repository and navigate to its directory.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Set your Slack API token as an environment variable: `export SLACK_API_TOKEN='your-slack-api-token'`.
4. Run the Flask API on the machine you want to monitor: `python app.py`.
5. Run the monitoring script on a separate machine or device: `python monitor.py`.

## Contribution

We welcome contributions to this project! Here's how you can help:

1. Fork this repository.
2. Make your changes in a new branch.
3. Test your changes to ensure they work as expected and don't introduce bugs.
4. Submit a pull request with your changes.

Please include a clear and detailed explanation of your changes in your pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
