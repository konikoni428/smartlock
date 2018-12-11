# -*- coding: utf-8 -*-
import sqlite3
from contextlib import closing
db_name = "manager.db"


def make_info(student_id, name, idm):
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()

        sql = "insert into users(student_id,name,idm) values(?,?,?)"
        param = (student_id, name, idm)
        c.execute(sql, param)

        conn.commit()


def confirm(student_id, idm):
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        sql = "SELECT student_id,name,idm FROM users WHERE student_id = ?"
        param = (student_id,)
        try:
            c.execute(sql, param)
        except sqlite3.Error:
            return False
        for row in c:
            idm_db = row[2]
            name = row[1]
        try:
            if idm_db == idm:
                sql = "insert into logs (student_id, name,enter_time) values (?,?,datetime('now','localtime'))"
                try:
                    param = (student_id, name)
                    c.execute(sql, param)
                    conn.commit()
                    return True
                except sqlite3.Error:
                    return False
        except NameError:
            return False

        else:
            return False


def find_name(student_id):
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        sql = "SELECT student_id,name FROM users WHERE student_id = ?"
        param = (student_id,)
        try:
            c.execute(sql, param)
        except sqlite3.Error:
            print 'Database Error'
        for row in c:
            name = row[1]
        return str(name)


def button_info_insert():
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        sql = "insert into logs (name,leave_time) values ('button',datetime('now','localtime'))"
        try:
            c.execute(sql)
            conn.commit()
        except sqlite3.Error:
            print ("Database Insert Error")


def rename_user(student_id, new_name):
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        sql = "UPDATE users SET name = ? WHERE student_id = ?"
        param = (new_name, student_id)
        try:
            c.execute(sql, param)
            conn.commit()
        except sqlite3.Error:
            print ("Database Error")


def delete_user(student_id):
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        sql = "DELETE FROM users where student_id = ?"
        param = (student_id, )
        try:
            c.execute(sql, param)
            conn.commit()
        except sqlite3.Error:
            print ("Database Error")
