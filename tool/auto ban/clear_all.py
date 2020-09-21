import time

CAPCHA = 'Opeviengi'
print('CAPCHA: {}'.format(CAPCHA))
p = input("Xác nhận tạo mới tất cả file (không bao gồm các bản backup, etc...)? Y/n: (write CAPCHA) ")

def clear_men(path):
    with open(path, 'r') as r:
        with open('backup/' + path, 'w') as w:
            w.write("".join(r.readlines()))
            w.close()
        r.close()
    w = open(path, 'w')
    w.close()

if p == CAPCHA:
    files = ['debug.log', 'error_id.txt', 'id_need_to_ban.txt', 'id-openid.txt', 'openid_need_to_ban.txt']
    
    for file in files:
        clear_men(file)
    print('Done!\nWait 2s to exit!')
    time.sleep(2)
else:
    print('NOPE!')
    time.sleep(2)