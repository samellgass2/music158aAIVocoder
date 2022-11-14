SELFTRANSITIONPROB = 0.3
FORWARDTRANSITIONPROB = 0.6
RETROGRESSIONPROB = 1 - SELFTRANSITIONPROB - FORWARDTRANSITIONPROB

function_probabilities = {
    "tonic" : {
        "tonic" : SELFTRANSITIONPROB,
        "predominant" : FORWARDTRANSITIONPROB,
        "dominant" : 0
    },
    "predominant" : {
        "tonic" : RETROGRESSIONPROB,
        "predominant" : SELFTRANSITIONPROB,
        "dominant" : FORWARDTRANSITIONPROB
    },
    "dominant" : {
        "tonic" : FORWARDTRANSITIONPROB,
        "predominant" : RETROGRESSIONPROB,
        "dominant" : SELFTRANSITIONPROB
    }
}

chord_probabilities = {
    "tonic" : {
        "I" : 0.4,
        "vi" : 0.4,
        "iii" : 0.2
    },
    "predominant" : {
        "ii" : 0.5,
        "IV" : 0.5
    },
    "dominant" : {
        "V" : 0.6,
        "V7" : 0.3,
        "vii" : 0.1
    }
}

note_to_scale = [0, 2, 4, 5, 7, 9, 11, 12]



chords_in_semitones = {
    "I" : [0, 4, 7],
    "ii": [2, 5, 9],
    "iii": [4, 7, 11],
    "IV": [5, 9, 0],
    "V": [7, 11, 2],
    "V7": [7, 11, 2, 5],
    "vi": [9, 0, 4],
    "vii": [11, 2, 5]
}

chord_to_function = {
    "I" : "tonic",
    "ii" : "predominant",
    "iii" : "tonic",
    "IV" : "predominant",
    "V" : "dominant",
    "V7" : "dominant",
    "vi" : "tonic",
    "vii" : "dominant"
}

min_to_majNote = {
    0 : 0,
    2 : 2,
    4 : 3,
    5 : 5,
    7 : 7,
    9 : 8,
    11 : 11
}

min_to_majChord = {
    "I" : "i",
    "ii" : "iio",
    "iii" : "III",
    "IV" : "iv",
    "V" : "V",
    "V7" : "V7",
    "vi" : "VI",
    "vii" : "VII"
}

maj_to_minChord = {
    "i" : "I",
    "iio" : "ii",
    "III" : "iii",
    "iv" : "IV",
    "V" : "V",
    "V7" : "V7",
    "VI" : "vi",
    "VII" : "vii"
}

chord_from_note_and_function = {
    (0, "tonic") : {
        "I" : 0.5,
        "iii" : 0.2,
        "vi" : 0.3
    },
    (0, "predominant") : {
        "I" : 0.1,
        "IV" : 0.6,
        "vi" : 0.3
    },
    (0, "dominant") : {
        "I" : 0.5,
        "vi" : 0.5
    },
    (2, "tonic"): {
        "ii" : 0.7,
        "V" : 0.3
    },
    (2, "predominant") : {
        "ii" : 0.4,
        "V" : 0.4,
        "V7" : 0.2
    },
    (2, "dominant") : {
        "V" : 0.4,
        "vii" : 0.3,
        "V7" : 0.3
    },
    (4, "tonic") : {
        "I" : 0.4,
        "vi" : 0.4,
        "iii" : 0.2
    },
    (4, "predominant") : {
        "ii" : 0.5,
        "IV" : 0.5
    },
    (4, "dominant"): {
        "I" : 0.5,
        "vi" : 0.5
    },
    (5, "tonic") : {
        "ii" : 0.4,
        "IV" : 0.5,
        "V7" : 0.1
    },
    (5, "predominant") : {
        "ii" : 0.4,
        "IV" : 0.4,
        "V7" : 0.2
    },
    (5, "dominant") : {
        "V7" : 0.9,
        "IV" : 0.1
    },
    (7, "tonic") : {
        "I" : 0.5,
        "V" : 0.4,
        "iii" : 0.1
    },
    (7, "predominant") : {
        "V" : 0.4,
        "V7" : 0.4,
        "vii" : 0.2
    },
    (7, "dominant") : {
        "V" : 0.4,
        "V7" : 0.4,
        "I" : 0.2
    },
    (9, "tonic") : {
        "vi" : 0.4,
        "ii" : 0.3,
        "IV" : 0.3
    },
    (9, "predominant") : {
        "ii" : 0.5,
        "IV" : 0.5
    },
    (9, "dominant") : {
        "vi" : 0.9,
        "iii" : 0.1
    },
    (11, "tonic") : {
        "V" : 0.6,
        "iii" : 0.4
    },
    (11, "predominant") : {
        "V" : 0.5,
        "V7": 0.3,
        "vii": 0.2
    },
    (11, "dominant") : {
        "V" : 0.4,
        "V7" : 0.4,
        "vii" : 0.2
    }
}
