# Scalable Mircroservices-Based E-Commerce Backend Project

## 1. The High-Level Architecture
In a monolith, you have one database. In microservices, we follow the "__Database per Service__"
pattern. This prevents services from becoming tightly coupled.
- __Identity Service__: Manages users and issues __JWT (JSON Web Tokens)__ for authentication.
- __Product Service__: A catalog for inventory.
- __Order Service__: Coordinates between the user and the inventory to create a transaction.
- __API Gateway__: A single entry point (usually using Nginx or a dedicated FastAPI proxy)
  that routes requests to the correct service.

## 2. Project Structure
```Plaintext
ecommerce-microservices/
    services/
        identity/
            main.py
            Dockerfile
        products/
            main.py
            Dockerfile
        orders/
            main.py
            Dockerfile
    docker-compose.yml
    .env
```
