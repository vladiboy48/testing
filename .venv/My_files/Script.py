from pathlib import Path
from time import sleep
from datetime import datetime
import os
import shutil
import sys
bin_path = Path('C:\\Program Files\\Jmeter\\apache-jmeter-5.6.3\\bin')
res_path = Path('C:\\Program Files\\Jmeter\\Результаты')
current_date = str(datetime.today().strftime('%d%m%Y'))
c_path = Path('C:\\Program Files\\Jmeter\\Результаты\\Хранилище',(current_date) + str('-ВТС(КСПД)'))
h_path = Path('H:\\VKorneev\\611.18 Заявка #372835 Подготовка нагрузочного тестирования и тестирования стабильности\\Результаты',(current_date) + str('-ВТС(КСПД)'))
count = 2
for report in list(bin_path.glob('*.download')):
    os.unlink(report)
for htmlka in list(bin_path.glob('*.html')):
    os.unlink(htmlka)
print('1.Скачанные файлы удалены из bin;')

if os.path.isdir(c_path):
    new_c_path = c_path
    new_h_path = h_path
    while os.path.isdir(new_c_path):
        new_c_path = Path(str(new_c_path) + ' - ' + str(count))
        new_h_path= Path(str(new_h_path) + ' - ' + str(count))
        count = count + 1
    os.makedirs(new_c_path)
    os.makedirs(new_h_path)
    c_path = new_c_path
    h_path = new_h_path
else:
    os.makedirs(c_path)
    os.makedirs(h_path)
print('2.На диске C и H создана папка с результатами \nСсылки для проверки:')
print(Path(c_path))
print(Path(h_path))
for cvs in list(res_path.glob('*.csv')):
    shutil.copy(cvs, c_path)
    shutil.copy(cvs, h_path)
for png in list(res_path.glob('*.png')):
    shutil.copy(png, c_path)
    shutil.copy(png, h_path)
for jmx in list(res_path.glob('*.jmx')):
    shutil.copy(jmx, c_path)
    shutil.copy(jmx, h_path)
print('3.Все готово! Незабудь почистить БД.')
sleep(2)
print('До выхода...')
for sec in range (5,0,-1):
    sleep(1)
    print (sec)
sys.exit
