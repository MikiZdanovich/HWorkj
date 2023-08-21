from task_3.src.services.animal_service import AnimalAPIService


def main():
    animal_name = input("Please enter the name of the animal: ")

    api_service = AnimalAPIService()
    try:
        animals = api_service.fetch_animals_by_name(animal_name)
        for animal in animals:
            print(f"Name: {animal.name}")
            print(f"Species: {animal.species}")
            print(f"Speed: {animal.speed}")
            print(f"Lifespan: {animal.lifespan}")
            print(f"Weight: {animal.weight}")
            print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
