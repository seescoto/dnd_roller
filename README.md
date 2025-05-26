# dnd_roller

A simple flask app that allows users to set their D&D stats and proficiencies and then roll using those stats.

## Getting started

1. Clone the repository to your local machine.

```sh
git clone https://github.com/seescoto/dnd_roller.git
```

2. Install the required packages.

```sh
pip install -r requirements.txt
```

3. Create a file config.py with a secret key for saving session data in between rolls.

```sh
secret_key = "YOUR_SECRET_KEY"
```

4. Navigate to the folder that holds this repository and run the app

```sh
flask --app app run
```

5. Follow the instructions in the terminal that leads you to opening 127.0.0.1:5000 in your favorite browser

6. Explore and enjoy!

7. To exit out of the app when you're done, type in control + C into the command line and the app will close on its own.

```sh
^C