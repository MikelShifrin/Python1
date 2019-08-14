from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

#The 2 lines above do the exact same thing

def main():
    line_graph()
    bar_chart()
    pie_chart()

#Line Graph
def line_graph():
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 2, 3, 4, 5]

    plt.plot(x, y, marker='o')
    plt.title('Linear Graph')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(True)
    plt.show()

#Bar Chart
def bar_chart():
    left_edge = [0, 5, 10, 15, 20]
    height = [10, 20, 30, 40, 50]
    bar_width = 5
    plt.bar(left_edge, height, bar_width, color=('r', 'g', 'b', 'm', 'k'))
    plt.show()

#Pie Chart
def pie_chart():
    values = [10, 50, 40]
    plt.pie(values)
    plt.show()
    
main()
