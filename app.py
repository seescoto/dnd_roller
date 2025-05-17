from flask import Flask, request, render_template

# run with 'flask --app FILENAME run'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set-stats', methods=['POST'])
def set_stats():
    return render_template('set_stats.html')


if __name__ == '__main__':
    app.run()
