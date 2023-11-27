import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError("Out dated vaccine")

            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Wear mask please dummy.")

        except KeyError:
            raise NotVaccinatedError("Visitor should be vaccinated.")

        else:
            return f"Welcome to {self.name}"