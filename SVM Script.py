from sklearn import svm
import pandas as pd
import numpy as np

# Link the Excel spreadsheet
filePath = r"C:\Users\gmari\Desktop\Coding\NHL Postseason Predictor\2021.xlsx"
project = pd.read_excel(filePath, None)

# Link, clean, and make library from the Team Statistics Spreadsheet
teamDataSheet = project["Team Statistics Table"]

teamDataSheet['Shots/G'] = teamDataSheet.apply(lambda x: x['Shot Data S'] / 56, axis = 1)

teamDataLibrary = {}

for i in range(1, 31):
    row = teamDataSheet.loc[i].to_numpy()
    teamDataLibrary[f"{row[1]}"] = teamDataSheet.loc[i, ['Per_game GF/G',
                                                         'Special Teams PP%',
                                                         'Special Teams PK%',
                                                         'Special Teams PIM/G',
                                                         'Shots/G',
                                                         'Shot Data S%',
                                                         'Shot Data SV%',
                                                         'Shot Data PDO',
                                                         'Corsi (5v5) CF%',
                                                         'Fenwick (5v5) FF%']].values.flatten().tolist()

# Link, clean, and make library from the Game Log Spreadsheets
playoffTeams = list(project.keys())
playoffTeams.pop(0)

teamGameLogs = {}
teamGameTargets = {}

for team in playoffTeams:

    teamLog = project[team]

    teamLog['Opp. PP%'] = teamLog.apply(lambda x: x['Opponent PPG'] / (x['Opponent PPO'] + 0.001), axis = 1)
    teamLog['Opp. PK%'] = teamLog.apply(lambda x: x['Team PPG'] / (x['Team PPO'] + 0.001 ), axis = 1)
    teamLog['Opp. CF%'] = teamLog.apply(lambda x: 100 - x['Advanced (at Even Strength) CF%'], axis = 1)
    teamLog['Opp. FF%'] = teamLog.apply(lambda x: 100 - x['Advanced (at Even Strength) FF%'], axis = 1)
    teamLog['Opp. S%'] = teamLog.apply(lambda x: x['GA'] * 100 / x['Opponent S'], axis = 1)
    teamLog['Opp. SV%'] = teamLog.apply(lambda x: 1 - x['GF']  / x['Team S'], axis = 1)
    teamLog['Opp. PDO'] = teamLog.apply(lambda x: 200 - x['Advanced (at Even Strength) PDO'], axis = 1)

    gameLog = []
    targetLog = []

    for i in range (0, 56):
        gameLog.append(teamLog.loc[i, ['GA',
                                       'Opp. PP%',
                                       'Opp. PK%',
                                       'Opponent PIM',
                                       'Opponent S',
                                       'Opp. S%',
                                       'Opp. SV%',
                                       'Opp. PDO',
                                       'Opp. CF%',
                                       'Opp. FF%']].values.flatten().tolist())
        targetLog.append(teamLog.iloc[i]['2'])

    teamGameLogs[f"{team}"] = gameLog
    teamGameTargets[f"{team}"] = targetLog

# Sci Kit Learn

clf = svm.SVC(kernel='rbf', C=0.5, gamma=15)
clf.fit(teamGameLogs['EDM'], teamGameTargets['EDM'])
prediction = clf.predict([teamDataLibrary['Tampa Bay Lightning']])

print(prediction)