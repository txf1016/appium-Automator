# coding:utf8
import os

root_path = os.path.dirname(__file__)
app_path = os.path.join(root_path, 'app/').replace('\\', '/')
app_name_path = app_path + os.listdir(app_path)[0]
screenShot_path = os.path.join(root_path, 'screenShot/')
resultReport_path = os.path.join(root_path, 'resultReport/')
# conf_path = os.path.join(root_path, '').replace('\\', '/')

# 验证
# print 'root_path: ' + root_path
# print 'app_name_path: ' + app_name_path
# print 'app_path: ' + app_path
# print 'resultReport_path: ' + resultReport_path
# print 'screenShot_path: ' + screenShot_path
