# clip studio speak converter
シナリオ用テキストから漫画のセリフに流し込んでいく形に変換かけるスクリプト  
windows 用の mecab-python が今までうまく入らなかったので保留していたが、再開  
mac の方で今確認とれてません  
使用は自己責任で  

## convertCspText.py
本体。「」や()等で囲われたセリフから「」（）記号を排除、長い文を複数の行に変換する  
mecab使用の場合、文末が意味のある単語区切りになるように処理(mecab不使用の場合単に文字数で改行する)  
  
テキストの区切りを判定する記号は下記のもので、外にあるテキストは除去される  
  
+ 「」 :会話の内容、口に出して喋っている内容
+ （） :考え事、思っていること
+ <>  :説明、モノログなど四角で囲った内容  
![sample](./ss.png)

今後の課題  
三点リーダ（…）のみならず、!!や♡といった記号が折り返しになる可能性が高い  
が、ほとんどのこれらはMeCab上ではただの「記号」としてまとめられているため、文末記号とそうでないものを判別できるようにする必要がある  

### copy_paste.py
macでのクリップボード処理用  
  
###  speakingConvert.py / speakingConvertPage.py / speakingConvertScene.py
それぞれページ単位、複数頁でのシーン単位、段単位で使用
