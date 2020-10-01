import matplotlib.pyplot as plt


def graphic_last_month(last_month, type_graphic):
    plt.plot(last_month, color='red')
    plt.title(f'{type_graphic} Price Variation')
    plt.ylabel('Price')
    plt.xlabel('Amount of Prices')
    plt.xlim(left=0)
    plt.show()
