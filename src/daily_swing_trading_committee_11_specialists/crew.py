import os
import requests
from pathlib import Path
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# [추가] 파일 위치를 찾기 위한 기준 경로 설정
base_path = Path(__file__).parent

# [설정] 무료 Groq 모델 정의
GROQ_LLM = LLM(
    model="groq/llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

@CrewBase
class DailySwingTradingCommittee11SpecialistsCrew:
    """DailySwingTradingCommittee11Specialists crew"""

    # [수정] 설정 파일의 경로를 절대 경로로 직접 지정 (에러 방지 핵심)
    agents_config = os.path.join(base_path, 'config/agents.yaml')
    tasks_config = os.path.join(base_path, 'config/tasks.yaml')

    # --- 텔레그램 전송 함수 ---
    def send_telegram_msg(self, result):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            text = f"🚀 [AI 투자 위원회 결론]\n\n{str(result)}"
            requests.post(url, json={"chat_id": chat_id, "text": text[:4000]})

    # --- 에이전트 정의 (LLM은 Groq, Tools는 비움) ---

    @agent
    def senior_technical_market_analyst(self) -> Agent:
        return Agent(config=self.agents_config["senior_technical_market_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def fundamental_market_research_analyst(self) -> Agent:
        return Agent(config=self.agents_config["fundamental_market_research_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def geopolitical_risk_analyst(self) -> Agent:
        return Agent(config=self.agents_config["geopolitical_risk_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def senior_investment_committee_moderator(self) -> Agent:
        return Agent(config=self.agents_config["senior_investment_committee_moderator"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def professional_chart_pattern_analyst(self) -> Agent:
        return Agent(config=self.agents_config["professional_chart_pattern_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def market_momentum_and_sentiment_specialist(self) -> Agent:
        return Agent(config=self.agents_config["market_momentum_and_sentiment_specialist"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def cryptocurrency_and_digital_assets_analyst(self) -> Agent:
        return Agent(config=self.agents_config["cryptocurrency_and_digital_assets_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def small_cap_growth_specialist(self) -> Agent:
        return Agent(config=self.agents_config["small_cap_growth_specialist"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def macro_sector_rotation_analyst(self) -> Agent:
        return Agent(config=self.agents_config["macro_sector_rotation_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def etf_strategy_specialist(self) -> Agent:
        return Agent(config=self.agents_config["etf_strategy_specialist"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def commodities_and_materials_analyst(self) -> Agent:
        return Agent(config=self.agents_config["commodities_and_materials_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def federal_reserve_and_monetary_policy_analyst(self) -> Agent:
        return Agent(config=self.agents_config["federal_reserve_and_monetary_policy_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    # --- 태스크 정의 ---

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
    def
