Write-Output "入退室管理システム管理スクリプト"

$input = Read-Host "何を実行しますか？（1：ユーザー追加　2：名前変更　3：ユーザー削除 その他:終了）"

switch($input){

  "1"{
  Write-Output "しばらくお待ちください。"
  ssh pi@192.168.1.12 -t 'stty erase ^H
  sh add_user.sh'
  }
 
  "2"{
  Write-Output "しばらくお待ちください。"
  ssh pi@192.168.1.12 -t 'stty erase ^H
  sh rename_user.sh'
  }
 
  "3"{
  Write-Output "しばらくお待ちください。"
  ssh pi@192.168.1.12 -t 'stty erase ^H
  sh delete_user.sh'
  }
  
default{
Write-Output "終了します。" 
}

}

Read-Host "終了しました。Enterを押してください。"