# badegg.service
デーモン設定ファイル

# How to use
/etc/systemd/system/  
に設置。その後、  
$ sudo systemctl daemon-reload  
$ sudo systemctl enable smartlock.service  
$ sudo systemctl start smartlock.service
を実行すると、自動的にプログラムが起動する。