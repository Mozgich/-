if __name__ == "__main__":
    class Profession:
        """Базовый класс для профессий."""

        def init(self, name: str, experience: int):
            """Инициализация профессии с указанием имени и опыта работы."""
            self._name = name
            self._experience = experience

        def introduce(self) -> str:
            """Представление профессии."""
            return f"Профессия: {self._name}, Опыт работы: {self._experience} лет"

        def get_name(self) -> str:
            """Получить имя профессии."""
            return self._name

        def get_experience(self) -> int:
            """Получить опыт работы."""
            return self._experience


    class Doctor(Profession):
        """Дочерний класс для врачей."""

        def init(self, name: str, experience: int, specialization: str):
            """Инициализация врача с указанием имени, опыта работы и специализации."""
            super().init(name, experience)
            self._specialization = specialization

        def introduce(self) -> str:
            """Представление врача."""
            return f"{super().introduce()}, Специализация: {self._specialization}"


    class Teacher(Profession):
        """Дочерний класс для учителей."""

        def init(self, name: str, experience: int, subject: str):
            """Инициализация учителя с указанием имени, опыта работы и предмета преподавания."""
            super().init(name, experience)
            self._subject = subject

        def introduce(self) -> str:
            """Представление учителя."""
            return f"{super().introduce()}, Предмет преподавания: {self._subject}"
    pass
