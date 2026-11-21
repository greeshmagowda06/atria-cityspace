
def score_backlog(items):
    scored = []

    for item in items:
        effort = item["effort"]

        if effort <= 0:
            continue

        score = round(item["value"] / effort, 2)
        scored.append((item["id"], score))

    return sorted(scored, key=lambda x: (-x[1], x[0]))

def validate_user_story(story):
    if not isinstance(story, str) or not story.strip():
        return False

    if not story.startswith("As a "):
        return False

    if story.count(", I want ") != 1:
        return False

    if story.count(", so that ") != 1:
        return False

    role_part, goal_part = story.split(", I want ")

    if not role_part.startswith("As a "):
        return False

    goal, benefit = goal_part.split(", so that ")

    role = role_part[len("As a "):].strip()

    return bool(role and goal.strip() and benefit.strip())