<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulk VPN Checker</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #2c3e50;
            font-size: 3em;
            text-align: center;
            margin-bottom: 10px;
        }
        h3, h5, h6 {
            font-weight: normal;
            color: #34495e;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 30px;
            color: #8e44ad;
        }
        .gela {
            color: #e74c3c;
            font-weight: bold;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 10px;
        }
        p {
            font-size: 1.1em;
        }
        .divider {
            height: 2px;
            background-color: #8e44ad;
            margin: 20px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Welcome to Bulk VPN Checker</h1>
    <h3>This API will check IPs in multiple VPN Checker services to provide accurate results for VPN or Proxy usage.</h3>

    <div class="divider"></div>

    <h2>USAGE:</h2>
    <h5 class="gela">GET 127.0.0.1/check_ip/{IP}</h5>
    <h6>Replace {IP} with an actual IP Address.</h6>

    <div class="divider"></div>

    <h2>DevLog:</h2>
    <h5><p>This API currently supports 2 checkers, with more coming soon!</p></h5>
    <h5><p><strong>Supported:</strong> GetIpIntel, ProxyCheck.io</p></h5>
</div>

</body>
</html>
