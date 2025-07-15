from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PGSearchTool
from crewai_tools import JSONSearchTool
from crewai_tools import XMLSearchTool

@CrewBase
class ComprehensiveCrewAutomationForEquityTradingPlatformCrew():
    """ComprehensiveCrewAutomationForEquityTradingPlatform crew"""

    @agent
    def data_ingestion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_ingestion_agent'],
            tools=[PGSearchTool(), JSONSearchTool(), XMLSearchTool()],
        )

    @agent
    def price_feed_sub_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['price_feed_sub_agent'],
            tools=[JSONSearchTool()],
        )

    @agent
    def fundamentals_sub_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['fundamentals_sub_agent'],
            tools=[JSONSearchTool()],
        )

    @agent
    def sector_taxonomy_sub_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['sector_taxonomy_sub_agent'],
            tools=[XMLSearchTool()],
        )

    @agent
    def news_event_sub_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['news_event_sub_agent'],
            tools=[JSONSearchTool()],
        )


    @task
    def fetch_market_prices(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_market_prices'],
            tools=[JSONSearchTool()],
        )

    @task
    def retrieve_financial_fundamentals(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_financial_fundamentals'],
            tools=[JSONSearchTool()],
        )

    @task
    def map_sector_classifications(self) -> Task:
        return Task(
            config=self.tasks_config['map_sector_classifications'],
            tools=[XMLSearchTool()],
        )

    @task
    def track_news_and_events(self) -> Task:
        return Task(
            config=self.tasks_config['track_news_and_events'],
            tools=[JSONSearchTool()],
        )

    @task
    def store_data_in_database(self) -> Task:
        return Task(
            config=self.tasks_config['store_data_in_database'],
            tools=[PGSearchTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ComprehensiveCrewAutomationForEquityTradingPlatform crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
