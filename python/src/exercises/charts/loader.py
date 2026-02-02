from bar_chart import draw_bar_chart_horizontal, draw_bar_chart

data = {}
with open('movie-genres.csv') as file:
    header = file.readline().strip()
    print(header)
    [x_label, y_label] = header.split(',')
    print(f"{x_label},{y_label}" )
    for line in file.readlines():
        [genre, popularity] = line.strip().split(',')
        data[genre] = int(popularity)
    colours = ['teal', 'gold', 'skyblue', 'pink', 'lightgreen', 'red']
    draw_bar_chart_horizontal(data, (x_label, y_label), colours)
    