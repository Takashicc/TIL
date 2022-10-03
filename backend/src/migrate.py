from .models import models
from .models.db import engine


def main() -> None:
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
