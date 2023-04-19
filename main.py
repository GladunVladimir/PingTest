import os
import subprocess

def ping_test(host):
    reached = []
    not_reached = []
    file = open("ping.txt", "a")
    for ip in host:
        # response = os.system('ping -c 30 %s' % ip)
        print(ip)
        try:
            response = subprocess.check_output(
                ['ping', '-c', '30', ip],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
        except subprocess.CalledProcessError:
            response = None

        file.write(response)

        if response == 0:
            reached.append(ip)
        else:
            not_reached.append(ip)
    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
    file.close()


hosts = [
        "92.223.6.71",  # 0 claster TanksBlitz
         "92.223.33.41",  # 1 claster
         "92.38.156.13", "92.38.156.93", "92.38.156.142", "92.38.156.189",  # 3 claster
         "92.223.4.191",    # 4 claster
         "92.223.41.195",   # 5 claster
         "92.223.57.35", "92.223.57.86" # 0 claster WotBlitz
         "92.223.39.65", "92.223.39.58" # 1 claster
         "92.223.45.13", "92.223.45.12" # 2 claster

         ]
ping_test(hosts)

# TanksBlitz
# claster 0
# Name:	login0.tanksblitz.ru
# Address: 92.223.6.71
# claster 1
# Name:	login1.tanksblitz.ru
# Address: 92.223.33.41
# claster 2
# Name:	login2.wotblitz.ru
# Address: 92.223.14.149
# Name:	login2.wotblitz.ru
# Address: 92.223.14.150
# Name:	login2.wotblitz.ru
# Address: 92.223.14.152
# Name:	login2.wotblitz.ru
# Address: 92.223.14.151
# claster 3
# Name:	login3.wotblitz.ru
# Address: 92.38.156.13
# Name:	login3.wotblitz.ru
# Address: 92.38.156.93
# Name:	login3.wotblitz.ru
# Address: 92.38.156.142
# Name:	login3.wotblitz.ru
# Address: 92.38.156.189
# claster 4
# Name:	login4.tanksblitz.ru
# Address: 92.223.4.191
# claster 5
# Name:	login5.tanksblitz.ru
# Address: 92.223.41.195


# WotBlitz
# claster 0
# Name:	login0.wotblitz.com
# Address: 92.223.57.35
# Name:	login0.wotblitz.com
# Address: 92.223.57.86
# claster 1
# Name:	login1.wotblitz.com
# Address: 92.223.39.65
# Name:	login1.wotblitz.com
# Address: 92.223.39.58
# claster 2
# Name:	login2.wotblitz.com
# Address: 92.223.45.13
# Name:	login2.wotblitz.com
# Address: 92.223.45.12

