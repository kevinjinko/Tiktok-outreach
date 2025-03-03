from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool

@CrewBase
class TiktokProfileMessagingAgentCrew():
    """TiktokProfileMessagingAgent crew"""

    @agent
    def profile_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_finder'],
            tools=[SeleniumScrapingTool()],
        )

    @agent
    def profile_filter(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_filter'],
            tools=[],
        )

    @agent
    def dm_dispatcher(self) -> Agent:
        return Agent(
            config=self.agents_config['dm_dispatcher'],
            tools=[SeleniumScrapingTool()],
        )

    @agent
    def logger(self) -> Agent:
        return Agent(
            config=self.agents_config['logger'],
            tools=[],
        )


    @task
    def search_travel_profiles(self) -> Task:
        return Task(
            config=self.tasks_config['search_travel_profiles'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def extract_profile_details(self) -> Task:
        return Task(
            config=self.tasks_config['extract_profile_details'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def filter_travel_profiles(self) -> Task:
        return Task(
            config=self.tasks_config['filter_travel_profiles'],
            tools=[],
        )

    @task
    def send_dm_to_profiles(self) -> Task:
        return Task(
            config=self.tasks_config['send_dm_to_profiles'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def log_messaging_outcomes(self) -> Task:
        return Task(
            config=self.tasks_config['log_messaging_outcomes'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the TiktokProfileMessagingAgent crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
