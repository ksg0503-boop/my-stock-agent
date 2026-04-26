import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	SerplyNewsSearchTool,
	BraveSearchTool
)






@CrewBase
class DailySwingTradingCommittee11SpecialistsCrew:
    """DailySwingTradingCommittee11Specialists crew"""

    
    @agent
    def senior_technical_market_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["senior_technical_market_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def fundamental_market_research_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["fundamental_market_research_analyst"],
            
            
            tools=[				SerplyNewsSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def geopolitical_risk_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["geopolitical_risk_analyst"],
            
            
            tools=[				BraveSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def senior_investment_committee_moderator(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["senior_investment_committee_moderator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def professional_chart_pattern_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["professional_chart_pattern_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def market_momentum_and_sentiment_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["market_momentum_and_sentiment_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def cryptocurrency_and_digital_assets_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["cryptocurrency_and_digital_assets_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def small_cap_growth_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["small_cap_growth_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def macro_sector_rotation_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["macro_sector_rotation_analyst"],
            
            
            tools=[				SerplyNewsSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def etf_strategy_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["etf_strategy_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def commodities_and_materials_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["commodities_and_materials_analyst"],
            
            
            tools=[				BraveSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def federal_reserve_and_monetary_policy_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["federal_reserve_and_monetary_policy_analyst"],
            
            
            tools=[				SerplyNewsSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def daily_technical_swing_trading_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["daily_technical_swing_trading_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def daily_fundamental_swing_catalyst_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["daily_fundamental_swing_catalyst_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def geopolitical_risk_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["geopolitical_risk_assessment"],
            markdown=False,
            
            
        )
    
    @task
    def chart_pattern_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["chart_pattern_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def momentum_and_sentiment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["momentum_and_sentiment_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def cryptocurrency_market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["cryptocurrency_market_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def small_cap_opportunity_discovery(self) -> Task:
        return Task(
            config=self.tasks_config["small_cap_opportunity_discovery"],
            markdown=False,
            
            
        )
    
    @task
    def macro_sector_flow_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["macro_sector_flow_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def etf_market_opportunity_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["etf_market_opportunity_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def commodity_and_materials_market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["commodity_and_materials_market_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def federal_reserve_policy_impact_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["federal_reserve_policy_impact_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def daily_investment_committee_consensus(self) -> Task:
        return Task(
            config=self.tasks_config["daily_investment_committee_consensus"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the DailySwingTradingCommittee11Specialists crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


