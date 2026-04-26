#!/usr/bin/env python
import sys
import os
from daily_swing_trading_committee_11_specialists.crew import DailySwingTradingCommittee11SpecialistsCrew

def run():
    """
    전문가 위원회를 실행하고 결과를 텔레그램으로 전송합니다.
    """
    # 1. 어떤 주제로 조사할지 기본 입력값을 정합니다.
    inputs = {
        'current_date': '2026-04-26', # 현재 날짜 정보를 주면 AI가 더 정확히 판단합니다.
        'market_focus': '미국 및 한국 주식 시장 스윙 트레이딩 종목 추천'
    }
    
    # 2. 에이전트들을 소집하여 토론을 시작합니다.
    crew_instance = DailySwingTradingCommittee11SpecialistsCrew()
    result = crew_instance.crew().kickoff(inputs=inputs)

    # 3. 토론 결과(result)를 텔레그램으로 발송합니다.
    print("토론 완료! 결과를 텔레그램으로 전송합니다...")
    crew_instance.send_telegram_msg(result)

def train():
    """에이전트 학습 모드"""
    inputs = {}
    try:
        DailySwingTradingCommittee11SpecialistsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"학습 중 에러 발생: {e}")

def replay():
    """특정 작업부터 다시 실행"""
    try:
        DailySwingTradingCommittee11SpecialistsCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"재실행 중 에러 발생: {e}")

def test():
    """테스트 모드"""
    inputs = {}
    try:
        DailySwingTradingCommittee11SpecialistsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"테스트 중 에러 발생: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"알 수 없는 명령어: {command}")
        sys.exit(1)