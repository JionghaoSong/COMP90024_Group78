#!/bin/bash

# Check if kubectl command is available
if ! command -v kubectl &> /dev/null; then
    echo "Error: kubectl command not found. Make sure it's installed and in your PATH."
    pip install kubernetes
fi

# Start port forwarding
kubectl port-forward service/router -n fission 9090:80 &
PORT_FORWARD_PID=$!

# Function to cleanup port forwarding when the script exits
cleanup() {
    kill $PORT_FORWARD_PID
}

# Trap SIGINT and SIGTERM signals to perform cleanup
trap cleanup INT TERM

# Wait for port forwarding to start
sleep 5

# Make the curl request, capture the HTTP response code and echo it
response_code=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:9090/sensor5k-fetch")
echo "Response Code: $response_code"

# End port forwarding
cleanup
