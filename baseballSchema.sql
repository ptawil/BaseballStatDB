CREATE TABLE team(
       team_id int auto_increment,
       team_city varchar(30),
       team_name varchar(30),
       stadium_name varchar(30),
       primary key(team_id)
);
CREATE TABLE player(
       player_id int auto_increment,
       name varchar(30),
       position varchar(20),
       team_id int,
       primary key(player_id),
       foreign key(team_id) references team(team_id)
);
CREATE TABLE game(
       game_id int auto_increment,
       game_date date,
       home_team_id int,
       away_team_id int,
       primary key(game_id),
       foreign key(home_team_id) references team(team_id),
       foreign key(away_team_id) references team(team_id),
       check (NOT (home_team_id = away_team_id))
);
CREATE TABLE player_game_stats(
       player_id int,
       game_id int,
       num_of_at_bats int,
       num_of_hits int,
       num_of_runs int,
       num_of_homeruns int,
       primary key(player_id, game_id),
       foreign key(player_id) references player(player_id),
       foreign key(game_id) references game(game_id),
       check (num_of_hits <= num_of_at_bats)
);
LOAD DATA LOCAL INFILE 'teams.txt' into table team;
LOAD DATA LOCAL INFILE 'players.txt' into table player;

/*My database satisfies first normal form, since there is only one possible value for each attribute in every table. It also satisfies second normal form, since there are no partial dependencies- every non-prime attribute of every table depends on a candidate key and not just a subset of it; every attribute in the player table depends on player_id, every attribute of team depends on team_id, every attribute in game depends on game_id, and every attribute of player_game_stats depends on the a particular player_id couple with a particular game_id. My tables also satisfy third normal form because there are no transitive functional dependencies- every attribute is dependent on the primary key and not on a different attribute in the table so redundancy is limited. That's why team and player are two separate tables; they could have been merged into one table and the information about the team such as stadium name would be part of the player relation, but then that information would be repeated because there are many players that are on the same team and there's no reason for the information which is related to the team and not directly related to the player to be repeated. Therefore, team is separated into its own table and player contains a foreign key which references the team table to link the two tables together. In addition, game information is separated into two tables; game and player_game_stats because which teams participated in the game and on what day the game was played is not dependent on how a specific player played in the game and that information does not need to be repeated for every player. That's why there is a game_id which links the game table which has more general information about the game to the player_game_stats table which has stats related to specific players in each game. I believe that my database is also in BCNF because there are no functional dependencies in any table that are not determined by super keys. */
