CREATE TABLE team(
       team_id int,
       team_city varchar(30),
       team_name varchar(30),
       stadium_name varchar(30),
       primary key(team_id)
);
CREATE TABLE player(
       player_id int,
       name varchar(30),
       position varchar(20),
       team_id int,
       primary key(player_id),
       foreign key(team_id) references team(team_id)
);
CREATE TABLE game(
       game_id int,
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
