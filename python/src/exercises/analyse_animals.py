from bar_chart import draw_bar_chart

def load_data(file_name):
    """ Load the data into a dict. """
    result = {}
    try:
        with open(file_name, mode='r') as f: 
            lines = f.readlines()
            for line in lines:
                parts = line.split(",")
                animal,sightings = parts[0],int(parts[1])
                if animal in result:
                    result[animal] += sightings
                else:
                    result[animal] = sightings
            return result
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)

def visualise(data):
    """ Visualise the data using a bar chart. """
    colours = ['#DAA520','#B5C7EB','#FA5053']
    draw_bar_chart(data, ('Animals', 'Sightings'), colours=colours)                

if __name__ == '__main__':
    data = load_data('animals.csv')
    visualise(data)