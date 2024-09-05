from flask import Flask, url_for, jsonify
from checks import gii_check, proxy_checkio

app = Flask(__name__)

@app.route("/check_ip/<string:ip_addr>")
def check_ip(ip_addr):
    if ip_addr:
        return jsonify({
            "GetIpIntel": gii_check(ip_addr),
            "Proxy-Check.io": proxy_checkio(ip_addr)
        })



if __name__ == "__main__":
    app.run(debug=True)