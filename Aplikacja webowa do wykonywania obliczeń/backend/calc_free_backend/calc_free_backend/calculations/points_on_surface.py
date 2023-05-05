import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('SVG')
import io
import base64

def find_distance_between_points(first_point, second_point, matplotlib_lock):
    response = {}
    result = ((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2) ** 0.5
    response["solution"] ="d = " + str(result).replace(".", ",")
    hint = "Odległość pomiędzy punktami można wyliczyć z twierdzenia Pitagorasa.\n" + \
    "Jest on równa długości przeciwprostokątnej trójkąta, którego przyprostokątne\n" + \
    "mają długość równą wartości bezwzględnej z różnicy współrzędnych x oraz y punktów.\n" + \
    "Wzór: d = ((x1 - x2)^2 + (y1 - y2)^2)^(1 / 2)\nWynik: d = ((" + \
        str(first_point[0]).replace(".", ",") + " - " + str(second_point[0]).replace(".", ",") + ")**2 + (" + \
            str(first_point[1]).replace(".", ",") + " - " + \
                str(second_point[1]).replace(".", ",") + ")**2)^(1 / 2) = " + str(result).replace(".", ",") 
    response["hint"] = hint
    matplotlib_lock.acquire()
    plt.plot([first_point[0], second_point[0]], [first_point[1], second_point[1]], color='#d64550')
    plt.title("Rysunek")
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')  
    plt.locator_params(nbins=12)
    plt.grid(True)
    plt.scatter(first_point[0], first_point[1], color='#d64550')
    plt.scatter(second_point[0], second_point[1], color='#d64550')
    x_half = (first_point[0] + second_point[0])/2.0
    y_half = (first_point[1] + second_point[1])/2.0
    round_result = round(result, 5)
    if first_point[1] >= second_point[1]:
        plt.annotate("  d = " + str(round_result).replace(".", ","),(x_half, y_half), fontsize = 11, verticalalignment='bottom')
    else:
        plt.annotate("  d = " + str(round_result).replace(".", ","),(x_half, y_half), fontsize = 11, verticalalignment='top')
    fig = plt.gcf()
    img_data = io.BytesIO()
    fig.savefig(img_data, format = 'png')
    plt.clf()
    matplotlib_lock.release()
    img_data.seek(0)
    image_bytes = base64.b64encode(img_data.read())
    response["graph"] = image_bytes.decode("raw-unicode-escape")
    return json.dumps(response)