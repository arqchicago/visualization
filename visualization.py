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
        self.fig, self.ax = plt.subplots()

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

    def line_chart(self, fig_name):
        mpl.style.use('seaborn')

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
          
        self.ax.plot(df['x'], df['y'], color='b', label='test')
        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        self.ax.set_ylabel(self.text_y_label)
        self.ax.legend()
        plt.savefig(fig_name)
        plt.close()

        
if __name__ == "__main__":
    df = pd.read_csv('data/test.csv')
    line_chart1 = visualization()
    line_chart1.plot_title = 'Plot of Y vs X'
    line_chart1.y_label = 'Y'
    line_chart1.x_label = 'X'
    #line_chart1.watermark = 'do not distribute'
    line_chart1.line_chart('fig1.png')