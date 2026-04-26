import os
import requests
from pathlib import Path
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# 파일 위치 기준 경로 설정
base_path = Path(__file__).parent

# [설정] 무료 Groq 모델 (Llama 3.1 70B)
# 속도 제한을 방지하기 위해 70B 모델을 사용합니다.
GROQ_LLM = LLM(
    model="groq/llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

@CrewBase
class DailySwingTradingCommittee11SpecialistsCrew:
    """정예 멤버로 구성된 주식 투자 위원회"""

    # 설정 파일 경로 지정
    agents_config = os.path.join(base_path, 'config/agents.yaml')
    tasks_config = os.path.join(base_path, 'config/tasks.yaml')

    # --- 텔레그램 전송 함수 ---
    def send_telegram_msg(self, result):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            text = f"🚀 [정예 AI 투자 위원회 결론]\n\n{str(result)}"
            # 텔레그램 안전 전송을 위해 4000자로 제한
            requests.post(url, json={"chat_id": chat_id, "text": text[:4000]})

    # --- 핵심 에이전트 4명 정의 (안정적 실행을 위해 축소) ---

    @agent
    def senior_technical_market_analyst(self) -> Agent:
        return Agent(config=self.agents_config["senior_technical_market_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def fundamental_market_research_analyst(self) -> Agent:
        return Agent(config=self.agents_config["fundamental_market_research_analyst"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def market_momentum_and_sentiment_specialist(self) -> Agent:
        return Agent(config=self.agents_config["market_momentum_and_sentiment_specialist"], tools=[], llm=GROQ_LLM, verbose=True)

    @agent
    def senior_investment_committee_moderator(self) -> Agent:
        return Agent(config=self.agents_config["senior_investment_committee_moderator"], tools=[], llm=GROQ_LLM, verbose=True)

    # --- 핵심 태스크 정의 ---

    @task
    def daily_technical_swing_trading_analysis(self) -> Task:
        return Task(config=self.tasks_config["daily_technical_swing_trading_analysis"])

    @task
    def daily_fundamental_swing_catalyst_analysis(self) -> Task:
        return Task(config=self.tasks_config["daily_fundamental_swing_catalyst_analysis"])

    @task
    def momentum_and_sentiment_analysis(self) -> Task:
        return Task(config=self.tasks_config["momentum_and_sentiment_analysis"])

    @task
    def daily_investment_committee_consensus(self) -> Task:
        return Task(config=self.tasks_config["daily_investment_committee_consensus"])

    # --- 크루 설정 (속도 제한 방지 로직 추가) ---

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # [중요] 무료 사용자를 위해 1분당 질문 횟수를 2회로 제한하여 에러 방지
            max_rpm=2 
        )
