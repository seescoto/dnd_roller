from flask import Flask, request, render_template, session
from src.Character import Character, character_to_dict, dict_to_character
from config import secret_key

# run with 'flask --app FILENAME run'
app = Flask(__name__)

app.secret_key = secret_key  # ability to save states w/ session


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set-stats', methods=['POST'])
def set_stats():

    # record character attributes + bonuses
    strength = request.form.get('strength')
    print(strength)
    dex = request.form.get('dexterity')
    con = request.form.get('constitution')
    intelligence = request.form.get('intelligence')
    wis = request.form.get('wisdom')
    cha = request.form.get('charisma')
    char = Character()
    char.set_attributes(int(strength), int(dex),
                        int(con), int(intelligence), int(wis), int(cha))
    char.set_proficiency_bonus(int(request.form.get('proficiency_bonus')))
    char.set_initiative_bonus(int(request.form.get('initiative_bonus')))

    # record if proficient in given skills
    profs = {}
    profs['Acrobatics'] = request.form.get('acrobatics')
    profs['Animal Handling'] = request.form.get('animal_handling')
    profs['Arcana'] = request.form.get('arcana')
    profs['Athletics'] = request.form.get('athletics')
    profs['Deception'] = request.form.get('deception')
    profs['History'] = request.form.get('history')
    profs['Insight'] = request.form.get('insight')
    profs['Intimidation'] = request.form.get('intimidation')
    profs['Investigation'] = request.form.get('investigation')
    profs['Medicine'] = request.form.get('medicine')
    profs['Nature'] = request.form.get('nature')
    profs['Perception'] = request.form.get('perception')
    profs['Performance'] = request.form.get('performance')
    profs['Persuasion'] = request.form.get('persuasion')
    profs['Religion'] = request.form.get('religion')
    profs['Sleight of Hand'] = request.form.get('sleight_of_hand')
    profs['Stealth'] = request.form.get('stealth')
    profs['Survival'] = request.form.get('survival')
    profs['Strength'] = request.form.get('strength_prof')
    profs['Dexterity'] = request.form.get('dexterity_prof')
    profs['Constitution'] = request.form.get('constitution_prof')
    profs['Intelligence'] = request.form.get('intelligence_prof')
    profs['Wisdom'] = request.form.get('wisdom_prof')
    profs['Charisma'] = request.form.get('charisma_prof')

    char.set_proficiencies(profs)

    # save stats and proficiencies for other pages
    session['stats'] = character_to_dict(char)
    session['proficiencies'] = char.proficiencies

    all_skills = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
                  'Deception', 'History', 'Insight', 'Intimidation',
                  'Investigation', 'Medicine', 'Nature', 'Perception',
                  'Performance', 'Persuasion', 'Religion', 'Sleight of Hand',
                  'Stealth', 'Survival',
                  'Strength', 'Dexterity', 'Constitution', 'Intelligence',
                  'Wisdom', 'Charisma']
    session['all_skills'] = all_skills

    saving_throws = ['Strength', 'Dexterity', 'Constitution',
                     'Intelligence', 'Wisdom', 'Charisma']
    session['saving_throws'] = saving_throws

    return render_template('set_stats.html', character=char, skills=all_skills, saving_throws=saving_throws, roll=None)


@app.route('/roll-skill', methods=['POST'])
def roll_skill():
    stats = session.get('stats')
    profs = session.get('proficiencies')

    # save character and load again
    char = dict_to_character(stats)
    for p in profs:
        char.add_proficiency(p)

    skill = request.form.get('skill')
    roll = char.roll_skill(skill)

    return render_template('set_stats.html', character=char, skills=session.get('all_skills'), saving_throws=session.get('saving_throws'), roll=roll)


@app.route('/roll-ability', methods=['POST'])
def roll_ability():
    stats = session.get('stats')
    profs = session.get('proficiencies')

    # save character and load again
    char = dict_to_character(stats)
    for p in profs:
        char.add_proficiency(p)

    ability = request.form.get('ability')
    roll = char.roll_skill(ability)

    return render_template('set_stats.html', character=char, skills=session.get('all_skills'), saving_throws=session.get('saving_throws'), roll=roll)


@app.route('/roll-initiative', methods=['POST'])
def roll_initiative():
    stats = session.get('stats')
    profs = session.get('proficiencies')

    # save character and load again
    char = dict_to_character(stats)
    for p in profs:
        char.add_proficiency(p)

    initiative = request.form.get('initiative')
    roll = char.roll_skill(initiative)

    return render_template('set_stats.html', character=char, skills=session.get('all_skills'), saving_throws=session.get('saving_throws'), roll=roll)


if __name__ == '__main__':
    app.run()
