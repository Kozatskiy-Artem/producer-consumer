from dependency_injector import containers, providers

from producer_consumer.repositories import Repository
from producer_consumer.services import Service


class RepositoryContainer(containers.DeclarativeContainer):
    """
    A container responsible for providing instances of various repository classes.
    Repositories are data access components used by services to retrieve data.
    """

    repository = providers.Factory(Repository)


class ServiceContainer(containers.DeclarativeContainer):
    """
    A container responsible for providing instances of various service classes.
    Services are responsible for interaction with the data storage layer and business logic of the application.
    """

    service = providers.Factory(Service, repository=RepositoryContainer.repository)
