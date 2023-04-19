import os


def ping_test(host):
    reached = []
    not_reached = []
    for ip in host:
        ping_test = os.system('ping -c 30 %s' % ip)


        if ping_test == 0:
            reached.append(ip)
        else:
            not_reached.append(ip)
    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))


hosts = [
        "92.223.6.71",  # 0 server
         "92.223.33.41",  # 1 server
         "92.38.156.13", "92.38.156.93", "92.38.156.142", "92.38.156.189",  # 3 server
         "92.223.4.191",    # 4 server
         "92.223.41.195",   # 5 server
         ]
ping_test(hosts)
#
#
# # Name:	login0.tanksblitz.ru
# # Address: 92.223.6.71
#
# # Name:	login1.tanksblitz.ru
# # Address: 92.223.33.41
#
# # Name:	login2.wotblitz.ru
# # Address: 92.223.14.149
# # Name:	login2.wotblitz.ru
# # Address: 92.223.14.150
# # Name:	login2.wotblitz.ru
# # Address: 92.223.14.152
# # Name:	login2.wotblitz.ru
# # Address: 92.223.14.151
#
# # Name:	login3.wotblitz.ru
# # Address: 92.38.156.13
# # Name:	login3.wotblitz.ru
# # Address: 92.38.156.93
# # Name:	login3.wotblitz.ru
# # Address: 92.38.156.142
# # Name:	login3.wotblitz.ru
# # Address: 92.38.156.189
#
# # Name:	login4.tanksblitz.ru
# # Address: 92.223.4.191
#
# # Name:	login5.tanksblitz.ru
# # Address: 92.223.41.195