from typing import List


class Team:
    """
    Класс, представляющий команду инженеров.
    """

    def __init__(self, team_id: int, name: str, members: List[str]) -> None:
        self.team_id = team_id
        self.name = name
        self.members = members
