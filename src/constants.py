ALL_COLUMNS = ['Nr.', 'Name', 'Geboren', 'Aufnahme', 'Gestorben', 'Fachsektion', 'Bild', 'Datenbank', 'Beiname']

RENAME_COLUMNS = {
    "Sektion": "Fachsektion",
    "Nr.\xa01": "Nr.",
    "Nr.*": "Nr.",
    "Aufnahme\xa01": "Aufnahme",
    "Beiname\xa01": "Beiname",
}

IRRELEVANT_COLUMNS = ['Beiname', 'Bild', 'Datenbank']

SHOULD_BE_NOTEMPTY_COLS = ['Geboren', 'Gestorben', 'Fachsektion']