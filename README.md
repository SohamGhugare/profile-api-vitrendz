# Official repo for Profile API built during VITrendz recruitments
## Techstack used:
- [FastAPI](fastapi.tiangolo.com/) - A backend python framework built on OpenAPI and Starlette with performance on par with Golang and NodeJS
- [SQLModel](sqlmodel.tiangolo.com/) - An ORM built by the same author of FastAPI with powerful integrations for CRUD and DBMS operations
- [Uvicorn](https://www.uvicorn.org/) - An ASGI server implementation acting as a platform for the API

## API Endpoints:
- GET `/clients/{id}` - Fetch a particular client.
- POST `/create-user` - Create a new user. Content-Type: application/json. Fields: [name, age, company, email]
    - **Possible errors thrown:**
        - 409 - Client already exists.
        - 400 - Email doesnt contain company name.
- DELETE `/clients/{id}` - Delete a particular client.
    - **Possible errors thrown:**
        - 400 - Client not found.