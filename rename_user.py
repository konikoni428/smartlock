# -*- coding: utf-8 -*-
import database
import slack

print "ユーザー名を変更します。"
# inputして古い名前を取得
student_id = raw_input("変更するユーザーの学籍番号を入力してください:").upper()
# エラー処理
try:
    old_name = database.find_name(student_id)
except UnboundLocalError:
    print "学籍番号が不正または登録されていません。"
    exit(1)
print "あなたの現在の名前は %s です。" %old_name
# 新しい名前を取得
new_name = raw_input("新しい名前を入力してください:")
# データベースに反映
database.rename_user(student_id, new_name)
# 反映の確認
new_db_name = str(database.find_name(student_id))
print "あなたの名前は %s に変更されました。" %new_name
# Slackにぶんなげる
slack.rename_user(old_name, new_name)