# -*- coding: utf-8 -*-
import database
import slack

print "ユーザーを削除します。"
# inputして古い名前を取得
student_id = raw_input("削除するユーザーの学籍番号を入力してください:").upper()
# エラー処理
try:
    name = database.find_name(student_id)
except UnboundLocalError:
    print "学籍番号が不正または登録されていません。"
    exit(1)
print "削除する方の名前は %s です。" %name
# 確認
answer = input("本当に削除しますか？\n削除する場合は1を入力してください:")
if answer is 1:
    # データベースに反映
    database.delete_user(student_id)
    slack.delete_user(student_id, name)
    print "削除しました。"
else:
    print "終了します。"
    exit(0)
