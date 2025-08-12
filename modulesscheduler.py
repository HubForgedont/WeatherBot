"""
Scheduler module for managing timed tasks
"""

import time
import datetime
import logging
import schedule

logger = logging.getLogger(__name__)

class Scheduler:
    """Class for scheduling and managing recurring tasks"""
    
    def __init__(self):
        """Initialize the scheduler"""
        self.scheduler = schedule
        logger.info("Scheduler initialized")
    
    def schedule_daily(self, task, at_time="08:00"):
        """
        Schedule a task to run daily at a specific time
        
        Args:
            task (callable): Function to execute
            at_time (str): Time to run the task (24-hour format, e.g., "08:00")
        """
        self.scheduler.every().day.at(at_time).do(task)
        logger.info(f"Task scheduled daily at {at_time}")
    
    def schedule_hourly(self, task):
        """Schedule a task to run every hour"""
        self.scheduler.every().hour.do(task)
        logger.info("Task scheduled hourly")
    
    def schedule_interval(self, task, interval_minutes):
        """
        Schedule a task to run at regular intervals
        
        Args:
            task (callable): Function to execute
            interval_minutes (int): Interval in minutes
        """
        self.scheduler.every(interval_minutes).minutes.do(task)
        logger.info(f"Task scheduled every {interval_minutes} minutes")
    
    def run_pending(self):
        """Run pending scheduled tasks"""
        self.scheduler.run_pending()
