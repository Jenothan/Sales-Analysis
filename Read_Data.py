from abc import ABC, abstractmethod

class ReadData(ABC):
    """Abstract class for data analysis."""

    @abstractmethod
    def analysis(self, data):
        """Abstract method for analysis."""
        pass

        