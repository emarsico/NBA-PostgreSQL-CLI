# setup_tables.py

import psycopg2

def setup_tables(conn):
    """
    Sets up all necessary tables in the database.
    """
    tables = [
        """
        CREATE TABLE IF NOT EXISTS PLAYER (
            person_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            birthdate DATE,
            height INTEGER,
            weight INTEGER,
            position VARCHAR(50),
            from_year INTEGER,
            to_year INTEGER,
            draft_year INTEGER,
            draft_number INTEGER,
            draft_round INTEGER
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Draft_History (
            draft_id SERIAL PRIMARY KEY,
            round_number INTEGER,
            round_pick INTEGER,
            overall_pick INTEGER,
            season INTEGER,
            person_id INTEGER REFERENCES PLAYER(person_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Draft_Combine_Stats (
            combine_id SERIAL PRIMARY KEY,
            height_wo_shoes FLOAT,
            weight INTEGER,
            wingspan FLOAT,
            vertical_leap FLOAT,
            season INTEGER,
            person_id INTEGER REFERENCES PLAYER(person_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Season (
            season_id SERIAL PRIMARY KEY,
            season_year INTEGER
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Game (
            season_id SERIAL PRIMARY KEY,
            season_year INTEGER
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Team (
            team_id SERIAL PRIMARY KEY,
            team_name VARCHAR(255),
            team_abbreviation VARCHAR(10),
            team_city VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Official (
            official_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Inactive_Players (
            inactive_id SERIAL PRIMARY KEY,
            jersey_num INTEGER,
            person_id INTEGER REFERENCES PLAYER(person_id),
            game_id INTEGER -- This should reference a Game table, which seems to be missing. Ensure to create Game table as well.
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Officiates (
            official_id INT NOT NULL,
            game_id INT NOT NULL,
            PRIMARY KEY (official_id, game_id),
            FOREIGN KEY (official_id) REFERENCES Official(official_id),
            FOREIGN KEY (game_id) REFERENCES Game(game_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Player_In_Season (
            person_id INT NOT NULL,
            season_id INT NOT NULL,
            PRIMARY KEY (person_id, season_id),
            FOREIGN KEY (person_id) REFERENCES PLAYER(person_id),
            FOREIGN KEY (season_id) REFERENCES Season(season_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Player_In_Game (
            person_id INT NOT NULL,
            game_id INT NOT NULL,
            PRIMARY KEY (person_id, game_id),
            FOREIGN KEY (person_id) REFERENCES PLAYER(person_id),
            FOREIGN KEY (game_id) REFERENCES Game(game_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Inactive_Player_In_Game (
            inactive_id INT NOT NULL,
            game_id INT NOT NULL,
            PRIMARY KEY (inactive_id, game_id),
            FOREIGN KEY (inactive_id) REFERENCES Inactive_Players(inactive_id),
            FOREIGN KEY (game_id) REFERENCES Game(game_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Team_In_Game (
            team_id INT NOT NULL,
            game_id INT NOT NULL,
            PRIMARY KEY (team_id, game_id),
            FOREIGN KEY (team_id) REFERENCES Team(team_id),
            FOREIGN KEY (game_id) REFERENCES Game(game_id)
        );
        """
    ]
    cur = conn.cursor()
    try:
        for table in tables:
            cur.execute(table)
        conn.commit()
        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred while setting up tables: {e}")
        conn.rollback()
    finally:
        cur.close()