from faker import Faker

from .models.db import get_db
from .models.models import Article

session = next(get_db())
fake = Faker()


def main() -> None:
    session.query(Article).delete()
    instances = []
    for _ in range(10):
        title = fake.text(max_nb_chars=20)
        content = fake.text(max_nb_chars=100)
        article = Article(title=title, content=content)
        instances.append(article)
    session.add_all(instances)
    session.commit()


if __name__ == "__main__":
    main()
