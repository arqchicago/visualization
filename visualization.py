import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


class visualization:
    def __init__(self):
        self.text_watermark = ''
        self.text_plot_title = ''
        self.text_y_label = ''
        self.text_x_label = ''
        
    @property
    def y_label(self):
        return self.text_y_label
        
    @y_label.setter
    def y_label(self, text):
        self.text_y_label = text
        
    @property
    def x_label(self):
        return self.text_x_label
        
    @x_label.setter
    def x_label(self, text):
        self.text_x_label = text
        
    @property
    def plot_title(self):
        return self.text_plot_title
        
    @plot_title.setter
    def plot_title(self, text):
        self.text_plot_title = text
        
    @property
    def watermark(self):
        return self.text_watermark
        
    @watermark.setter
    def watermark(self, text):
        self.text_watermark = text

    def plot(self, fig_name):
        mpl.style.use('seaborn')
        plt.plot(df['x'], df['y'], color='b', label='test')
        plt.title(self.text_plot_title)
        subtitle = 'this is the subtitle'
        plt.suptitle(subtitle, fontsize=10)
        plt.ylabel(self.text_y_label)
        plt.xlabel(self.text_x_label)
        plt.gca().set_xlim(left=0)
        plt.gca().set_ylim(bottom=0)
        #plt.text(10, 20, self.text_watermark, font=40, color='red', ha='right', va='bottom', alpha=0.25, rotation=40)
        plt.legend()
        plt.savefig(fig_name)
        plt.close()
        
        
if __name__ == "__main__":
    df = pd.read_csv('data/test.csv')
    plot1 = visualization()
    plot1.plot_title = 'Plot of Y vs X'
    plot1.y_label = 'Y'
    plot1.x_label = 'X'
    plot1.watermark = 'do not distribute'
    plot1.plot('fig1.png')