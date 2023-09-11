import requests

def is_cdn_domain(domain):
    try:
        response = requests.get("http://" + domain)
        server_header = response.headers.get('Server')
        if server_header and "CDN" in server_header:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

domain = "14.119.104.254"  # 要判断的域名
is_cdn = is_cdn_domain(domain)
print(is_cdn)