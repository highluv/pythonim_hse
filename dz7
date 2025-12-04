import csv


class Client:
    def __init__(self, full_name, gender, age, device, browser, amount, region):
        self.full_name = full_name
        self.gender = gender.lower().strip()       # male/female
        self.age = int(age)
        self.device = device.lower().strip()
        self.browser = browser
        self.amount = float(amount)
        self.region = region

    @classmethod
    def from_csv_row(cls, row: dict):
        return cls(
            full_name=row["name"],
            gender=row["sex"],
            age=row["age"],
            device=row["device_type"],
            browser=row["browser"],
            amount=row["bill"],
            region=row["region"]
        )

    def to_description(self) -> str:
        gender_text = self.gender_to_text(self.gender)
        verb = self.gender_to_verb(self.gender)
        device_text = self.device_to_text(self.device)

        return (
            f"Пользователь {self.full_name} {gender_text}, {self.age} лет, "
            f"{verb} покупку на {int(self.amount)} у.е. "
            f"с {device_text} браузера {self.browser}. "
            f"Регион, из которого совершалась покупка: {self.region}."
        )

    @staticmethod
    def gender_to_text(gender: str) -> str:
        return "мужского пола" if gender == "male" else "женского пола"

    @staticmethod
    def gender_to_verb(gender: str) -> str:
        return "совершил" if gender == "male" else "совершила"

    @staticmethod
    def device_to_text(device: str) -> str:
        if device == "mobile":
            return "мобильного"
        elif device == "desktop":
            return "настольного"
        elif device == "tablet":
            return "планшетного"
        return "неизвестного"


def load_clients_from_csv(csv_path: str) -> list[Client]:
    clients = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            clients.append(Client.from_csv_row(row))
    return clients


def save_descriptions_to_txt(clients: list[Client], txt_path: str) -> None:
    with open(txt_path, "w", encoding="utf-8") as f:
        for client in clients:
            f.write(client.to_description() + "\n")


def process_clients(csv_path: str, txt_path: str) -> None:
    clients = load_clients_from_csv(csv_path)
    save_descriptions_to_txt(clients, txt_path)


if __name__ == "__main__":
    process_clients("web_clients_correct.csv", "clients_descriptions.txt")
