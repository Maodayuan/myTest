class System:
    def __init__(self):
        self.Member = {}
        self.User = {'username': '未登入'}

    def menu(self):
        print(self.Member)
        title = '''=======登⼊系统=======
        1.登⼊
        2.注册
        3.退出
                '''
        print(title)
        try:
            number = int(input('请输入:'))
            if number not in [1, 2, 3]:
                print('请输入1,2,3')
                self.menu()
            elif number == 1:
                self.sign_in()
            elif number == 2:
                self.sign_up()
            elif number == 3:
                self.quit_out()
        except ValueError:
            print('请输入数字')
            self.menu()

    def listed(self):
        title = '''=======登⼊页面=======
        1.登出账号
        2.修改密码
        3.退出
                    '''
        print(title)
        print('当前登录用户:', self.User['username'])
        try:
            number = int(input('请输入:'))
            if number not in [1, 2, 3]:
                print('请输入1,2,3')
                self.listed()
            elif number == 1:
                self.sign_out()
            elif number == 2:
                self.change()
            elif number == 3:
                self.quit_out()
        except ValueError:
            print('请输入数字')
            self.listed()

    def change(self):
        change_word = input('请输入新的密码')
        if len(change_word) != 8 or ' ' in change_word:
            print('密码必须为8位且不能为空格')
            while True:
                enter = input("请输⼊q回到修改密码功能:")
                if enter == 'Q' or enter == 'q':
                    self.change()
                else:
                    continue
        else:
            self.Member[self.User['username']] = change_word
            print('修改密码成功')
        self.menu()

    def sign_out(self):
        self.User['username'] = '未登入'
        print('登出成功')
        self.menu()

    def sign_in(self):
        print('请输入账号密码')
        username = input('账号:')
        password = input('密码:')
        if username in self.Member.keys():
            if self.Member[username] == password:
                print('登入成功')
                self.User['username'] = username
                self.listed()
                return
            else:
                print('账号或密码不对')
        else:
            while True:
                enter = input("不存在⽤户,请输⼊q回到⾸⻚选择注册功能:")
                if enter == 'Q' or enter == 'q':
                    self.menu()
                    break
                else:
                    continue

    def sign_up(self):
        print('请输入需要注册的账号密码')
        username = input('账号:')
        password = input('密码:')
        if username in self.Member.keys():
            print('账号已存在')
            while True:
                enter = input("请输⼊q回到注册功能:")
                if enter == 'Q' or enter == 'q':
                    self.sign_up()
                else:
                    continue
        elif ' ' in username:
            print('输⼊账号不能有空格')
            while True:
                enter = input("请输⼊q回到注册功能:")
                if enter == 'Q' or enter == 'q':
                    self.sign_up()
                else:
                    continue
        elif len(password) != 8 or ' ' in password:
            print('密码必须为8位且不能为空格')
            while True:
                enter = input("请输⼊q回到注册功能:")
                if enter == 'Q' or enter == 'q':
                    self.sign_up()
                else:
                    continue
        else:
            self.Member[username] = password
            print('注册成功')
        self.menu()

    @staticmethod
    def quit_out():
        print('欢迎下次使⽤')


if __name__ == "__main__":

    star = System()
    star.menu()
