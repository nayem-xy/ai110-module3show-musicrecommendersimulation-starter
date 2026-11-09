import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            }

            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a weighted similarity score and explain each matching feature."""
    score = 0.0
    reasons = []

    # Genre: maximum 2 points
    if user_prefs["favorite_genre"].lower() == song["genre"].lower():
        score += 2.0
        reasons.append("Genre match (+2.00)")

    # Mood: maximum 1 point
    if user_prefs["favorite_mood"].lower() == song["mood"].lower():
        score += 1.0
        reasons.append("Mood match (+1.00)")

    # Energy: maximum 1.5 points
    energy_points = max(
        0, 1 - abs(user_prefs["target_energy"] - song["energy"])
    ) * 1.5
    score += energy_points
    if energy_points > 0:
        reasons.append(f"Energy similarity (+{energy_points:.2f})")

    # Tempo: maximum 1.5 points
    tempo_points = max(
        0, 1 - abs(user_prefs["target_tempo"] - song["tempo_bpm"]) / 120
    ) * 1.5
    score += tempo_points
    if tempo_points > 0:
        reasons.append(f"Tempo similarity (+{tempo_points:.2f})")

    # Valence: maximum 1 point
    valence_points = max(
        0, 1 - abs(user_prefs["target_valence"] - song["valence"])
    )
    score += valence_points
    if valence_points > 0:
        reasons.append(f"Valence similarity (+{valence_points:.2f})")

    # Danceability: maximum 1 point
    dance_points = max(
        0, 1 - abs(user_prefs["target_danceability"] - song["danceability"])
    )
    score += dance_points
    if dance_points > 0:
        reasons.append(f"Danceability similarity (+{dance_points:.2f})")

    # Acousticness: maximum 1 point
    acoustic_points = max(
        0, 1 - abs(user_prefs["target_acousticness"] - song["acousticness"])
    )
    score += acoustic_points
    if acoustic_points > 0:
        reasons.append(f"Acousticness similarity (+{acoustic_points:.2f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    # Sort by score from highest to lowest
    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return scored_songs[:k]

    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
