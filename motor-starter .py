



import json
import sys

def run_engine(rules, data):
    results = {}

    for player in data["players"]:
        score = 0

        for rule in rules:
            if rule["type"] == "lowest_wins":
                # Golf: lägst poäng vinner
                if player["score"] == min(p["score"] for p in data["players"]):
                    score += rule["points"]

            elif rule["type"] == "highest_wins":
                # Bowling: högst poäng vinner
                player_score = sum(player["frames"])
                if player_score == max(sum(p["frames"]) for p in data["players"]):
                    score += rule["points"]

            elif rule["type"] == "strike_bonus":
                score += player["frames"].count(10) * rule["points"]

            elif rule["type"] == "apm_bonus":
                if player["apm"] > rule["threshold"]:
                    score += rule["points"]
            elif rule["type"] == "win_bonus":
                if player["outcome"] == "win":
                    score += rule["points"]

        results[player["name"]] = score

    return results

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        match = json.load(f)

    result = run_engine(match["rules"], match)
    print(json.dumps(result, indent=2, ensure_ascii=False))



