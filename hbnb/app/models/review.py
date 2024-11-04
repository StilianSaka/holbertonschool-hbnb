from datetime import datetime
import uuid

class Review:
    def __init__(self, text, rating, place_id, user_id):
        if text is None or rating is None or place_id is None or user_id is None:
            raise ValueError("Required attributes not specified!")

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.text = text
        self.rating = rating
        self.place_id = place_id  # relationship - id of Place that the Review is for
        self.user_id = user_id  # relationship - id of User who wrote the Review

    # --- Getters and Setters ---
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Invalid value specified for rating")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        from app.services.facade import HBnBFacade
        facade = HBnBFacade()
        user_exists = facade.get_user(value)
        if user_exists:
            self._user_id = value
        else:
            raise ValueError("User does not exist!")

    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        from app.services.facade import HBnBFacade
        facade = HBnBFacade()
        place_exists = facade.get_place(value)
        if place_exists:
            self._place_id = value
        else:
            raise ValueError("Place does not exist!")

    # --- Methods ---
    def save(self):
        self.updated_at = datetime.now()

    def update(self, data):
        """ Update Review attributes from a dictionary """
        from app.services.facade import HBnBFacade
        facade = HBnBFacade()
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
        facade.update_review(self.id, data)

    def delete(self):
        """ Method to delete the review from repository """
        from app.services.facade import HBnBFacade
        facade = HBnBFacade()
        facade.delete_review(self.id)

    def validate_rating(self):
        """ Validate the rating attribute """
        if not (1 <= self.rating <= 5):
            raise ValueError("Invalid value specified for rating")

    def to_dict(self):
        """ Convert Review object to dictionary """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def review_exists(review_id):
        pass  # Unused - the facade method get_review will handle this
