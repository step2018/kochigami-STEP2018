# HW1

## How to execute

`python hw1.py`  

Then, enter characters shown in apps
Note: Please enter `q` when `Qu` appears.  

ex. 
```
python hw1.py 

Enter alphabets: moonstarer
```
Finally, you will get the results like this. 
`I found: astronomer 11`

Please enter the result (astronomer) in apps.  
Enjoy! :)

## My STEP

### step 0
`add round-robin competition`  

入力文字を16, 15, 14, ..., 2文字選んで，辞書の単語の文字と逐一比較．  
入力文字も辞書もアルファベットを順番に一つずつリストに入れて一致するかを見る．  
アルファベットの順番は考えていないので，多少計算は早くなる．  

`score: 1051 time: 25m46s`

### step 1
`use dict for separating number of chars`  

辞書の単語を文字数でグループ分けした．  
入力文字を16, 15, 14, ..., 2文字選んで，辞書の単語の文字と逐一比較．  
調べる辞書は選んだ入力文字数のグループのものだけにした．  
step 0より計算は早くなった．  

```
score: 1020 time: 4m8s
score: 1068 time: 4m15s
score: 1264 time: 3m48s
score: 1262 time: 3m53s
```

### step 2
`search based on word length`

発想を変えた．  
入力文字全てを使うなら，最大16文字なので，16, 15, 14, 13, ..., 2文字の単語グループを検索し，入力文字の中に必要なアルファベットが全て含まれるかを調べた．    
後ほど，`intersection` を取る方法では，重複するアルファベットが1つにまとめられてしまうことに気づいた．（例えば，2つ「o」を使う文字は除外されてしまうので，バグになる．）  

`score: 1438 time: 3m20s`

### step 3
`select word of maximum point`

step2の方針はそのまま用いる．  
見つかった単語は全部リストに入れて，獲得点数を計算し，最高点を出すものを選ぶようにした．  

`score: 1539 time: 3m26s`

### step 4
`calculate intersection with duplication`

辞書の中の単語に，1つのアルファベットが複数含まれる場合でも，入力文字の中に必要なアルファベットが全て含まれるか調べられるようにした．  
step2の方針よりも，長い単語を見つけられるようになった．  

`score: 1728 time: 3m26s`

## My impressions

高得点の単語を見つけられた時は爽快だった．  
やみつきになり，ゲーム廃人になりそうだった．  

## Future work

自動で解くにはどうしたらよいのだろう？