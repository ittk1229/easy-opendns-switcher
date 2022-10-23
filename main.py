from opendns import *

# モード選択
while True:
    mode = input('choose mode by typing r/p (restrict/permit) > ')
    if mode in ['r', 'restrict', 'p', 'permit']:
        break
    else:
        print('you must choose one of [restrict, permit]')

# ユーザ情報の読み込み
user_info  = json_to_obj('user_info.json')

# ユーザ情報を用いてOpenDNSにログイン
print('(1/5) installing driver...')
opendns = OpenDns(user_info['mail'], user_info['password'], user_info['network_id'])

opendns.login()
print('(2/5) login successful')

opendns.move_to_setting()
print('(3/5) move to setting')

# モードに応じて処理を実施
if mode in ['r', 'restrict']:
    print('(4/5) adding domains...')
    opendns.restrict()

    hour, minute, second = get_n_minutes_later(3)
    print(f'(5/5) blacklisted domains will not be available from {hour:02}:{minute:02}:{second:02}')
elif mode in ['p', 'permit']:
    print('(4/5) deleting domains...')
    opendns.permit()

    hour, minute, second = get_n_minutes_later(3)
    print(f"(5/5) you can use any domain from {hour:02}:{minute:02}:{second:02}")
