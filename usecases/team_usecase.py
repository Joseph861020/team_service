from typing import List, Optional
from entities.team import Team
from repositories.team_repository import TeamRepository


class TeamUseCase:
    """
    UseCase для работы с командами инженеров.
    """

    def __init__(self, team_repository: TeamRepository) -> None:
        self.team_repository = team_repository

    def create_team(self, name: str, members: List[str]) -> Team:
        """
        Создает новую команду.
        """
        new_team = Team(None, name, members)
        return self.team_repository.create(new_team)

    def update_team(self, team_id: int, name: str, members: List[str]) -> Optional[Team]:
        """
        Обновляет информацию о команде.
        """
        team = self.team_repository.get_by_id(team_id)
        if team:
            team.name = name
            team.members = members
            return self.team_repository.update(team)
        return None

    def delete_team(self, team_id: int) -> bool:
        """
        Удаляет команду.
        """
        return self.team_repository.delete(team_id)
