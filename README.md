Entities, Attributes, and Relations 

1. Player 

Attributes: person_id (PK), first_name, last_name, birthdate, height, weight, position, team_id (FK), from_year, to_year, draft_year, draft_round, draft_number 

Relations: 

Player - Team: 

Cardinality: Many to One 

Participation: Total for Player, Partial for Team 

Player - Draft Combine Stats: 

Cardinality: One to One 

Participation: Partial for Player, Total for Draft Combine Stats 

Player - Game (via Performance): 

Cardinality: Many to Many 

Participation: Total for Player, Total for Game 

Player - Draft History: 

Cardinality: One to One 

Participation: Partial for Player, Total for Draft 

2. Team 

Attributes: team_id (PK), team_name, team_abbreviation, team_city 

Relations: 

Team - Game (Home and Away): 

Cardinality: Many to Many 

Participation: Total for Team, Total for Game 

Team - Player: 

Cardinality: One to Many 

Participation: Partial for Team, Total for Player 

Team - Draft History: 

Cardinality: One to Many 

Participation: Partial for Team, Total for Draft 

3. Game 

Attributes: game_id (PK), season_id, game_date, team_id_home (FK), team_id_away (FK) 

Relations: 

Game - Team (Home and Away): 

Cardinality: Many to Many 

Participation: Total for Game, Total for Team 

Game - Official: 

Cardinality: Many to Many 

Participation: Total for Game, Partial for Official 

Game - Player (via Performance): 

Cardinality: Many to Many 

Participation: Total for Game, Total for Player 

Game - Inactive Players: 

Cardinality: Many to Many 

Participation: Partial for Game, Partial for Player 

4. Draft Combine Stats 

Attributes: player_id (FK), season, height_wo_shoes, weight, wingspan, vertical_leap 

Relations: 

Draft Combine Stats - Player: 

Cardinality: One to One 

Participation: Total for Draft Combine Stats, Partial for Player 

5. Draft History 

Attributes: person_id (FK), team_id (FK), season, round_number, round_pick, overall_pick 

Relations: 

Draft History - Player: 

Cardinality: One to One 

Participation: Total for Draft History, Partial for Player 

Draft History - Team: 

Cardinality: Many to One 

Participation: Total for Draft History, Partial for Team 

6. Official 

Attributes: official_id (PK), first_name, last_name 

Relations: 

Official - Game: 

Cardinality: Many to Many 

Participation: Partial for Official, Total for Game 

Inactive Players - Season: 

Cardinality: Many to One 

Participation: Partial for Inactive Players, Total for Season Inactive player status is determined within the context of specific games and, by extension, seasons. 

7. Inactive Players 

Attributes: game_id (FK), player_id (FK), jersey_num 

Relations: 

Inactive Players - Game: 

Cardinality: Many to Many 

Participation: Partial for Inactive Players, Partial for Game 

8. Season 

Attributes: season_id (PK), season_year 

Relations: 

Season - Game: 

Cardinality: One to Many 

Participation: Total for Season, Total for Game 

Season - Draft History: 

Cardinality: One to Many 

Participation: Total for Season, Total for Draft History 

Season - Player (Seasonal Alignment): 

Cardinality: Many to Many 

Participation: Partial for Season, Partial for Player 

Season - Team Performance: 

Cardinality: One to Many 

Participation: Partial for Season, Partial for Team 

Season - Official Engagement: 

Cardinality: One to Many 

Participation: Partial for Season, Partial for Official 

