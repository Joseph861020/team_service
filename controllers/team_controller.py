from flask import Blueprint, request, jsonify
from flask.typing import ResponseReturnValue
from repositories.team_repository import TeamRepository
from usecases.team_usecase import TeamUseCase

team_blueprint = Blueprint('team_blueprint', __name__)

# Инициализация UseCase
team_usecase = TeamUseCase(TeamRepository())


@team_blueprint.route('/teams', methods=['POST'])
def create_team() -> ResponseReturnValue:
    """
    Создает новую команду.

    Возвращает:
        ResponseReturnValue: Информация о созданной команде в формате JSON.
    """
    data = request.get_json()
    team = team_usecase.create_team(data['name'], data['members'])
    return jsonify(team.__dict__), 201


@team_blueprint.route('/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id: int) -> ResponseReturnValue:
    """
    Обновляет информацию о команде.

    Аргументы:
        team_id (int): ID команды.

    Возвращает:
        ResponseReturnValue: Обновленная информация о команде или ошибка, если команда не найдена.
    """
    data = request.get_json()
    team = team_usecase.update_team(team_id, data['name'], data['members'])
    if team:
        return jsonify(team.__dict__), 200
    return jsonify({'error': 'Team not found'}), 404


@team_blueprint.route('/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id: int) -> ResponseReturnValue:
    """
    Удаляет команду.

    Аргументы:
        team_id (int): ID команды.

    Возвращает:
        ResponseReturnValue: Пустой ответ или ошибка, если команда не найдена.
    """
    result = team_usecase.delete_team(team_id)
    if result:
        return '', 204
    return jsonify
