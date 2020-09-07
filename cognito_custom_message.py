# -*- coding:utf-8 -*-

def handler(event, context):
    if event['triggerSource'] == 'CustomMessage_AdminCreateUser':
        customed_event = custom_message_admin_create_user(event)

    return customed_event


def custom_message_admin_create_user(event):

    email_message = '''
{username} 様
<br>
<br>
管理者から招待されました。
<br>
<br>
ログインメールアドレス：{mail}
<br>
初回ログインパスワード：{password}
'''.format(username='{username}',
           mail=event['request']['userAttributes']['email'],
           password='{####}')

    event['response']['emailSubject'] = '仮パスワード発行のお知らせ'
    event['response']['emailMessage'] = email_message

    return event
