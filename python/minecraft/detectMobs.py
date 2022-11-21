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
        #type 0:クリーパー, 1:ゾンビ　（嘘ついてるかも）
        self.type = 0
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

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)

    def calcDistance(self):
        # 0:近距離 1:中距離 2:遠距離
        if self.width > 0.1:
            self.distance = 0
        elif self.width > 0.05:
            self.distance = 1
        else:
            self.distance = 2

    # txtに書き込む
    def outputDataDetail(self):
        # txtに書き込む内容
        # txt = " {x:.03f} {y:.03f} {width:.03f} {height:.03f} {distance:1d}".format(x=self.x,y=self.y,width=self.width,height=self.height,distance=self.distance)
        txt = "{x:03.0f}{y:03.0f}{width:03.0f}{height:03.0f}{distance:03d}".format(x=self.x*1000,y=self.y*1000,width=self.width*1000,height=self.height*1000,distance=self.distance)

        writeTxt(txt, self.type)

    # def outputDataAbout(self):
    #     txt = "{x:.03f}{y:.03f}{width:.03f}{height:.03f}{distance:1d}".format(x=self.x,y=self.y,width=self.width,height=self.height,distance=self.distance)

    #def calcPosition(self):

# スクショ用関数
def captureMC(winHundle, windowSize):
    if winHundle:
        image = ImageGrab.grab(windowSize)
        # 保存先
        image.save("./python/YOLO/capture.png")
    else:
        print("error!!")

# 結果の出力用
# txt初期化
def initTxt():
        f = open('t_zombie.txt', 'w', encoding='UTF-8')
        f.write("0")
        f.close()
        f = open('t_creeper.txt', 'w', encoding='UTF-8')
        f.write("1")
        f.close()

# txt書き込み
def writeTxt(line, type):
    if type == 0:
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
        mobData = []
        for j in range(len(result)):
            mobData.append(mob())
            mobData[j].setData(result=result[j])
            mobData[j].calcDistance()
            mobData[j].outputDataDetail()

if __name__ == '__main__':
    main()