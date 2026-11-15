
import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


# ============================================================
# 1. DATA MODELS
# ============================================================

@dataclass
class Song:
    """Represents a song and its attributes."""

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

    # Advanced attributes
    popularity: int = 50
    release_decade: int = 2020
    mood_tags: Optional[List[str]] = None
    language: str = "English"
    instrumentalness: float = 0.0


@dataclass
class UserProfile:
    """Represents a user's music preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

    # Optional preferences
    target_tempo: Optional[float] = None
    target_valence: Optional[float] = None
    target_danceability: Optional[float] = None
    target_acousticness: Optional[float] = None
    target_popularity: Optional[int] = None
    preferred_decade: Optional[int] = None
    preferred_mood_tags: Optional[List[str]] = None
    preferred_language: Optional[str] = None
    target_instrumentalness: Optional[float] = None


# ============================================================
# 2. SCORING STRATEGY BASE CLASS
# ============================================================

class ScoringStrategy:
    """
    Base class for recommendation scoring strategies.

    Every concrete strategy must implement score().
    """

    weights = {
        "genre": 1.0,
        "mood": 1.0,
        "energy": 3.0,
        "tempo": 1.5,
        "valence": 1.0,
        "danceability": 1.0,
        "acousticness": 1.0
    }

    def score(self, user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
        """Calculate a song's score using this strategy."""

        score = 0.0
        reasons = []

        # Genre similarity
        if user_prefs["favorite_genre"].lower() == song["genre"].lower():
            points = self.weights["genre"]
            score += points
            reasons.append(f"Genre match (+{points:.2f})")

        # Mood similarity
        if user_prefs["favorite_mood"].lower() == song["mood"].lower():
            points = self.weights["mood"]
            score += points
            reasons.append(f"Mood match (+{points:.2f})")

        # Energy similarity
        energy_similarity = max(
            0, 1 - abs(user_prefs["target_energy"] - song["energy"])
        )
        energy_points = energy_similarity * self.weights["energy"]
        score += energy_points

        if energy_points > 0:
            reasons.append(f"Energy similarity (+{energy_points:.2f})")

        # Tempo similarity
        if user_prefs.get("target_tempo") is not None:
            tempo_similarity = max(
                0,
                1 - abs(user_prefs["target_tempo"] - song["tempo_bpm"]) / 120
            )
            tempo_points = tempo_similarity * self.weights["tempo"]
            score += tempo_points

            if tempo_points > 0:
                reasons.append(f"Tempo similarity (+{tempo_points:.2f})")

        # Valence similarity
        if user_prefs.get("target_valence") is not None:
            similarity = max(
                0, 1 - abs(user_prefs["target_valence"] - song["valence"])
            )
            points = similarity * self.weights["valence"]
            score += points

            if points > 0:
                reasons.append(f"Valence similarity (+{points:.2f})")

        # Danceability similarity
        if user_prefs.get("target_danceability") is not None:
            similarity = max(
                0,
                1 - abs(
                    user_prefs["target_danceability"] - song["danceability"]
                )
            )
            points = similarity * self.weights["danceability"]
            score += points

            if points > 0:
                reasons.append(f"Danceability similarity (+{points:.2f})")

        # Acousticness similarity
        if user_prefs.get("target_acousticness") is not None:
            similarity = max(
                0,
                1 - abs(
                    user_prefs["target_acousticness"] - song["acousticness"]
                )
            )
            points = similarity * self.weights["acousticness"]
            score += points

            if points > 0:
                reasons.append(f"Acousticness similarity (+{points:.2f})")

        # Advanced attributes
        if user_prefs.get("target_popularity") is not None:
            points = max(
                0,
                1 - abs(
                    user_prefs["target_popularity"] - song["popularity"]
                ) / 100
            ) * 0.5

            score += points
            reasons.append(f"Popularity similarity (+{points:.2f})")

        if user_prefs.get("preferred_decade") is not None:
            if user_prefs["preferred_decade"] == song["release_decade"]:
                score += 0.5
                reasons.append("Release decade match (+0.50)")

        if user_prefs.get("preferred_mood_tags"):
            preferred_tags = {
                tag.lower() for tag in user_prefs["preferred_mood_tags"]
            }
            song_tags = set(song.get("mood_tags") or [])

            matching_tags = preferred_tags.intersection(song_tags)

            points = len(matching_tags) / len(preferred_tags)
            score += points

            if matching_tags:
                reasons.append(
                    f"Mood tag matches: {', '.join(sorted(matching_tags))} "
                    f"(+{points:.2f})"
                )

        if user_prefs.get("preferred_language") is not None:
            if (
                user_prefs["preferred_language"].lower()
                == song["language"].lower()
            ):
                score += 0.5
                reasons.append("Language match (+0.50)")

        if user_prefs.get("target_instrumentalness") is not None:
            points = max(
                0,
                1 - abs(
                    user_prefs["target_instrumentalness"]
                    - song["instrumentalness"]
                )
            ) * 0.5

            score += points
            reasons.append(
                f"Instrumentalness similarity (+{points:.2f})"
            )

        return round(score, 2), reasons


