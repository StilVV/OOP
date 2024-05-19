from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * PremiumInfluencer.INITIAL_PAYMENT

    def reached_followers(self, campaign_type: str):
        result = 0
        if campaign_type == "HighBudgetCampaign":
            result = int((self.followers * self.engagement_rate) * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            result = int((self.followers * self.engagement_rate) * 0.8)

        return result

