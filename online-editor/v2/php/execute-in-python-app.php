<?php
// URL of the Python app
$pythonAppURL = 'http://localhost:5000/run'; // Replace with actual URL

// Check if there's code to forward
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['code'])) {
    $code = $_POST['code'];

    // Initialize cURL session
    $ch = curl_init($pythonAppURL);

    if ($ch === false) {
        die("Failed to create cURL session");
    }

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(array('code' => $code)));
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($ch, CURLOPT_TIMEOUT, 10); // Timeout for the request, in seconds

    // Execute the POST request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        curl_close($ch);
        die("cURL request error: " . $error_msg);
    }

    // Get HTTP response status
    $http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // Check if the response is successful
    if ($http_status != 200) {
        die("Error: Python app returned HTTP status code " . $http_status);
    }

    // Send the response back to the HTML editor
    echo $response;
} else {
    echo "No code provided.";
}
?>
