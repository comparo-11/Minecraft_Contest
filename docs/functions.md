# 関数の仕様

## detectMobsDetail(int mode, char *buf）

- 引数  
    - int mode : MOBの種類  1の時クリーパー? 2の時ゾンビ?  
~~未確認~~
    - char *buf : txtから取得した文字列を格納する配列のアドレス  
~~高い確率で仕様変更有（intにする）~~  

- 戻り値  
    - char : *bufで受け取ったアドレス

- フォーマット  
    - MOBの種類(int 1桁), X座標(int 3桁), Y座標(int 3桁), width(int 3桁), height(int 3桁), 距離(int 3桁)   
    - MOBの種類以外の値は検出した数だけ出力されてるので、長くなる  
    - 距離はwidthの値を使って、検知したMOBの現在の大体の距離を計算して0, 1, 2で表示。(それぞれ近・中・遠)  

この関数では、modeによって開くtxtファイルを変え、そのファイルの中に記載されているMOBの検出情報をbufに入れる。  
この関数で出力される値は、もう一個の方と比べて細かい値になっている。  
現状ではmodeに1, 2以外が入るとエラーを出して終了する。  
detectMobsAboutと同時に使うことは現状できない。~~後日改良予定~~  
　
## detectMobsAbout(int mode, int *ibuf)

- 引数
    - int mode：detectMobsDetail関数と同様
    - int *ibuf ：detectMobsDetail関数と違い、数字(int)を格納する配列のアドレス  
　
- 戻り値
    - int *ibufで受け取ったアドレス
　
- フォーマット
    - MOBの種類(int 1桁), X座標(int 3桁), Y座標(int 3桁), 距離(int 3桁)  
    - X座標、Y座標は画像内を座標を基準に左・中・右で区切り、それぞれ0･1･2で表示  
    - 距離はdetectMobsDetail関数と同じ  

処理はdetectMobsDetail関数とほとんど同じで、文字列をintに変えて配列に入れる処理がある点だけ異なる。  
