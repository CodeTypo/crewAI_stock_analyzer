#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from IPython.display import Markdown


from crewai_stock_analyzer.crew import CrewaiStockAnalyzer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    financial_trading_inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }
    
    try:
        result = CrewaiStockAnalyzer().crew().kickoff(inputs=financial_trading_inputs)
        Markdown(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")   

if __name__ == "__main__":
    run()