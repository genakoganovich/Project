from log_plotter import LogPlotter

def main():
    plotter = LogPlotter(log_filename='app.log')
    plotter.read_log()
    plotter.plot()

if __name__ == '__main__':
    main()
