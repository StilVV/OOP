from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        try:
            influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        if influencer.username in [i.username for i in self.influencers]:
            return f"{username} is already registered."

        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        try:
            campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        except KeyError:
            return f"{campaign_type} is not a valid campaign type."

        if campaign.campaign_id in [c.campaign_id for c in self.campaigns]:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility:
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0.0:
            payment = influencer.calculate_payment(campaign)
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' has successfully participated in"
                    f" the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_followers = {}
        for campaign in self.campaigns:
            total = sum(
                influencer.reached_followers(type(campaign).__name__) for influencer in campaign.approved_influencers)
            if total:
                total_followers[campaign] = total
        return total_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((influencer for influencer in self.influencers if influencer.username == username), None)
        if not influencer:
            return f"{username} has not participated in any campaigns."
        else:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        return "\n".join([f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
                          f"Total budget: ${campaign.budget:.2f}, Total reached followers: {self.calculate_total_reached_followers()[campaign]}"
                          for campaign in sorted_campaigns])
