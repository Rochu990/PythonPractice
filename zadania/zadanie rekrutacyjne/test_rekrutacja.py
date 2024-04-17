from zadanie_rekrutacyjne import solution, first_sunday

def test_s():
    expenses = {
        "2023-01": {
            "01": {
                "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
                "fuel": [ 210.22 ]
            },
            "09": {
                "food": [ 11.9 ],
                "fuel": [ 190.22 ]
            }
        },
        "2023-03": {
            "07": {
                "food": [ 20, 11.9, 30.20, 11.9 ]
            },
            "04": {
                "food": [ 10.20, 11.50, 2.5 ],
                "fuel": []
            }
        },
        "2023-04": {}
    }
    result = solution(expenses)
    assert result == 11.72

def test_empty_expenses():
    assert solution({}) == None

def test_empty_days():
    expenses = {"2023-01": {}}
    assert solution(expenses) == None

def test_empty_day():
    expenses = {"2023-01": {
        "01": {}
        }
    }
    assert solution(expenses) == None   

def test_empty_values():
    expenses = {"2023-01": {
        "01": {
            "food": [],
            "fuel": []

        }
        }
    }
    assert solution(expenses) == None

def test_max_day():
    assert first_sunday("2023-01") == 1
    assert first_sunday("2023-02") == 5
    assert first_sunday("2023-03") == 5
    assert first_sunday("2023-04") == 2
    assert first_sunday("2023-05") == 7
    assert first_sunday("2023-06") == 4
    assert first_sunday("2023-07") == 2
    assert first_sunday("2023-08") == 6
    assert first_sunday("2023-09") == 3
    assert first_sunday("2023-10") == 1
    assert first_sunday("2023-11") == 5
    assert first_sunday("2023-12") == 3

def test():
    expenses = {
        "2023-05": {
            "01": {
                "food": [ 1, 2, 3, 4, 5],
                "fuel": [ 6 ]
            },
            "02": {
                "food": [ 2, 3 ],
                "fuel": [ 5, 7 ]
            },
            "03": {
                "food": [ 2, 3 ],
            },
            "04": {
                "food": [ 2, 3 ],
                "fuel": []
            },
            "05": {
                "tibia_account_premium": [41],
                "fuel": [ 5 ]
            },
            "06": {
                "drugs": [],
                "fuel": [ 5, 7 ],
                "cos": [ 5, 7 ]
            },
            "07": {
                "food": [ 123 ],
                "fuel": [ 5, 7 ]
            },
            "08": {
                "food": [  ],
                "fuel": [ 5, 7 ]
            }
        },
    }
    assert solution(expenses) == 5


def test_test():
    expenses = {
        "2023-05": {
            "01": {
                "food": [ "1, 2, 3, 4, 5"],
                "fuel": [ 6 ]
            },    
        }
    }
    assert solution(expenses) == 6




