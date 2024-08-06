1. Написать REST сервис для работы с командами инженеров. Нужно использовать чистую архитектуру (описаны entity, usecase, принципы SOLID и тп). Сервис должен быть заточен под деплой в k8s (Dockerfile + хэлсчеки) Сервис должен позволять:
  1. Создавать команду
  2. Изменять состав команды
  3. Удалять команду


# Team Service
## Описание

Team Service — это приложение, предназначенное для управления командами и членами команд. Оно построено на
основе [Flask](https://flask.palletsprojects.com/) и развернуто с использованием Kubernetes и Minikube для
контейнеризации и оркестрации.

## Установка

### Локальная установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваш-репозиторий/team_service.git
    cd team_service
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # На Windows используйте: .venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите приложение:

    ```bash
    python app.py
    ```

### Развертывание в Minikube

1. Убедитесь, что Minikube и kubectl установлены и настроены. Запустите Minikube:

    ```bash
    minikube start --driver=docker
    ```

2. Загрузите образ Docker в Minikube:

    ```bash
    minikube image load team-service:latest
    ```

3. Примените манифесты Kubernetes:

    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

4. Проверьте состояние Pod и Service:

    ```bash
    kubectl get pods
    kubectl get services
    ```

5. Для доступа к приложению через браузер используйте URL:

    ```bash
    minikube service team-service
    ```

## Развертывание

Для развертывания в Kubernetes, убедитесь, что у вас есть необходимые манифесты в папке k8s/.

Используйте команду

```bash
  kubectl apply
 ```

для применения манифестов и развертывания приложения.