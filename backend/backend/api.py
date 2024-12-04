from ninja import NinjaAPI

app = NinjaAPI()


@app.get("hello")
def health_check(request):
    return {"message": "Hello, World!"}
