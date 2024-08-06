from typing import List, Optional
from entities.team import Team


class TeamRepository:
    """
    Репозиторий для работы с командами.
    """

    def __init__(self) -> None:
        self.teams: List[Team] = []

    def create(self, team: Team) -> Team:
        """
        Создает новую команду.
        """
        team.team_id = len(self.teams) + 1
        self.teams.append(team)
        return team

    def get_by_id(self, team_id: int) -> Optional[Team]:
        """
        Возвращает команду по ID.
        """
        for team in self.teams:
            if team.team_id == team_id:
                return team
        return None

    def update(self, team: Team) -> Optional[Team]:
        """
        Обновляет информацию о команде.
        """
        for i, t in enumerate(self.teams):
            if t.team_id == team.team_id:
                self.teams[i] = team
                return team
        return None

    def delete(self, team_id: int) -> bool:
        """
        Удаляет команду по ID.
        """
        for i, team in enumerate(self.teams):
            if team.team_id == team_id:
                del self.teams[i]
                return True
        return False
