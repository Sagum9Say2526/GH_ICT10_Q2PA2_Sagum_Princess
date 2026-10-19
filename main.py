from pyscript import display, document

def add_member(e):
    sector_one = {''}
    sector_two = {''}
    sector_three = {''}
    sector_four = {''}
    first_name = document.getElementById("first").value
    surname = document.getElementById("surname").value
    added_member = str(first_name) + str(" ") + str(surname)
    members = {'Alex Bueno', 'Eliana De La Cruz', 'Helena Magsino', 'Frances Torculas', 'Gudz Gudz', 'Lord Starscream'}
    members.add(added_member)
    display(f'{members}', target='results', append=False)
    display(f'the total number of members: {len(members)}', target='results')