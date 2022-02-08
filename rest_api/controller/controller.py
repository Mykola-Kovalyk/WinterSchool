from main import app

@app.route('/')
def index():
    return "YAHOO"

@app.route('/get/<id>')
def get_fish(id):
    print(id)
    return "what a horrible smell... code smell!"

@app.route('/get', methods=['GET'])
def get_all_fishes():
    return "not some of them - all of them!"

@app.route('/create', methods=['POST'])
def create_fish():
    print("hello fish")
    return "and the legendary fish was born!"