from whois import whois
#域名查询
# try:
#     whois_data = whois('www.1688.com')
#     print(whois_data)
#     print(whois_data['state'])#地方
#     print(whois_data['country'])#国家
# except Exception as e:
#     print('查不到有效信息！')


def query_domain(domain):
    try:
        whois_data = whois(domain)
        # print(whois_data)
        # print(whois_data['state'])  # 地方
        # print(whois_data['country'])  # 国家
        data = {
            'city': whois_data['state'],
            'country': whois_data['country']
        }
        return data
    except Exception as e:
        return False


if __name__ == '__main__':
    print(query_domain('www.tencent.com'))