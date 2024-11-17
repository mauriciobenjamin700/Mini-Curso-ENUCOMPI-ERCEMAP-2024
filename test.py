from src.controllers.apply import predict, count_unique_animals
from src.controllers.save import to_json
from src.models.main import get_model


video = "videos/03.mp4"

model = get_model()

result = predict(video, model)

to_json(result, "frames.json")

cont = count_unique_animals(result)

to_json(cont, "count.json")

