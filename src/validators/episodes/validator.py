from fastapi import HTTPException


class ValidatorEpisode:
    @staticmethod
    def validate_not_episode(episode):
        if episode is None:
            raise HTTPException(status_code=404, detail="Episode not found.")
