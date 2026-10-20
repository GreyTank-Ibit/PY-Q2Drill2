from pyscript import document,display

def add_member(e):
    document.getElementById('output1').innerHTML = " "

    grade7 = {'Johnathan Joestar', 'Silver Chariot', 'Gyro Zeppeli', 'Dio Brando'}
    grade8 = {'Optimus Prime', 'Bumblebee', 'Megatron', 'Starscream'}
    grade9 = {'Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Geoffrey Monmouth'}
    grade10 = {'Spider-Man', 'Mary Jane', 'Norman Osborn', 'Flash Thompson'}
    grade11 = {'Atasha Sampan', 'Pio Oquendo', 'Cameron Bufford', 'Hans William Smith Arada'}

    first_name = document.getElementById('input1').value
    last_name = document.getElementById('input2').value

    new_member_set = {f'{first_name} {last_name}'}

    all_members = grade7 | grade8 | grade9 | grade10 | grade11 | new_member_set

    total_members = len(all_members)

    member_list = "<br>".join(sorted(all_members))

    # displays the full list of members and the total number of members
    document.getElementById('output1').innerHTML = f'All members:<br>{member_list}<br><br>Total members: {total_members}'