# ============================================================
# 3. CONCRETE SCORING STRATEGIES
# ============================================================

class BalancedStrategy(ScoringStrategy):
    """Uses the original balanced scoring weights."""

    weights = {
        "genre": 1.0,
        "mood": 1.0,
        "energy": 3.0,
        "tempo": 1.5,
        "valence": 1.0,
        "danceability": 1.0,
        "acousticness": 1.0
    }


class GenreFirstStrategy(ScoringStrategy):
    """Gives genre matches the highest priority."""

    weights = {
        "genre": 4.0,
        "mood": 1.0,
        "energy": 1.0,
        "tempo": 0.5,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5
    }


class MoodFirstStrategy(ScoringStrategy):
    """Gives mood matches the highest priority."""

    weights = {
        "genre": 1.0,
        "mood": 4.0,
        "energy": 1.0,
        "tempo": 0.5,
        "valence": 1.0,
        "danceability": 0.5,
        "acousticness": 0.5
    }


class EnergyFirstStrategy(ScoringStrategy):
    """Prioritizes energy and tempo similarity."""

    weights = {
        "genre": 0.5,
        "mood": 0.5,
        "energy": 4.0,
        "tempo": 3.0,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5
    }


# ============================================================
# 4. RECOMMENDER CLASS
# ============================================================

class Recommender:
    """
    Manages recommendations using a selectable scoring strategy.
    """

    def __init__(
        self,
        songs: List[Song],
        strategy: Optional[ScoringStrategy] = None
    ):
        self.songs = songs
        self.strategy = strategy or BalancedStrategy()

    def set_strategy(self, strategy: ScoringStrategy):
        """Change the recommendation strategy."""

        self.strategy = strategy

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs using the selected strategy."""

        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_tempo": user.target_tempo,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability,
            "target_acousticness": (
                user.target_acousticness
                if user.target_acousticness is not None
                else (1.0 if user.likes_acoustic else 0.0)
            ),
            "target_popularity": user.target_popularity,
            "preferred_decade": user.preferred_decade,
            "preferred_mood_tags": user.preferred_mood_tags,
            "preferred_language": user.preferred_language,
            "target_instrumentalness": user.target_instrumentalness
        }

        scored_songs = []

        for song in self.songs:
            song_data = song_to_dict(song)

            score, _ = self.strategy.score(user_prefs, song_data)

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song
    ) -> str:
        """Explain why a song was recommended."""

        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "target_tempo": user.target_tempo,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability,
            "target_acousticness": (
                user.target_acousticness
                if user.target_acousticness is not None
                else (1.0 if user.likes_acoustic else 0.0)
            ),
            "target_popularity": user.target_popularity,
            "preferred_decade": user.preferred_decade,
            "preferred_mood_tags": user.preferred_mood_tags,
            "preferred_language": user.preferred_language,
            "target_instrumentalness": user.target_instrumentalness
        }

        score, reasons = self.strategy.score(
            user_prefs,
            song_to_dict(song)
        )

        if not reasons:
            return f"{song.title} received a score of {score:.2f}."

        return (
            f"{song.title} received a score of {score:.2f} because "
            + ", ".join(reasons)
        )


# ============================================================
# 5. HELPER FUNCTIONS
# ============================================================

def song_to_dict(song: Song) -> Dict:
    """Convert a Song object into the dictionary format."""

    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
        "popularity": song.popularity,
        "release_decade": song.release_decade,
        "mood_tags": song.mood_tags or [],
        "language": song.language,
        "instrumentalness": song.instrumentalness
    }


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs and their attributes from a CSV file."""

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
                "acousticness": float(row["acousticness"]),
                "popularity": int(row.get("popularity") or 50),
                "release_decade": int(row.get("release_decade") or 2020),
                "mood_tags": [
                    tag.strip().lower()
                    for tag in (row.get("mood_tags") or "").split("|")
                    if tag.strip()
                ],
                "language": (row.get("language") or "English").strip(),
                "instrumentalness": float(
                    row.get("instrumentalness") or 0
                )
            }

            songs.append(song)

    return songs


# ============================================================
# 6. FUNCTION-BASED API (PRESERVES CHALLENGE 1)
# ============================================================

def score_song(
    user_prefs: Dict,
    song: Dict,
    strategy: Optional[ScoringStrategy] = None
) -> Tuple[float, List[str]]:
    """Score a song using the selected strategy."""

    selected_strategy = strategy or BalancedStrategy()

    return selected_strategy.score(user_prefs, song)


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    strategy: Optional[ScoringStrategy] = None
) -> List[Tuple[Dict, float, str]]:
    """Rank songs and return their scores and explanations."""

    selected_strategy = strategy or BalancedStrategy()

    scored_songs = []

    for song in songs:
        score, reasons = selected_strategy.score(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return scored_songs[:k]
