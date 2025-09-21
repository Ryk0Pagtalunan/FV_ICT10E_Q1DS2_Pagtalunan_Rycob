from pyscript import display, document

def Message(e):
    nameofp = (document.getElementById("namep").value)
    ageofp = (document.getElementById("agep").value)
    schoolofp = (document.getElementById("schoolp").value)
    msg = f"""Student Profile\n
    Name:\t{nameofp}
    \n
    Age:\t{ageofp}
    \n
    School:\t{schoolofp}
    \n
    Notes:\n
    {nameofp} is currently {ageofp} years old, studying at {schoolofp}."""

    display(msg, target="msgappear", append=False)