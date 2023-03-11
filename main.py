# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from easy import *
import os
from PIL import Image, ImageEnhance
class ImageProcessor():
    def __init__(self, image = None, filename = None, folder = None):
        self.image = image
        self.filename = filename
        self.folder = folder
    def loadImage(self, filename):
        self.filename = filename
        file_path = os.path.join(workdir, filename)
        self.image = Image.open(file_path)
    def showImage(self, path):
        win.img_lbl.hide()
        pixmap = QPixmap(path)
        w,h = win.img_lbl.width(), win.img_lbl.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        win.img_lbl.setPixmap(pixmap)
        win.img_lbl.show()
    def do_baw(self):
        if win.listOfImage.currentItem():
            self.image = self.image.convert('L')
            self.saveImage()
            path = os.path.join(workdir, self.folder, self.filename)
            self.showImage(path)
    def do_rotateL(self):
        if win.listOfImage.currentItem():
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            path = os.path.join(workdir, self.folder, self.filename)
            self.showImage(path)
    def do_rotateR(self):
        if win.listOfImage.currentItem():
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            path = os.path.join(workdir, self.folder, self.filename)
            self.showImage(path)
    def do_mirror(self):
        if win.listOfImage.currentItem():
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            path = os.path.join(workdir, self.folder, self.filename)
            self.showImage(path)
    def do_sharp(self):
        if win.listOfImage.currentItem():
            self.image = ImageEnhance.Contrast(self.image).enhance(1.5)
            self.saveImage()
            path = os.path.join(workdir, self.folder, self.filename)
            self.showImage(path)
    def saveImage(self):
        save_path = os.path.join(workdir, self.folder)
        if not (os.path.exists(save_path) or os.path.isdir(save_path)):
            os.mkdir(save_path)
        img_path = os.path.join(save_path, self.filename)
        self.image.save(img_path)


def filter_pict(filenames, extentions):
    result = []
    for i in extentions:
        for f in filenames:
            if f.lower().endswith(i):
                result.append(f)
    return result

def open_folder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = os.listdir(workdir)
    win.listOfImage.clear()
    win.listOfImage.addItems(filter_pict(filenames, extentions))
    pixmap = QPixmap()
    win.img_lbl.setPixmap(pixmap)

def showChosenImage():
    if win.listOfImage.currentItem():
        filename = win.listOfImage.currentItem().text()
        imageProc.loadImage(filename)
        file_path = os.path.join(workdir, filename)
        imageProc.showImage(file_path)

extentions = ['.jpg', '.png', '.bmp', '.jfif']
workdir = ""
imageProc = ImageProcessor(folder="ModifiedImage")

app = QApplication([])
win = Window()
win.setupUi(win)
win.show()
win.folder_btn.clicked.connect(open_folder)
win.listOfImage.currentRowChanged.connect(showChosenImage)
win.baw_btn.clicked.connect(imageProc.do_baw)
win.left_btn.clicked.connect(imageProc.do_rotateL)
win.right_btn.clicked.connect(imageProc.do_rotateR)
win.mirror_btn.clicked.connect(imageProc.do_mirror)
win.sharp_btn.clicked.connect(imageProc.do_sharp)
win.resized.connect(showChosenImage)
app.exec_()