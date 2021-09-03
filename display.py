# author: ZhaoKun
# contact: 1161678627@qq.com
# datetime: 2021-02-26 21:37
# software: PyCharm

from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QLineEdit, QInputDialog
from ui import Ui_Form as Ui_MainWindow
import json
import requests
import chenwujian_every_day

class display(QMainWindow):
    def __init__(self):
        super(display, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setVisible(False)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.pushButton.clicked.connect(self.process_login)
        self.ui.pushButton_2.clicked.connect(self.process_submit)
        # 禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())
        self.exit = 0
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        title, okPressed = QInputDialog.getText(
            self,
            "config",
            "请输入服务ip:",
            QLineEdit.Normal,
            "10.175.72.156")
        self.ip = 'http://'+title+':8000/storage'
        if not okPressed:
            exit()

    def process_login(self):
        self.username = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        if self.username == '' or self.password == '':
            QMessageBox.about(self, '警告', '账号或密码为空')
        else:
            self.session, response = chenwujian_every_day.login_account(self.username, self.password)
            if '操作成功' in response:
                self.ui.pushButton_2.setVisible(True)
            else:
                QMessageBox.about(self, '错误', '账号或密码错误，\n登陆失败！')
                self.session.close()

    # 将账号，密码，是否是新校区 post至服务器
    def process_submit(self):
        # 检测是否开启新校区,复选框被选中返回True
        if self.ui.checkBox.isChecked():
            xinxiaoqu = 1
        else:
            xinxiaoqu = 0

        try:
            # url = 'http://127.0.0.1:8000/storage'
            url = self.ip
            data = json.dumps({'username': self.username, 'password': self.password, 'xinxiaoqu': xinxiaoqu})
            response = requests.post(url=url, data=data)
        except:
            QMessageBox.about(self, '警告', '服务器错误，\n请稍后再试！')
            self.exit = 1

        if self.exit:
            self.session.close()
            exit()
        # print(response.text)

        # # 服务器将信息都存入数据库中
        # response = chenwujian_tianbao.submit_data(self.session, xinxiaoqu)
        # print(response)
        if 'success' in response.text:
            QMessageBox.about(self, '提示', '当前账号以设置为自动填报模式！')
            self.ui.pushButton_2.setVisible(False)
            self.session.close()
        else:
            QMessageBox.about(self, '警告', '自动填报模式开启失败！\n请退出重试')
            self.session.close()
            exit()


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon(resource_path('icon.jpg')))
    activate = display()
    activate.show()
    app.exec_()