"""
Имеется лог-файл, в котором хранится статистика запросов к серверу в виде «ip bytes» через пробел, по одному хосту на
строку:

127.0.0.1 120
10.1.1.1 210
127.0.0.1 80
10.1.1.1 215
10.1.1.1 200
10.1.1.2 210


Нам необходимо вычислить суммарный объем траффика на каждый хост и выдать его в виде списка в поряке убывания траффика.
"""

ip_log = [x.split(" ") for x in open("05_ip.txt")]
# print(ip_log)

ip_stat = {}
for ip, traffic in ip_log:
        if ip in ip_stat:
                ip_stat[ip] += int(traffic)
        else:
                ip_stat[ip] = int(traffic)
print(ip_stat)
ip_traffic_summary = 0
for ip_address, ip_traffic in ip_stat.items():
        print('{}\t{}'.format(ip_address, ip_traffic))
        ip_traffic_summary += ip_traffic
print('-' * 20)
print('Summary:\t{}'.format(ip_traffic_summary))

