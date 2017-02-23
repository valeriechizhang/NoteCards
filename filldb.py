from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Notebook, Card


engine = create_engine('sqlite:///notecards.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


# clean up
notebooks = session.query(Notebook).all()
for n in notebooks:
    cards = session.query(Card).filter_by(notebook_id=n.id).all()
    for c in cards:
        session.delete(c)
        session.commit()
    session.delete(n)
    session.commit()

users = session.query(User).all()
for u in users:
    session.delete(u)
    session.commit()


# Dummy user
User1 = User(name="user1", email="user1@udacity.com")
session.add(User1)
session.commit()

User2 = User(name="user2", email="user2@udacity.com")
session.add(User2)
session.commit()

# Dummy Notebook
Notebook1 = Notebook(name="GRE Vocab 1", description="The first GRE vocab collection", user_id=1)
Notebook2 = Notebook(name="GRE Vocab 2", description="The second GRE vocab collection", user_id=1)
Notebook3 = Notebook(name="GRE Vocab 3", description="The third GRE vocab collection", user_id=1)
Notebook4 = Notebook(name="GRE Vocab 4", description="The fourth GRE vocab collection", user_id=2)
Notebook5 = Notebook(name="GRE Vocab 5", description="The fifth GRE vocab collection", user_id=2)
Notebook6 = Notebook(name="GRE Vocab 6", description="The sixth GRE vocab collection", user_id=2)
session.add(Notebook1)
session.add(Notebook2)
session.add(Notebook3)
session.add(Notebook4)
session.add(Notebook5)
session.commit()


# Dummy Cards
Card1_1 = Card(term="aberrant", description="deviating from normal or correct.", tag="adj.", notebook_id=1)
Card1_2 = Card(term="abscond", description="to leave secretly and hide, often to avoid the law.", tag="v.", notebook_id=1)
Card1_3 = Card(term="advocate", description="to speak, plead, or argue for a cause, or in another's behalf. (n) -- one who advocates.", tag="v., n.", notebook_id=1)
Card1_4 = Card(term="aggrandize", description="to make greater, to increase, thus, to exaggerate.", tag="v.", notebook_id=1)
Card1_5 = Card(term="amalgamate", description="to unite or mix. (n) -- amalgamation.", tag="v.", notebook_id=1)
Card1_6 = Card(term="ambiguous", description="vague; subject to more than one interpretation", tag="adj.", notebook_id=1)
Card1_7 = Card(term="ambrosial", description="extremely pleasing to the senses, divine (as related to the gods) or delicious (n: ambrosia)", tag="adj.", notebook_id=1)
Card1_8 = Card(term="anachronism", description="a person or artifact appearing after its own time or out of chronological order (adj: anachronistic)", tag="n.", notebook_id=1)

session.add(Card1_1)
session.add(Card1_2)
session.add(Card1_3)
session.add(Card1_4)
session.add(Card1_5)
session.add(Card1_6)
session.add(Card1_7)
session.add(Card1_8)
session.commit()


Card2_1 = Card(term="aberrant", description="deviating from normal or correct.", tag="adj.", notebook_id=2)
Card2_2 = Card(term="abscond", description="to leave secretly and hide, often to avoid the law.", tag="v.", notebook_id=2)
Card2_3 = Card(term="advocate", description="to speak, plead, or argue for a cause, or in another's behalf. (n) -- one who advocates.", tag="v., n.", notebook_id=2)
Card2_4 = Card(term="aggrandize", description="to make greater, to increase, thus, to exaggerate.", tag="v.", notebook_id=2)
Card2_5 = Card(term="amalgamate", description="to unite or mix. (n) -- amalgamation.", tag="v.", notebook_id=2)
Card2_6 = Card(term="ambiguous", description="vague; subject to more than one interpretation", tag="adj.", notebook_id=2)
Card2_7 = Card(term="ambrosial", description="extremely pleasing to the senses, divine (as related to the gods) or delicious (n: ambrosia)", tag="adj.", notebook_id=2)
Card2_8 = Card(term="anachronism", description="a person or artifact appearing after its own time or out of chronological order (adj: anachronistic)", tag="n.", notebook_id=2)

session.add(Card2_1)
session.add(Card2_2)
session.add(Card2_3)
session.add(Card2_4)
session.add(Card2_5)
session.add(Card2_6)
session.add(Card2_7)
session.add(Card2_8)
session.commit()

Card3_1 = Card(term="aberrant", description="deviating from normal or correct.", tag="adj.", notebook_id=3)
Card3_2 = Card(term="abscond", description="to leave secretly and hide, often to avoid the law.", tag="v.", notebook_id=3)
Card3_3 = Card(term="advocate", description="to speak, plead, or argue for a cause, or in another's behalf. (n) -- one who advocates.", tag="v., n.", notebook_id=3)
Card3_4 = Card(term="aggrandize", description="to make greater, to increase, thus, to exaggerate.", tag="v.", notebook_id=3)
Card3_5 = Card(term="amalgamate", description="to unite or mix. (n) -- amalgamation.", tag="v.", notebook_id=3)
Card3_6 = Card(term="ambiguous", description="vague; subject to more than one interpretation", tag="adj.", notebook_id=3)
Card3_7 = Card(term="ambrosial", description="extremely pleasing to the senses, divine (as related to the gods) or delicious (n: ambrosia)", tag="adj.", notebook_id=3)
Card3_8 = Card(term="anachronism", description="a person or artifact appearing after its own time or out of chronological order (adj: anachronistic)", tag="n.", notebook_id=3)

session.add(Card3_1)
session.add(Card3_2)
session.add(Card3_3)
session.add(Card3_4)
session.add(Card3_5)
session.add(Card3_6)
session.add(Card3_7)
session.add(Card3_8)
session.commit()

Card4_1 = Card(term="aberrant", description="deviating from normal or correct.", tag="adj.", notebook_id=4)
Card4_2 = Card(term="abscond", description="to leave secretly and hide, often to avoid the law.", tag="v.", notebook_id=4)
Card4_3 = Card(term="advocate", description="to speak, plead, or argue for a cause, or in another's behalf. (n) -- one who advocates.", tag="v., n.", notebook_id=4)
Card4_4 = Card(term="aggrandize", description="to make greater, to increase, thus, to exaggerate.", tag="v.", notebook_id=4)
Card4_5 = Card(term="amalgamate", description="to unite or mix. (n) -- amalgamation.", tag="v.", notebook_id=4)
Card4_6 = Card(term="ambiguous", description="vague; subject to more than one interpretation", tag="adj.", notebook_id=4)
Card4_7 = Card(term="ambrosial", description="extremely pleasing to the senses, divine (as related to the gods) or delicious (n: ambrosia)", tag="adj.", notebook_id=4)
Card4_8 = Card(term="anachronism", description="a person or artifact appearing after its own time or out of chronological order (adj: anachronistic)", tag="n.", notebook_id=4)

session.add(Card4_1)
session.add(Card4_2)
session.add(Card4_3)
session.add(Card4_4)
session.add(Card4_5)
session.add(Card4_6)
session.add(Card4_7)
session.add(Card4_8)
session.commit()

Card5_1 = Card(term="aberrant", description="deviating from normal or correct.", tag="adj.", notebook_id=5)
Card5_2 = Card(term="abscond", description="to leave secretly and hide, often to avoid the law.", tag="v.", notebook_id=5)
Card5_3 = Card(term="advocate", description="to speak, plead, or argue for a cause, or in another's behalf. (n) -- one who advocates.", tag="v., n.", notebook_id=5)
Card5_4 = Card(term="aggrandize", description="to make greater, to increase, thus, to exaggerate.", tag="v.", notebook_id=5)
Card5_5 = Card(term="amalgamate", description="to unite or mix. (n) -- amalgamation.", tag="v.", notebook_id=5)
Card5_6 = Card(term="ambiguous", description="vague; subject to more than one interpretation", tag="adj.", notebook_id=5)
Card5_7 = Card(term="ambrosial", description="extremely pleasing to the senses, divine (as related to the gods) or delicious (n: ambrosia)", tag="adj.", notebook_id=5)
Card5_8 = Card(term="anachronism", description="a person or artifact appearing after its own time or out of chronological order (adj: anachronistic)", tag="n.", notebook_id=5)

session.add(Card5_1)
session.add(Card5_2)
session.add(Card5_3)
session.add(Card5_4)
session.add(Card5_5)
session.add(Card5_6)
session.add(Card5_7)
session.add(Card5_8)
session.commit()


notebooks = session.query(Notebook).all()
for n in notebooks:
    print '******************************'
    print n.name
    print n.description
    cards = session.query(Card).filter_by(notebook_id=n.id).all()
    for c in cards:
        print c.term
        print c.tag
        print c.description
    print '******************************'


print "added all items!"









