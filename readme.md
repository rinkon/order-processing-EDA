# Event-Driven Order Processing System

A backend system demonstrating event-driven architecture using FastAPI, Celery, RabbitMQ, Redis, and PostgreSQL.

---

## 🚀 Tech Stack

* FastAPI
* Celery
* RabbitMQ
* Redis
* PostgreSQL
* Docker

---

## 📌 Features

* User registraition and login
* Redis-based idempotency handling
* Order creation API
* Order queuing with RabbitMQ
* Async order processing with Celery workers
* Order status tracking
* Order status updates via background tasks
* Persistent storage with PostgreSQL

---

## 🧠 Architecture

```
Client → FastAPI → PostgreSQL
                ↓
             Redis (idempotency)
                ↓
         RabbitMQ (queue)
                ↓
          Celery Workers
                ↓
        Update Order Status
```

---

## 📡 API Endpoints

### Create Order

```
POST /orders/
```

### Get Order

```
GET /orders/
```

---

## ⚙️ Core Flow

1. Client sends order request
2. FastAPI validates and stores order as PENDING
3. Idempotency key checked via Redis
4. Celery task queued via RabbitMQ
5. Worker processes order
6. Order status updated in PostgreSQL

---

## 🧩 Celery Worker Responsibilities

* Process order
* Update order status
* Handle retries (if configured)
* Maintain DB consistency

---

## 🐳 Running with Docker

Services:

* API service (FastAPI)
* Worker service (Celery)
* RabbitMQ
* Redis
* PostgreSQL

---

## 🔥 Design Principles

* Event-driven architecture
* Asynchronous processing
* Idempotent API design
* Decoupled worker system
* Stateless API layer


---

## 💬 Summary

This project simulates a production-style distributed order processing system using asynchronous task queues and event-driven design principles.
