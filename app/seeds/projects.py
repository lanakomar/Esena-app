from app.models import db, User, Project

from datetime import datetime


def seed_projects():
    esena_email_project = Project(name="Email alerts on Esena", description="When users are away from Esena app, they will receive notifications by email.", start_date=datetime(
        2023, 3, 1), end_date=datetime(2023, 4, 1), is_archived=False, is_private=True, priority_id=1, status_id=1, owner_id=1)

    nescord_project = Project(name="iOS messenger for Nescord", description="An instant messaging app for Nescord.", start_date=datetime(
        2023, 3, 15), end_date=datetime(2023, 3, 22), is_archived=False, is_private=False, priority_id=1, status_id=1, owner_id=5)

    walk_project = Project(name="Map my walk", description="An app that allows users to track where and how far they have walked each day.", start_date=datetime(
        2023, 3, 3), end_date=datetime(2023, 7, 25), is_archived=False, is_private=False, priority_id=2, status_id=3, owner_id=8)

    cupid_project = Project(name="PetCupid", description="An app that connects pet owners with other pet owners and allows them to chat and exchange advice.",
                            start_date=datetime(2023, 3, 14), end_date=datetime(2023, 6, 7), is_archived=False, is_private=True, priority_id=2, status_id=2, owner_id=1)

    ml_project = Project(name="Identify Trends with ML", description="Understand the company's current and future machine learning strategy, conduct secondary research on machine learning applications for similar use cases, and interview company's users to understand how and why they conduct multi-studies",
                         start_date=datetime(2023, 3, 2), end_date=datetime(2023, 6, 8), is_archived=False, is_private=False, priority_id=3, status_id=3, owner_id=1)

    persona_project = Project(name="Align Teams Across Personas", description="The Company has many forms of personas currently in use across the product and engineering organizations. We need to create formalized personas to align teams, projects, and product strategy",
                              start_date=datetime(2023, 3, 11), end_date=datetime(2023, 5, 11), is_archived=False, is_private=False, priority_id=1, status_id=3, owner_id=2)

    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    user4 = User.query.get(4)
    user5 = User.query.get(5)
    user6 = User.query.get(6)
    user7 = User.query.get(7)
    user8 = User.query.get(8)

    esena_email_project.members.append(user2)
    esena_email_project.members.append(user3)
    esena_email_project.members.append(user4)

    nescord_project.members.append(user1)
    nescord_project.members.append(user4)
    nescord_project.members.append(user6)
    nescord_project.members.append(user7)

    walk_project.members.append(user1)
    walk_project.members.append(user2)
    walk_project.members.append(user5)

    cupid_project.members.append(user3)
    cupid_project.members.append(user4)
    cupid_project.members.append(user6)
    cupid_project.members.append(user8)

    ml_project.members.append(user2)
    ml_project.members.append(user5)
    ml_project.members.append(user7)
    ml_project.members.append(user3)
    ml_project.members.append(user8)

    persona_project.members.append(user1)
    persona_project.members.append(user3)
    persona_project.members.append(user6)
    persona_project.members.append(user7)

    db.session.add(esena_email_project)
    db.session.add(nescord_project)
    db.session.add(walk_project)
    db.session.add(cupid_project)
    db.session.add(ml_project)
    db.session.add(persona_project)

    db.session.commit()


def undo_projects():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.commit()
