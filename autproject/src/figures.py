import matplotlib.pyplot as plt

def plot_trajectory_and_points(x_coords, y_coords, points_list):
    #x_coords_cm = [x * 100 for x in x_coords]  # Convert each element in x_coords from m to cm
    y_coords = [y *-1 for y in y_coords]  # Convert each element in y_coords from m to cm
    points_list= [[point[0],point[1], point[2] *-1] for point in points_list]  # Convert points from m to cm
    #print(x_coords, y_coords)

    # Plot trajectory (blue line)
    plt.plot(y_coords, x_coords, 'b-')


    # Plot points as red circles
    for point in points_list:
        plt.plot(point[2], point[1], 'o',label=point[0])  # 'ro' means red circles

    # Set labels and title
    plt.xlabel('y (m)')
    plt.ylabel('x (m)')
    plt.title('Trayectoria realizada y puntos encontrados')
    plt.grid()
    plt.xlim([-3,3])
    plt.ylim([-3,3])

    # Display legend
    plt.legend()
    
    # Display the plot
    plt.show()
