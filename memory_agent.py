import json

memory = {}

def save_insight(symbol, insight):
    memory[symbol] = insight
    save_to_file()

def get_insight(symbol):
    return memory.get(symbol, "No prior insight available.")

def save_to_file():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

def load_from_file():
    global memory
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
    except FileNotFoundError:
        memory = {}
