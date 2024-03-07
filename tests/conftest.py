from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch


class BaseConfTest(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.addClassCleanup(patch.stopall)

        super().setUpClass()


class BaseUseCaseConfTest(BaseConfTest):
    pass
