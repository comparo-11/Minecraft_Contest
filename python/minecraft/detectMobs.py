import sys
sys.path.append('.')
sys.path.append('./python/')

from PIL import ImageGrab
import win32gui, time, os, logging

sys.path.append('.')
sys.path.append('./python/YOLO')
import detect

# 画面内のmob情報を格納するクラス
class mob:
    def __init__(self):
        #type 1:クリーパー, 2:ゾンビ　（嘘ついてるかも）
        self.type = 1
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.distance = 0

    def setData(self, result):
        data = result.split()
        self.type = int(data[0])
        self.x = float(data[1])
        self.y = float(data[2])
        self.width = float(data[3])
        self.height = float(data[4])
        self.distance = calcDistance(self.x)

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)
         
    # txtに書き込む
    # フォーマット：種類(1,2) X Y width height 距離
    # 種類以外0埋め三桁表示
    def outputDataDetail(self):
        i_x = (int)(self.x * 1000)
        i_y = (int)(self.y * 1000)
        i_width = (int)(self.width * 1000)
        i_height = (int)(self.height * 1000)

        # txtに書き込む内容
        txt = "{x:03.0f}{y:03.0f}{w:03.0f}{h:03.0f}{dist:03d}".format(x=i_x,y=i_y,w=i_width,h=i_height,dist=self.distance)

        writeTxt(txt, self.type)

    # フォーマット：種類(1,2) X軸位置 Y軸位置 距離
    # 全て１桁
    def outputDataAbout(self):
        x_pos = calcPosition(self.x)
        y_pos = calcPosition(self.y)

        # txtに書き込む内容
        txt = "{x:01d}{y:01d}{dist:01d}".format(x=x_pos,y=y_pos,dist=self.distance)

        writeTxt(txt, self.type)

# スクショ用関数
def captureMC(winHundle, windowSize):
    if winHundle:
        image = ImageGrab.grab(windowSize)
        # 保存先
        image.save("./python/YOLO/capture.png")
    else:
        print("error!!")

# 大体の距離を計算
def calcDistance(width):
    # 0:近距離 1:中距離 2:遠距離
    if width > 0.1:
        distance = 0
    elif width > 0.05:
        distance = 1
    else:
        distance = 2 
    
    return distance

# 大体の位置計算
def calcPosition(posVal):
    if posVal < 0.4:
        position = 0
    elif posVal < 0.6:
        position = 1
    else:
        position = 2

    return position

# 結果の出力用
# txt初期化
def initTxt():
        f = open('t_zombie.txt', 'w', encoding='UTF-8')
        f.write("1")
        f.close()
        f = open('t_creeper.txt', 'w', encoding='UTF-8')
        f.write("2")
        f.close()

# txt書き込み
def writeTxt(line, type):
    if type == 1:
        txtName = "t_zombie.txt"
    else:
        txtName = "t_creeper.txt"

    f = open(txtName, 'a', encoding='UTF-8')
    f.write(line)
    f.close()

def main():
    # txt初期化
    initTxt()

    # Minecraftのウィンドウ取得
    winHundle = win32gui.FindWindow(None, "Minecraft: Education Edition")

    # Minecraftのウィンドウサイズを取得
    windowSize = win32gui.GetWindowRect(winHundle)

    # スクショ➡検出のループ
    while True:
        #スクショ
        captureMC(winHundle, windowSize)

        # 検出
        result = detect.run()
        initTxt()
        mobData = []
        for j in range(len(result)):
            mobData.append(mob())
            mobData[j].setData(result=result[j])
            mobData[j].outputDataAbout()

if __name__ == '__main__':
    main()