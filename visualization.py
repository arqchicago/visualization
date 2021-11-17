import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


class visualization:
    def __init__(self, df):
        mpl.style.use('seaborn')
        self.df = df
        self.text_watermark = ''
        self.text_plot_title = ''
        self.text_plot_suptitle = ''
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
    def plot_suptitle(self):
        return self.text_plot_suptitle
        
    @plot_suptitle.setter
    def plot_suptitle(self, suptitle):
        self.text_plot_suptitle = suptitle
        
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
        self.fig, self.ax = plt.subplots()

        self.fig.suptitle(self.text_plot_suptitle, fontsize=16)

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
          
        self.ax.plot(self.df['x'], self.df['y'], color='b', label='test')
        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        self.ax.set_ylabel(self.text_y_label)
        self.ax.legend()
        self.fig.text(0.85, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        plt.savefig(fig_name)
        plt.close()

    def scatter(self, fig_name):
        self.fig, self.ax = plt.subplots()

        self.fig.suptitle(self.text_plot_suptitle, fontsize=16)

        for axis in ['bottom','left']:  #'top', 'right'
            self.ax.spines[axis].set_linewidth(2)
            self.ax.spines[axis].set_color('red')
          
        self.ax.scatter(self.df['x'], self.df['y'], color='b', label='test')
        self.ax.set(title=self.text_plot_title)
        self.ax.set_xlabel(self.text_x_label)
        self.ax.set_ylabel(self.text_y_label)
        self.ax.legend()
        self.fig.text(0.85, 0.15, self.text_watermark, fontsize=25, color='gray', ha='right', va='bottom', alpha=0.5)
        plt.savefig(fig_name)
        plt.close()

    def boxplot(self, fig_name, var):
        green_diamond = dict(markerfacecolor='g', marker='s')
        fig, ax = plt.subplots()
        ax.set_title('Boxplot - variable ' + var)
        boxplot = ax.boxplot(df[var], notch=True, flierprops=green_diamond, patch_artist=True, showmeans=True)
        plt.xticks([1], [var])
        for patch, color in zip(boxplot['boxes'], ['pink']):
            patch.set_facecolor(color)
            
        for median in boxplot['medians']: 
            median.set(color ='red', linewidth = 3) 
        
        
        plt.savefig(fig_name)
        plt.close()
    
    
    
if __name__ == "__main__":
    df = pd.read_csv('data/test.csv')
    data_viz = visualization(df)
    data_viz.plot_title = 'Plot of Y vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.y_label = 'Y'
    data_viz.x_label = 'X'
    data_viz.watermark = 'do not distribute'
    data_viz.line_chart('fig1.png')
    data_viz.scatter('fig2.png')
    data_viz.boxplot('fig3.png', 'x')