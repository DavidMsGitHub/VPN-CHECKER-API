import requests

proxy_check_io_key = "9f242efa5e6d73faea9960edf2c6c0c855a22c98b76b06ccd471edd95382b817"

def gii_check(ip):
    param = {
        "ip": ip,
        "contact": "dato2006213@gmail.com",
        "flag": "m"
    }
    result = requests.get("http://check.getipintel.net/check.php", params=param)
    if result.text == "0":
        return "Not VPN"
    elif result.text == "1":
        return "is VPN"
    else:
        return "Something went wrong..."

def proxy_checkio(ip):
    param = {
        "key": proxy_check_io_key,
        "risk": 1,
        "vpn": 3
    }
    response = requests.get(f"http://proxycheck.io/v2/{ip}", params=param)
    result = response.json()
    if "yes" in result[ip]["vpn"] and "yes" in result[ip]["proxy"]:
        return "is VPN/Proxy"
    elif "yes" in result[ip]["vpn"] and "no" in result[ip]["proxy"]:
        return "is VPN"
    elif "no" in result[ip]["vpn"] and "yes" in result[ip]["proxy"]:
        return "is Proxy"
    elif "no" in result[ip]["vpn"] and "no" in result[ip]["proxy"]:
        return "Not VPN or Proxy"
    else:
        return "Something went wrong..."

