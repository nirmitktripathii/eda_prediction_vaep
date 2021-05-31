from tkinter import *
import tkinter as tk
import pandas as pd
import csv
from tkinter import ttk
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename
from Automated_Goal_plots import id_return,nice_time,data_generation,plotting
'====================================================================================================='
# Function for checking team names
def check_name(team_name):
    diff_teams = {'Deportivo Alaves':'Deportivo Alav\u00e9s','Atletico Madrid':'Atl\u00e9tico Madrid','Leganes':'Legan\u00e9s',
                  'Deportivo La Coruna':'Deportivo La Coru\u00f1a', "Malaga":'M\u00e1laga','Bayern Munich':'Bayern M\u00fcnchen',
                  'Koln':'K\u00f6ln','Saint-Etienne':'Saint-\u00c9tienne'}

    if team_name in diff_teams:
        return diff_teams[team_name]
    else:
        return team_name
'====================================================================================================='
# Function for loading the data
def import_csv_data(display,league_chosen):
    vaep_path = {"Serie A":"VAEP_score_Serie_A.csv",
                 "La Liga":"VAEP_score_La_Liga.csv",
                 "Premier League":"VAEP_score_Premier_League.csv    ",
                 "Ligue 1":"VAEP_score_Ligue_1.csv",
                 "Bundes Liga":"VAEP_score_Bundesliga.csv"
                    }
    csv_file_path = vaep_path[league_chosen]
    with open(csv_file_path) as file:
       reader = csv.reader(file)

       # r and c tell us where to grid the labels
       r = 0
       for col in reader:
          c = 0
          for row in col:
             # i've added some styling
             label = tk.Label(display, width = 15, height = 2,
                                   text = row, relief = tk.GROOVE)
             label.grid(row = r, column = c)
             c += 1
          r += 1
'====================================================================================================='
# Loading team data
teams = pd.read_csv('teams.csv',header=0,index_col=None)
team_names = [list(teams.Serie_A.values),list(teams.Premier_League.values),list(teams.La_Liga.values),
                list(teams.Bundes_Liga.values),list(teams.Ligue_1.values)]
'====================================================================================================='
# Required functions
def get_names():
    global league,home_team,away_team,disp
    chosen_league = league.get()
    chosen_display_method = disp.get()
    chosen_home_team = check_name(home_team.get())
    chosen_away_team = check_name(away_team.get())


    if chosen_home_team != None and chosen_away_team != None and chosen_display_method=='VAEP Ranking':
        mb.showinfo('Combination Mismatch !!!',"VAEP ranking of players need only selection of league.")

    if chosen_display_method == 'Goal Plots':
        actions,goal,games = data_generation(chosen_home_team,chosen_away_team,chosen_league)
        fig = plt.figure()
        if len(goal.index) == 0:
            mb.showinfo('No Goals Warning !!!',"No goals were scored in the selected match !!. Please try another match.")
            plt.close('all')
        elif len(goal.index) < 5:
            for i in range(goal.shape[0]):
                ax = fig.add_subplot(goal.shape[0],1,i+1)
                plotting(goal,actions,games,i,ax)
                plt.subplots_adjust(left=0.28,right=0.625,bottom=0.11)
        else:
            for i in range(goal.shape[0]):
                ax = fig.add_subplot(5,2,i+1)
                plotting(goal,actions,games,i,ax)
                plt.subplots_adjust(left=0,bottom=0,right=0.75,top=0.88,wspace=1,hspace=0.057)
        plt.show()
    elif chosen_display_method == 'VAEP Ranking':
        display = tk.Tk()
        display.title('TOP 10 Players with highest VAEP values')
        display.geometry('500x500')
        # b1 = Button(display, command=display.destroy(), text='Close')
        # b1.place(x = 200, y= 400)
        import_csv_data(display,chosen_league)


    # window.destroy()
'====================================================================================================='
# Creating tkinter window
window = tk.Tk()
window.title('Football Project')
window.geometry('500x500')
'====================================================================================================='
# Labels
# label text for title
ttk.Label(window, text = "Football Project",
          background = 'grey', foreground ="white",
          font = ("Times New Roman", 20)).grid(row = 15, column = 1)

#label text for season information
ttk.Label(window, text = "Season 2017-18",
          background = 'grey', foreground ="white",
          font = ("Times New Roman", 15)).grid(row = 20, column = 1)


# label for selecting the league
ttk.Label(window, text = "Select the League :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 25, padx = 20, pady = 25)

# label for selecting the home team
ttk.Label(window, text = "Select the Home Team :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 30, padx = 5, pady = 25)

# label for selecting the away team
ttk.Label(window, text = "Select the Away Team :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 35, padx = 5, pady = 25)

# label for selecting the display
ttk.Label(window, text = "Select the display option :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 40, padx = 5, pady = 25)

'====================================================================================================='
# Preparation for optionmenu
leagues = ['Serie A','Premier League','La Liga','Bundes Liga','Ligue 1']
league = StringVar(window)
league.set(leagues[0])

league_menu = OptionMenu(window,league,*leagues)
league_menu.grid(column = 1, row = 25)
'====================================================================================================='
# Combobox creation for dropdown of Home Team Selection
home_team = tk.StringVar(window)
home_teamchosen = ttk.Combobox(window, width = 27, textvariable = home_team,state='readonly')

def home_callback(eventObject):
    abc = eventObject.widget.get()
    league_selected = league.get()
    index=leagues.index(league_selected)
    home_teamchosen.config(values=team_names[index])

# Adding combobox drop down list
home_teamchosen.grid(column = 1, row = 30)
home_teamchosen.bind('<Button-1>',home_callback)
'====================================================================================================='
# Combobox creation for dropdown of Away Team Selection
away_team = tk.StringVar(window)
away_teamchosen = ttk.Combobox(window, width = 27, textvariable = away_team,state='readonly')

def away_callback(eventObject):
    abc = eventObject.widget.get()
    league_selected = league.get()
    index=leagues.index(league_selected)
    away_teamchosen.config(values=team_names[index])

# Adding combobox drop down list
away_teamchosen.grid(column = 1, row = 35)
away_teamchosen.bind('<Button-1>',away_callback)
'====================================================================================================='
# Combobox creation for dropdown of display
disp = tk.StringVar()
dispchosen = ttk.Combobox(window, width = 27, textvariable = disp)

# Adding combobox drop down list
dispchosen['values'] = ('Goal Plots','VAEP Ranking')

dispchosen.grid(column = 1, row = 40)
dispchosen.current(0)
'====================================================================================================='
b1 = Button(window, command=get_names, text='Plot/Display')
b1.place(x = 200, y= 400)
window.mainloop()
