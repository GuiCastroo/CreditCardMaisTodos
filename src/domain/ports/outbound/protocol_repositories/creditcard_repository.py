from abc import ABCMeta

from src.domain.ports.outbound.protocol_repositories.repositories import IGetRepository, ICreateRepository


class ICreditCardRepository(IGetRepository, ICreateRepository, metaclass=ABCMeta):
    """Implementation CreditCardRepository"""
