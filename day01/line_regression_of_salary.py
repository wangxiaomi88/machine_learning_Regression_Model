import numpy as np
import pandas as pd
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import cv2 as cv
import pickle


# 声明一个薪资预测类型，封装预测逻辑


class SalaryPredictionModel():
    def __init__(self):
        with open("model.pic", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, exps):
        """
        exps:工作年限数组（一维数组）
        """
        exps = np.array(exps).reshape(-1, 1)  # 可以把(n,)的一维数组变维：(4,1)的二维数组。-1表示自适应
        return self.model.predict(exps)

