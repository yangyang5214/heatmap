import argparse
import os.path

import garth


class GarminLogin:
    username = ""
    password = ""
    domain = ""

    def __init__(self, user, pwd, is_cn):
        self.username = user
        self.password = pwd
        if is_cn:
            self.domain = 'garmin.cn'

    def gen_secret(self, p) -> bool:
        if self.domain:
            garth.configure(domain=self.domain)
        try:
            if not os.path.exists(p):
                print('new login')
                garth.login(self.username, self.password)
                garth.client.dump(p)
            else:
                print('load token from cache')
            garth.client.load(p)
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", action="store", required=True, help="email")
    parser.add_argument("-p", "--pwd", action="store", required=True, help="pwd")
    parser.add_argument("--cn", action="store_true", help="if garmin accout is cn",
                        )
    options = parser.parse_args()
    print(options)
    login = GarminLogin(options.user, options.pwd, options.cn)
    p = '.garth_' + options.user
    is_success = login.gen_secret(p)
    if is_success:
        print('success')
