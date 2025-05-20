from flask import Flask, request, render_template
from src.Character import Character

# run with 'flask --app FILENAME run'
app = Flask(__name__)


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
    new_char = Character()
    new_char.set_attributes(int(strength), int(dex),
                            int(con), int(intelligence), int(wis), int(cha))
    new_char.set_proficiency_bonus(int(request.form.get('proficiency_bonus')))
    new_char.set_initiative_bonus(int(request.form.get('initiative_bonus')))

    # record if proficient in given skills
    profs = {}
    profs['Acrobatics'] = request.form.get('acrobatics')
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

    new_char.set_proficiencies(profs)

    all_skills = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
                  'Deception', 'History', 'Insight', 'Intimidation',
                  'Investigation', 'Medicine', 'Nature', 'Perception',
                  'Performance', 'Persuasion', 'Religion', 'Sleight of Hand',
                  'Stealth', 'Survival',
                  'Strength', 'Dexterity', 'Constitution', 'Intelligence',
                  'Wisdom', 'Charisma']

    saving_throws = ['Strength', 'Dexterity',
                     'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

    return render_template('set_stats.html', character=new_char, skills=all_skills, saving_throws=saving_throws)


if __name__ == '__main__':
    app.run()
