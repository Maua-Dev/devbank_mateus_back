
from enum import Enum
import os

from src.app.repo.account_repository_interface import IAccountRepository
from src.app.repo.transaction_history_repository_interface import ITransactionHistoryRepository
from src.app.repo.transaction_repository_interface import ITransactionRepository

from src.app.repo.account_repository_interface import IAccountRepository
from src.app.repo.transaction_history_repository_interface import ITransactionHistoryRepository
from src.app.repo.transaction_repository_interface import ITransactionRepository

from src.app.errors.environment_errors import EnvironmentNotFound


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]
        
    @staticmethod
    def get_transaction_repo() -> ITransactionRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transaction_repository_mock import TransactionRepositoryMock
            return TransactionRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_history_repo() -> ITransactionHistoryRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transaction_history_repository_mock import TransactionHistoryRepositoryMock
            return TransactionHistoryRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_account_repo() -> IAccountRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.account_repository_mock import AccountRepositoryMock
            return AccountRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
        

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__