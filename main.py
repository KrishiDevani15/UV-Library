from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    print("Hello from example!")


if __name__ == "__main__":
    main()
