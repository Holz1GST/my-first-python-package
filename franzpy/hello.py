from emoji import emojize

def make_compliment(moderator = "Luuk"):
    """The make_compliment function.

    This function makes a compliment to the moderator of a seminar session. 

    Parameters
    ----------
    moderator : str
        The name of the moderator of the seminar session. Default is "Luuk".
    
    Returns
    -------
    opinion : str
        The compliment to the moderator of the seminar session.

    Examples
    --------
    >>> make_compliment("Luuk")
    
    """
    opinion = "This was a great idea for a seminar session, " + moderator + "-MVP!" + emojize(":star-struck:")
    print(opinion)

    return opinion