from flask import Flask, jsonify
from flask.typing import ResponseReturnValue
from controllers.team_controller import team_blueprint

app = Flask(__name__)

# Регистрация блюпринтов
app.register_blueprint(team_blueprint)


@app.route('/health', methods=['GET'])
def health_check() -> ResponseReturnValue:
    """
    Проверка состояния сервиса.

    Возвращает:
        ResponseReturnValue: Ответ с JSON, содержащим статус здоровья сервиса.
    """
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
