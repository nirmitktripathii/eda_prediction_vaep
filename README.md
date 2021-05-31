# EDA_Prediction_VAEP

Explanatory Data Analysis, Preparation of shot maps, pass networks and Predictive model for top leagues in European football along with preparation of VAEP model scoring and player ranking with GUI implementation. 

# Project Summary
In the era of big data and artificial intelligence, many different domains such as healthcare, finance, banking, retail, travel, social media and many more. Sports analytics is one such branch which has been attracting increasing interest due to availability advanced sensing technologies which make the data available. One such effort is being made in this project, where along with EDA, we are trying to develop a predictive model to predict the outcome of games as well as final points table with the use of expected goals parameter. 
EDA is aimed at studying the football dataset, to analyse, extract information from it and make important conclusions based on the data. The main goal is to find the different styles of plays in different teams, finding weaknesses and strengths of the teams and assess the ways of measurement and improvement of the team performance. We got the most effective events and capitalised on their characteristics in order to achieve the set goal. For EDA we are working on Kaggle Football events dataset which contains the off-the -ball type events data (don’t include passing shots and location) of 4 years (season 2012-13 to season 2016-17) for 5 leagues (Laliga, Premier League, Bundesliga, League One, Serie A) as well as match events data made available for public access by Statsbomb and Wyscout.
For predictions we have used multiple output regressor with different regressors such as Random forest regressor (RF), Support Vector Regressor (SVR). In the points table, the main ranks to be predicted are top positions (vary as per league) and bottom 3 positions which is selected as accuracy measure. The prediction of season for 2019-20 season, top prediction accuracy is found to be 67 % whereas 33% for bottom positions.
Along with this, understanding attacking style of play of different teams using the shot maps, and of players using pass maps is also done. Shot maps of all Barcelona matches in the latest 19/20 season were created and analyzed. Similarly, Lionel Messi’s pass maps in the same matches were created and were used to extract inference on his style of play, positional preference and influence on the game. Along with that passing clusters were also created for Barcelona for the same set of matches to deeply understand the style of play. 
Also along with this we have created a GUI wherein we display the goal plots in which all the previous actions leading to a goal are displayed and top 10 players, of each league, according to VAEP rankings are also displayed.


For more information read the Project report document file.


































