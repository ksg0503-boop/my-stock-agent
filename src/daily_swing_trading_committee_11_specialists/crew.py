import os
import requests
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    SerperDevTool,
    SerplyNewsSearchTool,
    BraveSearchTool
)

# 무료 Groq 모델 설정
GROQ_LLM = LLM(
    model="groq/llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

@CrewBase
class DailySwingTradingCommittee11SpecialistsCrew:
    """DailySwingTradingCommittee11Specialists crew"""

    # --- 텔레그램 전송 함수 ---
    def send_telegram_msg(self, result):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            text = f"🚀 [AI 투자 위원회 결론]\n\n{str(result)}"
            requests.post(url, json={"chat_id": chat_id, "text": text[:4000]})

    # --- 에이전트 정의 ---
    @agent
    def senior_technical_market_analyst(self) -> Agent:
        return Agent(config=self.agents_config["senior_technical_market_analyst"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def fundamental_market_research_analyst(self) -> Agent:
        return Agent(config=self.agents_config["fundamental_market_research_analyst"], tools=[SerplyNewsSearchTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def geopolitical_risk_analyst(self) -> Agent:
        return Agent(config=self.agents_config["geopolitical_risk_analyst"], tools=[BraveSearchTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def senior_investment_committee_moderator(self) -> Agent:
        return Agent(config=self.agents_config["senior_investment_committee_moderator"], llm=GROQ_LLM, verbose=True)

    @agent
    def professional_chart_pattern_analyst(self) -> Agent:
        return Agent(config=self.agents_config["professional_chart_pattern_analyst"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def market_momentum_and_sentiment_specialist(self) -> Agent:
        return Agent(config=self.agents_config["market_momentum_and_sentiment_specialist"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def cryptocurrency_and_digital_assets_analyst(self) -> Agent:
        return Agent(config=self.agents_config["cryptocurrency_and_digital_assets_analyst"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def small_cap_growth_specialist(self) -> Agent:
        return Agent(config=self.agents_config["small_cap_growth_specialist"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def macro_sector_rotation_analyst(self) -> Agent:
        return Agent(config=self.agents_config["macro_sector_rotation_analyst"], tools=[SerplyNewsSearchTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def etf_strategy_specialist(self) -> Agent:
        return Agent(config=self.agents_config["etf_strategy_specialist"], tools=[SerperDevTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def commodities_and_materials_analyst(self) -> Agent:
        return Agent(config=self.agents_config["commodities_and_materials_analyst"], tools=[BraveSearchTool()], llm=GROQ_LLM, verbose=True)

    @agent
    def federal_reserve_and_monetary_policy_analyst(self) -> Agent:
        return Agent(config=self.agents_config["federal_reserve_and_monetary_policy_analyst"], tools=[SerplyNewsSearchTool()], llm=GROQ_LLM, verbose=True)

    # --- 태스크 정의 (콜론 ':' 오타 모두 수정 완료) ---
    @task
    def daily_technical_swing_trading_analysis(self) -> Task:
        return Task(config=self.tasks_config["daily_technical_swing_trading_analysis"])

    @task
    def daily_fundamental_swing_catalyst_analysis(self) -> Task:
        return Task(config=self.tasks_config["daily_fundamental_swing_catalyst_analysis"])

    @task
    def geopolitical_risk_assessment(self) -> Task:
        return Task(config=self.tasks_config["geopolitical_risk_assessment"])

    @task
    def chart_pattern_analysis(self) -> Task:
        return Task(config=self.tasks_config["chart_pattern_analysis"])

    @task
    def momentum_and_sentiment_analysis(self) -> Task:
        return Task(config=self.tasks_config["momentum_and_sentiment_analysis"])

    @task
    def cryptocurrency_market_analysis(self) -> Task:
        return Task(config=self.tasks_config["cryptocurrency_market_analysis"])

    @task
    def small_cap_opportunity_discovery(self) -> Task:
        return Task(config=self.tasks_config["small_cap_opportunity_discovery"])

    @task
    def macro_sector_flow_analysis(self) -> Task:
        return Task(config=self.tasks_config["macro_sector_flow_analysis"])

    @task
    def etf_market_opportunity_analysis(self) -> Task:
        return Task(config=self.tasks_config["etf_market_opportunity_analysis"])

    @task
    def commodity_and_materials_market_analysis(self) -> Task:
        return Task(config=self.tasks_config["commodity_and_materials_market_analysis"])

    @task
    def federal_reserve_policy_impact_analysis(self) -> Task:
        return Task(config=self.tasks_config["federal_reserve_policy_impact_analysis"])

    @task
    def daily_investment_committee_consensus(self) -> Task:
        return Task(config=self.tasks_config["daily_investment_committee_consensus"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
