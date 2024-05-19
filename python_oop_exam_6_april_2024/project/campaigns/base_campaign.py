from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    UNIC_REQUIRED_ENGAGEMENTS = []

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if value < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")

        self.__campaign_id = value

    @property
    def required_engagement(self):
        return self.__required_engagement

    @required_engagement.setter
    def required_engagement(self, value):
        if value in self.UNIC_REQUIRED_ENGAGEMENTS:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")

        self.__required_engagement = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass
