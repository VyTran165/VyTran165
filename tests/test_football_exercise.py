# Test constructor of class GameScorer
import pytest
import football_exercise

def test_game_scorer_init():
    gs = football_exercise.GameScorer('t1', 't2', 3, 2)
    assert gs.name_team_1 == 't1'
    assert gs.name_team_2 == 't2'
    assert gs.score_team_1 == 3
    assert gs.score_team_2 == 2


@pytest.mark.parametrize('fs, points_t1, points_t2', [
    (football_exercise.FootballScorer(3, 't1', 't2', 0, 0), 1, 1),
    (football_exercise.FootballScorer(4, 't1', 't2', 5, 0), 3, 0),
    (football_exercise.FootballScorer(5, 't1', 't2', 1, 2), 0, 3)
])
def test_calculate_points(fs, points_t1, points_t2):
    fs.calculate_points()
    assert fs.points_team_1 == points_t1
    assert fs.points_team_2 == points_t2


# Test constructor of class TeamFootballSeason

def test_team_football_season_init():
    tfs = football_exercise.TeamFootballSeason(2, 't1', ['t2', 't3'], [1, 2], [2, 1])
    assert tfs.n_games == 2
    assert tfs.games[0].name_team_1 == 't1'
    assert tfs.games[0].name_team_2 == 't2'
    assert tfs.games[0].score_team_1 == 1
    assert tfs.games[0].score_team_2 == 2
    assert tfs.games[1].name_team_1 == 't1'
    assert tfs.games[1].name_team_2 == 't3'
    assert tfs.games[1].score_team_1 == 2
    assert tfs.games[1].score_team_2 == 1


# Test method add_game of class TeamFootballSeason

def test_team_football_season_add_game():
    tfs = football_exercise.TeamFootballSeason(2, 't1', ['t2', 't3'], [1, 2], [2, 1])
    tfs.add_game('t4', 1, 1)
    assert tfs.n_games == 3
    assert tfs.games[2].name_team_1 == 't1'
    assert tfs.games[2].name_team_2 == 't4'
    assert tfs.games[2].score_team_1 == 1
    assert tfs.games[2].score_team_2 == 1

def test_name_football_season_add_football_scorer():
    tfs = football_exercise.TeamFootballSeason(2, 't1', ['t2', 't3'], [1, 2], [2, 1])
    tfs.add_game('t4', 1, 1)
    fs = football_exercise.FootballScorer(3, 't1', 't4', 1, 1)
    tfs.add_football_scorer(fs)
    assert tfs.n_games == 3
    assert tfs.games[2].name_team_1 == 't4'
