import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from visualizer import arq_viz    
    
if __name__ == "__main__":
    df = pd.read_csv('data/test.csv')
    data_viz = arq_viz(df)
    data_viz.plot_title = 'Plot of Y vs X'
    data_viz.plot_suptitle = 'Figure Title'
    data_viz.y_label = 'Y'
    data_viz.x_label = 'X'
    data_viz.watermark = 'do not distribute'
    
    # create a boxplot of variable 'x'
    data_viz.boxplot('fig1.png', 'x')
    
    # create a line chart of variable 'y' vs 'x'
    data_viz.line_chart('fig2.png', 'x', 'y')
    
    # create a scatterplot of variable 'y' vs 'x'
    data_viz.scatter('fig3.png', 'x', 'y')