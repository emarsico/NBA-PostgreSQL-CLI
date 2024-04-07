import datetime

def log_query(query):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Queries.log", "a") as log_file:
        log_file.write(f"{timestamp}: {query}\n")
