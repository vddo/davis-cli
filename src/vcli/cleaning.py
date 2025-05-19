from abc import ABC, abstractmethod


class Cleaner(ABC):
    """Interface for raw data set cleaner"""

    @abstractmethod
    def clean(self):
        """Processes the cleaning"""
        pass


class FootballCleaner(Cleaner):
    """Designed to clean the data set 1 consisting of football related data"""

    def clean(self):
        """Cleans the football data set

        1. If more than 2 field positions are given it will assign the last position to 'Best Position'
            and collects the remaining values into 'Positions Played'
        2.
        """
