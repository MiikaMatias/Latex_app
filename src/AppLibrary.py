from stub_io import StubIO
from repositories.reference_repository import ReferenceRepository
from services.reference_services import ReferenceService
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._reference_repository = ReferenceRepository()
        self._reference_service = ReferenceService(self._reference_repository)

        self._app = App(
            self._reference_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_reference(self, type, fields):
        self._reference_service.create_user(type, fields)
