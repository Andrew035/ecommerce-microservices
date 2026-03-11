services:
  identity-db:
    image: postgres:alpine
    environment:
      POSTGRES_DB: identity_db

  identity-service:
    build: ./services/identity
    ports:
      - "8001:8000"
    depends_on:
      - identity-db

  product-db:
    image: postgres:alpine
    environment:
      POSTGRES_DB: product_db

  product-service:
    build: ./services/products
    ports:
      - "8002:8000"
    depends_on:
      - product-db
