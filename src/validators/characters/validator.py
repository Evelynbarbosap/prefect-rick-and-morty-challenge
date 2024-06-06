from fastapi import HTTPException


class ValidatorCharacter:
    @staticmethod
    def validate_not_character(character):
        if character is None:
            raise HTTPException(status_code=404, detail="Character not found.")
