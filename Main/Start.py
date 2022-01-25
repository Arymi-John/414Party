import wx
import os


class MyFrame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, parent=None, size=(400, 300),pos=(600, 100), title='414Party')
        panel = wx.Panel(self)
        self.Start_button = wx.Button(panel, label='开始游戏', size=(150, 40), pos=(125, 150))
        self.Start_button.Bind(wx.EVT_BUTTON, self.Start)
        self.Start_button.SetBackgroundColour('red')
        imgpath = '../Images/首页.png'
        bmp = wx.Image(imgpath, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.Bmp = wx.StaticBitmap(panel, -1, bmp)

    def Start(self, event):
        if __name__ == '__main__':
            pass


if __name__ == '__main__':
    app= wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()