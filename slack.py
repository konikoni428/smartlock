# -*- coding: utf-8 -*-
import urllib2
import json

url = 'YOUR URL'


def send_slack(Name):
    body = "%sが入室しました" % Name
    data = json.dumps({"text": body})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print "slack_error"
    f.close()


def button():
    data = json.dumps({"text": "退出しました"})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print "slack_error"
    f.close()


def add_user(stu_id, name):
    body = "学籍番号 %s 名前 %s のユーザーを追加しました。" %(stu_id, name)
    data = json.dumps({"text": body})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print "slack_error"
    f.close()


def rename_user(old_name, new_name):
    body = "%s は %s に名前を変更しました。" %(old_name, new_name)
    data = json.dumps({"text": body})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print "slack_error"
    f.close()


def delete_user(student_id, name):
    body = "学籍番号 %s の　%s さんがデータベースから削除されました。" %(student_id, name)
    data = json.dumps({"text": body})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print "slack_error"
    f.close()
