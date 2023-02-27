from app.models import db, Task
from datetime import datetime


def seed_tasks():
    email_task1 = Task(name="Add first name and last name to subject", description="",
                       end_date=datetime(2023, 2, 24), create_date=datetime(2023, 2, 20), status_id=3, priority_id=1, assigner_id=2, assignee_id=1, project_id=1, is_completed=True)
    email_task2 = Task(name="Redo reminder card", description="",
                       end_date=datetime(2023, 2, 23), create_date=datetime(2023, 2, 21), status_id=3, priority_id=1, assigner_id=3, assignee_id=1, project_id=1, is_completed=True)
    email_task3 = Task(name="Hide Configuration menu + get defaults", description="Defaults for email feature",
                       end_date=datetime(2023, 3, 22), create_date=datetime(2023, 3, 2), status_id=2, priority_id=3, assigner_id=4, assignee_id=2, project_id=1, is_completed=False)
    email_task4 = Task(name="Revise the account setting page", description="Users can choose receiving email notifications or not",
                       end_date=datetime(2023, 3, 18), create_date=datetime(2023, 3, 3), status_id=1, priority_id=2, assigner_id=4, assignee_id=1, project_id=1, is_completed=False)
    email_task5 = Task(name="Make sure SC works for all features", description="",
                       end_date=datetime(2023, 3, 29), create_date=datetime(2023, 3, 13), status_id=1, priority_id=1, assigner_id=3, assignee_id=3, project_id=1, is_completed=False)
    email_task6 = Task(name="Clicking on a reminder card should activate reminder tab", description="",
                       end_date=datetime(2023, 3, 30), create_date=datetime(2023, 3, 15), status_id=2, priority_id=1, assigner_id=1, assignee_id=1, project_id=1, is_completed=False)
    email_task7 = Task(name="CSS issues on notification page", description="",
                       end_date=datetime(2023, 3, 17), create_date=datetime(2023, 3, 15), status_id=1, priority_id=2, assigner_id=1, assignee_id=4, project_id=1, is_completed=False)
    email_task8 = Task(name="Remove priority status from overview page", description="",
                       end_date=datetime(2023, 3, 31), create_date=datetime(2023, 3, 13), status_id=3, priority_id=2, assigner_id=1, assignee_id=3, project_id=1, is_completed=False)
    email_task9 = Task(name="Inter IDS in stream subscription", description="",
                       end_date=datetime(2023, 4, 1), create_date=datetime(2023, 3, 12), status_id=3, priority_id=3, assigner_id=2, assignee_id=1, project_id=1, is_completed=False)

    nescord_task1 = Task(name="Enable post rendering logging for STL labels", description="", end_date=datetime(
        2023, 2, 23), create_date=datetime(2023, 2, 19), assigner_id=5, status_id=2, priority_id=2, assignee_id=1, project_id=2, is_completed=True)
    nescord_task2 = Task(name="Enable diagnostics for UIKit", description="", end_date=datetime(2023, 2, 24), create_date=datetime(
        2023, 2, 20), assigner_id=1, status_id=1, priority_id=2, assignee_id=4, project_id=2, is_completed=True)
    nescord_task3 = Task(name="User specified schedule in SLI scheduling", description="", end_date=datetime(2023, 3, 20), create_date=datetime(
        2023, 3, 16), assigner_id=1, status_id=3, priority_id=3, assignee_id=5, project_id=2, is_completed=False)
    nescord_task4 = Task(name="Add option to only show key plots", description="", end_date=datetime(2023, 3, 21), create_date=datetime(
        2023, 3, 17), assigner_id=5, status_id=2, priority_id=3, assignee_id=1, project_id=2, is_completed=False)
    nescord_task5 = Task(name="Reset the SPWT SN state on the downlink when server not responding", description="", end_date=datetime(
        2023, 3, 22), create_date=datetime(2023, 3, 18), assigner_id=4, status_id=1, priority_id=1, assignee_id=1, project_id=2, is_completed=False)
    nescord_task6 = Task(name="Add filed stats for user explicit video pause time in video calls", description="", end_date=datetime(
        2023, 3, 21), create_date=datetime(2023, 3, 19), assigner_id=1, status_id=1, priority_id=3, assignee_id=5, project_id=2, is_completed=False)
    nescord_task7 = Task(name="Detect change of replay list upon group update", description="", end_date=datetime(
        2023, 3, 22), create_date=datetime(2023, 3, 17), assigner_id=6, status_id=2, priority_id=2, assignee_id=7, project_id=2, is_completed=False)
    nescord_task8 = Task(name="Migrate restart based on network condition check", description="", end_date=datetime(
        2023, 3, 19), create_date=datetime(2023, 3, 15), assigner_id=4, status_id=1, priority_id=1, assignee_id=5, project_id=2, is_completed=False)
    nescord_task9 = Task(name="Improve stateful ping usage in client transport", description="", end_date=datetime(
        2023, 3, 22), create_date=datetime(2023, 3, 17), assigner_id=7, status_id=3, priority_id=2, assignee_id=1, project_id=2, is_completed=False)
    nescord_task10 = Task(name="Resets in video call", description="Video image rendering is resetting during video meetings", end_date=datetime(
        2023, 3, 21), create_date=datetime(2023, 3, 15), assigner_id=5, status_id=1, priority_id=3, assignee_id=1, project_id=2, is_completed=False)

    walk_task1 = Task(name="Split store test into multiple targets", description="", end_date=datetime(2023, 2, 23), create_date=datetime(
        2023, 2, 18), status_id=3, priority_id=1, assigner_id=8, assignee_id=2, project_id=3, is_completed=True)
    walk_task2 = Task(name="Track maximum distance from slide window", description="", end_date=datetime(2023, 2, 24), create_date=datetime(
        2023, 2, 19), status_id=2, priority_id=1, assigner_id=1, assignee_id=5, project_id=3, is_completed=True)
    walk_task3 = Task(name="Update client wiki page", description="", end_date=datetime(2023, 5, 12), create_date=datetime(
        2023, 4, 8), status_id=1, priority_id=1, assigner_id=2, assignee_id=8, project_id=3, is_completed=False)
    walk_task4 = Task(name="Improve code structure sheet", description="", end_date=datetime(2023, 4, 16), create_date=datetime(
        2023, 3, 14), status_id=2, priority_id=1, assigner_id=1, assignee_id=1, project_id=3, is_completed=False)
    walk_task5 = Task(name="Add GSO related info on client", description="", end_date=datetime(2023, 4, 15), create_date=datetime(
        2023, 3, 12), status_id=1, priority_id=2, assigner_id=5, assignee_id=1, project_id=3, is_completed=False)
    walk_task6 = Task(name="Enable strict nullability for UXG", description="", end_date=datetime(2023, 7, 18), create_date=datetime(
        2023, 5, 14), status_id=3, priority_id=2, assigner_id=2, assignee_id=8, project_id=3, is_completed=False)
    walk_task7 = Task(name="Verify performance of music player", description="", end_date=datetime(2023, 6, 19), create_date=datetime(
        2023, 5, 16), status_id=2, priority_id=2, assigner_id=5, assignee_id=1, project_id=3, is_completed=False)
    walk_task8 = Task(name="Bring back help section", description="", end_date=datetime(2023, 3, 21), create_date=datetime(
        2023, 3, 4), status_id=1, priority_id=3, assigner_id=8, assignee_id=1, project_id=3, is_completed=False)
    walk_task9 = Task(name="Remove translation status", description="", end_date=datetime(2023, 3, 22), create_date=datetime(
        2023, 3, 5), status_id=3, priority_id=3, assigner_id=1, assignee_id=2, project_id=3, is_completed=False)
    walk_task10 = Task(name="Adjust CSS on profile page", description="", end_date=datetime(2023, 4, 24), create_date=datetime(
        2023, 4, 1), status_id=1, priority_id=1, assigner_id=1, assignee_id=5, project_id=3, is_completed=False)

    cupid_task1 = Task(name="Use imgix API to optimize the image", description="", end_date=datetime(2023, 2, 23), create_date=datetime(
        2023, 2, 18), status_id=2, priority_id=2, assigner_id=1, assignee_id=3, project_id=4, is_completed=True)
    cupid_task2 = Task(name="Add Payfast Payment Gateway", description="", end_date=datetime(2023, 2, 24), create_date=datetime(
        2023, 2, 17), status_id=1, priority_id=2, assigner_id=6, assignee_id=4, project_id=4, is_completed=True)
    cupid_task3 = Task(name="User Status Circle", description="", end_date=datetime(2023, 4, 8), create_date=datetime(
        2023, 3, 15), status_id=3, priority_id=1, assigner_id=8, assignee_id=6, project_id=4, is_completed=False)
    cupid_task4 = Task(name="Improve private live chat", description="", end_date=datetime(2023, 4, 10), create_date=datetime(
        2023, 3, 22), status_id=2, priority_id=3, assigner_id=1, assignee_id=8, project_id=4, is_completed=False)
    cupid_task5 = Task(name="Create an invoice section in the User's account", description="", end_date=datetime(
        2023, 5, 15), create_date=datetime(2023, 4, 5), status_id=1, priority_id=2, assigner_id=3, assignee_id=1, project_id=4, is_completed=False)
    cupid_task6 = Task(name="Move badages to different sections", description="", end_date=datetime(2023, 4, 14), create_date=datetime(
        2023, 3, 12), status_id=2, priority_id=1, assigner_id=4, assignee_id=1, project_id=4, is_completed=False)
    cupid_task7 = Task(name="Improve file readability", description="", end_date=datetime(2023, 3, 30), create_date=datetime(
        2023, 3, 14), status_id=2, priority_id=2, assigner_id=6, assignee_id=3, project_id=4, is_completed=False)
    cupid_task8 = Task(name="Improve way of logging error msg", description="", end_date=datetime(2023, 4, 23), create_date=datetime(
        2023, 3, 19), status_id=3, priority_id=1, assigner_id=1, assignee_id=4, project_id=4, is_completed=False)
    cupid_task9 = Task(name="Cleanup kernel constant and ban class", description="", end_date=datetime(2023, 6, 7), create_date=datetime(
        2023, 5, 21), status_id=2, priority_id=1, assigner_id=8, assignee_id=1, project_id=4, is_completed=False)
    cupid_task10 = Task(name="Access Admin Panel Upon Installation ", description="", end_date=datetime(2023, 5, 28), create_date=datetime(
        2023, 4, 27), status_id=1, priority_id=3, assigner_id=1, assignee_id=6, project_id=4, is_completed=False)

    ai_task1 = Task(name="Conduct quantitative data analysis", description="Narrow down a specific, relevant audience to identify the users who conduct the highest percentages of multi-studies.",
                    end_date=datetime(2023, 2, 22), create_date=datetime(2023, 2, 16), status_id=2, priority_id=2, assigner_id=2, assignee_id=1, project_id=5, is_completed=True)
    ai_task2 = Task(name="Conduct qualitiative interviews", description="Expand beyond the quantitative data, ask questions about why and how to support user research",
                    end_date=datetime(2023, 2, 24), create_date=datetime(2023, 2, 17), status_id=1, priority_id=3, assigner_id=5, assignee_id=3, project_id=5, is_completed=True)
    ai_task3 = Task(name="Construct product strategy with metrics", description="Present strongest ideas to stakeholders, using Desirability, Feasibility, Viability metrics",
                    end_date=datetime(2023, 3, 24), create_date=datetime(2023, 3, 3), status_id=2, priority_id=1, assigner_id=5, assignee_id=7, project_id=5, is_completed=False)
    ai_task4 = Task(name="Build a usable dataset ", description="Work with engineers to pull data from API queries to parse JSON files into relational database and readable data",
                    end_date=datetime(2023, 3, 27), create_date=datetime(2023, 3, 10), status_id=3, priority_id=1, assigner_id=3, assignee_id=2, project_id=5, is_completed=False)
    ai_task5 = Task(name="Transform dataset into pattern set", description="Transform textual values into numerical vectors into readable outputs or predictions from data models",
                    end_date=datetime(2023, 4, 21),  create_date=datetime(2023, 3, 18), status_id=2, priority_id=3, assigner_id=8, assignee_id=1, project_id=5, is_completed=False)
    ai_task6 = Task(name="Seasonality analysis", description="Seasonality can affect the data so we must normalize the data to eliminate biases", end_date=datetime(
        2023, 4, 25),  create_date=datetime(2023, 3, 22), status_id=3, priority_id=3, assigner_id=1, assignee_id=1, project_id=5, is_completed=False)
    ai_task7 = Task(name="Conduct Stationarity Test", description="Data can also be affected by time, run autocorrelation and statistical tests to determine if data is stationary",
                    end_date=datetime(2023, 5, 3),  create_date=datetime(2023, 4, 1), status_id=1, priority_id=2, assigner_id=1, assignee_id=8, project_id=5, is_completed=False)
    ai_task8 = Task(name="Understand association patterns", description="Cluster data into certain pattern sets and understand user behavior", end_date=datetime(
        2023, 6, 8),  create_date=datetime(2023, 5, 5), status_id=2, priority_id=1, assigner_id=2, assignee_id=3, project_id=5, is_completed=False)
    ai_task9 = Task(name="Process Mining Analysis", description="Where do users experience the most complex behaviors in the product? What can we do to ease their experience and cut down on attrition?",
                    end_date=datetime(2023, 4, 15), create_date=datetime(2023, 3, 12), status_id=3, priority_id=1, assigner_id=5, assignee_id=7, project_id=5, is_completed=False)
    ai_task10 = Task(name="Prepare proposition slide deck", description="Create clean slides to present ideas to stakeholders, submit for review", end_date=datetime(
        2023, 4, 22), create_date=datetime(2023, 3, 18), status_id=2, priority_id=3, assigner_id=1, assignee_id=7, project_id=5, is_completed=False)

    persona_task1 = Task(name="Conduct interviews", description="Conduct interviews with Product and Engineering Teams, as well as the Company's users", end_date=datetime(
        2023, 2, 23), create_date=datetime(2023, 2, 15), status_id=1, priority_id=1, assigner_id=1, assignee_id=6, project_id=6, is_completed=True)
    persona_task2 = Task(name="Formulate thesis from interview data", description="Construct the Why the Company needs formalized personas, what makes personas valuable, and what is needed to ensure adoption. Also, understand any empathy gaps and questions we still have about our users",
                         end_date=datetime(2023, 2, 24), create_date=datetime(2023, 2, 20), status_id=2, priority_id=3, assigner_id=3, assignee_id=3, project_id=6, is_completed=True)
    persona_task3 = Task(name="Data visualization", description="Break raw research out into a visual map of themes and common feelings and thoughts from user interviews",
                         end_date=datetime(2023, 5, 11), create_date=datetime(2023, 4, 25), status_id=1, priority_id=2, assigner_id=2, assignee_id=1, project_id=6, is_completed=False)
    persona_task4 = Task(name="Propose product team strategy", description="Given data from conducted interviews, propose plan as to how we can explore persona visualizations and frameworks to entice various stakeholders",
                         end_date=datetime(2023, 4, 5), create_date=datetime(2023, 3, 11),  status_id=2, priority_id=1, assigner_id=6, assignee_id=7, project_id=6, is_completed=False)
    persona_task5 = Task(name="Construct product strategy", description="How does our research and thesis align with the current product roadmap?", end_date=datetime(
        2023, 5, 11), create_date=datetime(2023, 4, 12), status_id=3, priority_id=1, assigner_id=7, assignee_id=2, project_id=6, is_completed=False)
    persona_task6 = Task(name="Reflect on future customers", description="Understand how our current strategy will affect current customers but also future customers with changing landscapes",
                         end_date=datetime(2023, 3, 29), create_date=datetime(2023, 3, 19), status_id=1, priority_id=3, assigner_id=1, assignee_id=7, project_id=6, is_completed=False)

    db.session.add(email_task1)
    db.session.add(email_task2)
    db.session.add(email_task3)
    db.session.add(email_task4)
    db.session.add(email_task5)
    db.session.add(email_task6)
    db.session.add(email_task7)
    db.session.add(email_task8)
    db.session.add(email_task9)

    db.session.add(nescord_task1)
    db.session.add(nescord_task2)
    db.session.add(nescord_task3)
    db.session.add(nescord_task4)
    db.session.add(nescord_task5)
    db.session.add(nescord_task6)
    db.session.add(nescord_task7)
    db.session.add(nescord_task8)
    db.session.add(nescord_task9)
    db.session.add(nescord_task10)

    db.session.add(walk_task1)
    db.session.add(walk_task2)
    db.session.add(walk_task3)
    db.session.add(walk_task4)
    db.session.add(walk_task5)
    db.session.add(walk_task6)
    db.session.add(walk_task7)
    db.session.add(walk_task8)
    db.session.add(walk_task9)
    db.session.add(walk_task10)

    db.session.add(cupid_task1)
    db.session.add(cupid_task2)
    db.session.add(cupid_task3)
    db.session.add(cupid_task4)
    db.session.add(cupid_task5)
    db.session.add(cupid_task6)
    db.session.add(cupid_task7)
    db.session.add(cupid_task8)
    db.session.add(cupid_task9)
    db.session.add(cupid_task10)

    db.session.add(ai_task1)
    db.session.add(ai_task2)
    db.session.add(ai_task3)
    db.session.add(ai_task4)
    db.session.add(ai_task5)
    db.session.add(ai_task6)
    db.session.add(ai_task7)
    db.session.add(ai_task8)
    db.session.add(ai_task9)
    db.session.add(ai_task10)

    db.session.add(persona_task1)
    db.session.add(persona_task2)
    db.session.add(persona_task3)
    db.session.add(persona_task4)
    db.session.add(persona_task5)
    db.session.add(persona_task6)

    db.session.commit()


def undo_tasks():
    db.session.execute('TRUNCATE tasks RESTART IDENTITY CASCADE;')
    db.session.commit()
