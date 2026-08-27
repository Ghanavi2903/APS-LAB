from data import generate_linear_data
from visualize import plot_2d_data

def main():
    x,y=generate_linear_data()
    plot_2d_data(x,y,title="linearly seperable data")

if __name__ == "__main__":
    main()